import numpy as np

def lectura_datos(fichero):
    file=open(fichero)
    fila=[]
    for line in file:
        hilera=line.split()
        if len(hilera)>0:
            if hilera[0]=="#":
                continue
            else:
                fila.append(listas(hilera))
    return np.array(fila)
    file.close()

def listas(hilera):
    lista=[]
    for i in range(len(hilera)):
        lista.append(hilera[i])
    return lista

def aproximar(lista_valores,valor_dado):
    funcion_dif_abs = lambda list_valores: abs(list_valores-valor_dado)
    valor_aproximado=min(lista_valores,key=funcion_dif_abs)
    return valor_aproximado 

def close_files(list_files):
    lf=len(list_files)
    for i in range(lf):
        list_files[i]

ofiles=[]

#
#Aeropuerto de Bilbo 
####################

ifile_bilbo='../aemet-climatologias_diarias/aemet_BILBAO_AERO_corr.txt'
ifile_bilbo_era5L='../T_Td_ws_ERA5Land/era5Land_BILBAO_AERO.txt'

data_bilbo=lectura_datos(ifile_bilbo)
data_bilbo_era5=lectura_datos(ifile_bilbo_era5L)
lb=len(data_bilbo)
lbe=len(data_bilbo_era5)

#
#Fechas en fichero de datos era5 ya recortadas a [1986-01-01 : 2016-12-31]
#
#Faltan datos de aemet entre [2000-11-20 : 2001-02-01]
#

for te in range(lbe):
    if (data_bilbo_era5[te,0]=="2000-11-20"):
        iok=te
    elif (data_bilbo_era5[te,0]=="2001-02-01"):
        ifalta=te

ws_bilbo_reduced=np.zeros((lbe,4),'U10')
#Cuarta columna: valores era5 corregidos por adicion de sesgo
lwsbr=len(ws_bilbo_reduced)

gap=abs(iok-ifalta)

#
#Faltan datos de aemet entre [2000-11-20 (7994 de era5): 2001-02-01 (8067 de era5)]
#  

for i in range(lbe):

    if i<=iok:
        date=data_bilbo_era5[i,0]
        ws_bilbo_reduced[i,0]=date
        ws_bilbo_reduced[i,1]=data_bilbo[i,6]
        ws_bilbo_reduced[i,2]=data_bilbo_era5[i,-1]
                                #Esta matriz proviene del fichero que ya tiene datos de ws, ws, rachas de viento, etc.
    elif (i>iok and i<ifalta):
        ws_bilbo_reduced[i,:]=" "

    elif i>=ifalta:
        newi=abs(i-gap+1)

        date=data_bilbo_era5[i,0]
        ws_bilbo_reduced[i,0]=date
        ws_bilbo_reduced[i,1]=data_bilbo[newi,6]
        ws_bilbo_reduced[i,2]=data_bilbo_era5[i,-1]
        
#
#Correccion del sesgo por cuantiles:
#matrices de los histogramas por deciles
#

ws_bilbo_decil=[]
ws_bilbo_era5_decil=[]

for i in range(lwsbr):
    if (ws_bilbo_reduced[i,1] == "nan" or ws_bilbo_reduced[i,2] == "nan" or ws_bilbo_reduced[i,1] == " " or ws_bilbo_reduced[i,2] == " " ):
        continue
    else:
        ws_bilbo_decil.append(float(ws_bilbo_reduced[i,1]))
        ws_bilbo_era5_decil.append(float(ws_bilbo_reduced[i,2]))

rangos_wsb_deciles=[]
rangos_wsb_era5_deciles=[]

for i in range(10):
    rangos_wsb_deciles.append(np.nanpercentile(ws_bilbo_decil,i*10+10))
    rangos_wsb_era5_deciles.append(np.nanpercentile(ws_bilbo_era5_decil,i*10+10))

#ws_bilbo_histd=np.histogram(ws_bilbo_decil,rangos_wsb_deciles) 
#ws_bilbo_era5_histd=np.histogram(ws_bilbo_era5_decil,rangos_wsb_era5_deciles)

#
#Si el valor reanalisis > valor observado:
#identificar valor percentil, y ANNADIR valor del reanalisis al observado
#
#Si el valor reanalisis < valor observado:
#identificar valor percentil, y RESTAR valor del reanalisis al observado
#

for i in range(lwsbr):

    if (ws_bilbo_reduced[i,1] != "nan" and ws_bilbo_reduced[i,2] != "nan"):
    
        if ws_bilbo_reduced[i,2] > ws_bilbo_reduced[i,1]:

            if (float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[0]):
   
                decil1=rangos_wsb_era5_deciles[0]
                vmp=aproximar(rangos_wsb_deciles,decil1)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])+vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[0] and float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[1]):

                #decil1=rangos_wsb_era5_deciles[0]
                vmp=aproximar(rangos_wsb_deciles,decil1)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])+vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[1] and float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[2]):

                decil2=rangos_wsb_era5_deciles[1]
                vmp=aproximar(rangos_wsb_deciles,decil2)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])+vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[2] and float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[3]):

                decil3=rangos_wsb_era5_deciles[2]
                vmp=aproximar(rangos_wsb_deciles,decil3)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])+vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[3] and float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[4]):

                decil4=rangos_wsb_era5_deciles[3]
                vmp=aproximar(rangos_wsb_deciles,decil4)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])+vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[4] and float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[5]):

                decil5=rangos_wsb_era5_deciles[4]
                vmp=aproximar(rangos_wsb_deciles,decil5)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])+vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[5] and float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[6]):

                decil6=rangos_wsb_era5_deciles[5]
                vmp=aproximar(rangos_wsb_deciles,decil6)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])+vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[6] and float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[7]):

                decil7=rangos_wsb_era5_deciles[6]
                vmp=aproximar(rangos_wsb_deciles,decil7)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])+vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[7] and float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[8]):

                decil8=rangos_wsb_era5_deciles[7]
                vmp=aproximar(rangos_wsb_deciles,decil8)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])+vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[8] and float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[9]):

                decil9=rangos_wsb_era5_deciles[8]
                vmp=aproximar(rangos_wsb_deciles,decil9)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])+vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[9]):

                decil10=rangos_wsb_era5_deciles[9]
                vmp=aproximar(rangos_wsb_deciles,decil10)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])+vmp

        elif (ws_bilbo_reduced[i,2] < ws_bilbo_reduced[i,1]):

            if (float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[0]):
   
                decil1=rangos_wsb_era5_deciles[0]
                vmp=aproximar(rangos_wsb_deciles,decil1)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])-vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[0] and float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[1]):

                #decil1=rangos_wsb_era5_deciles[0]
                vmp=aproximar(rangos_wsb_deciles,decil1)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])-vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[1] and float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[2]):

                decil2=rangos_wsb_era5_deciles[1]
                vmp=aproximar(rangos_wsb_deciles,decil2)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])-vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[2] and float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[3]):

                decil3=rangos_wsb_era5_deciles[2]
                vmp=aproximar(rangos_wsb_deciles,decil3)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])-vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[3] and float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[4]):

                decil4=rangos_wsb_era5_deciles[3]
                vmp=aproximar(rangos_wsb_deciles,decil4)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])-vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[4] and float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[5]):

                decil5=rangos_wsb_era5_deciles[4]
                vmp=aproximar(rangos_wsb_deciles,decil5)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])-vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[5] and float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[6]):

                decil6=rangos_wsb_era5_deciles[5]
                vmp=aproximar(rangos_wsb_deciles,decil6)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])-vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[6] and float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[7]):

                decil7=rangos_wsb_era5_deciles[6]
                vmp=aproximar(rangos_wsb_deciles,decil7)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])-vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[7] and float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[8]):

                decil8=rangos_wsb_era5_deciles[7]
                vmp=aproximar(rangos_wsb_deciles,decil8)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])-vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[8] and float(ws_bilbo_reduced[i,2]) < rangos_wsb_era5_deciles[9]):

                decil9=rangos_wsb_era5_deciles[8]
                vmp=aproximar(rangos_wsb_deciles,decil9)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])-vmp

            elif (float(ws_bilbo_reduced[i,2]) >= rangos_wsb_era5_deciles[9]):

                decil10=rangos_wsb_era5_deciles[9]
                vmp=aproximar(rangos_wsb_deciles,decil10)
                ws_bilbo_reduced[i,3]=float(ws_bilbo_reduced[i,2])-vmp


ofile_ws_bilbo_sesgo=open('ws_era5_sesgocorr_BILBAO_AERO.dat','w')
ofiles.append(ofile_ws_bilbo_sesgo)

for i in range(lwsbr):
    if (ws_bilbo_reduced[i,1] == "nan" or ws_bilbo_reduced[i,2] == "nan" or ws_bilbo_reduced[i,-1] == "nan" or np.all(ws_bilbo_reduced[i,:]==" ")==True):
        ofile_ws_bilbo_sesgo.write("\n")
    else:
        ofile_ws_bilbo_sesgo.write("%s %5.2f %5.2f \n" %(ws_bilbo_reduced[i,0],float(ws_bilbo_reduced[i,2]),float(ws_bilbo_reduced[i,3])))
 
#
#Madrid, Cuatro Vientos
#######################

ifile_cv='../aemet-climatologias_diarias/aemet_CUATRO_VIENTOS_corr.txt'
ifile_cv_era5L='../T_Td_ws_ERA5Land/era5Land_CUATRO_VIENTOS.txt'

data_cv=lectura_datos(ifile_cv)
data_cv_era5=lectura_datos(ifile_cv_era5L)
lcv=len(data_cv)
lcve=len(data_cv_era5)

#
#Fechas en fichero de datos era5 ya recortadas a [1986-01-01 : 2016-12-31]
#

ws_cv_reduced=np.zeros((lcve,4),'U10')
lwscvr=len(ws_cv_reduced)

#
#No hay discontinuidades
#    

for i in range(lcve):

    date=data_cv_era5[i,0]
    ws_cv_reduced[i,0]=date
    ws_cv_reduced[i,1]=data_cv[i,7]
    ws_cv_reduced[i,2]=data_cv_era5[i,-1]

#
#Correccion del sesgo por cuantiles:
#matrices de los histogramas por deciles
#

ws_cv_decil=[]
ws_cv_era5_decil=[]

for i in range(lwscvr):
    if (ws_cv_reduced[i,1] == "nan" or ws_cv_reduced[i,2] == "nan" or ws_cv_reduced[i,1] == " " or ws_cv_reduced[i,2] == " " ):
        continue
    else:
        ws_cv_decil.append(float(ws_cv_reduced[i,1]))
        ws_cv_era5_decil.append(float(ws_cv_reduced[i,2]))

rangos_wscv_deciles=[]
rangos_wscv_era5_deciles=[]

for i in range(10):
    rangos_wscv_deciles.append(np.nanpercentile(ws_cv_decil,i*10+10))
    rangos_wscv_era5_deciles.append(np.nanpercentile(ws_cv_era5_decil,i*10+10))

#ws_cv_histd=np.histogram(ws_cv_decil,rangos_wsb_deciles) 
#ws_cv_era5_histd=np.histogram(ws_cv_era5_decil,rangos_wsb_deciles)

#
#Si el valor observado > valor reanalisis:
#identificar valor percentil, y añadir valor observado al del reanalisis
#
#Si el valor observado < valor reanalisis:
#identificar valor percentil, y restar valor observado al del reanalisis
#

for i in range(lwscvr):

    if (ws_cv_reduced[i,1] != "nan" and ws_cv_reduced[i,2] != "nan"):
    
        if ws_cv_reduced[i,2] > ws_cv_reduced[i,1]:

            if (float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[0]):
   
                decil1=rangos_wscv_era5_deciles[0]
                vmp=aproximar(rangos_wscv_deciles,decil1)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])+vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[0] and float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[1]):

                #decil1=rangos_wscv_era5_deciles[0]
                vmp=aproximar(rangos_wscv_deciles,decil1)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])+vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[1] and float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[2]):

                decil2=rangos_wscv_era5_deciles[1]
                vmp=aproximar(rangos_wscv_deciles,decil2)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])+vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[2] and float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[3]):

                decil3=rangos_wscv_era5_deciles[2]
                vmp=aproximar(rangos_wscv_deciles,decil3)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])+vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[3] and float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[4]):

                decil4=rangos_wscv_era5_deciles[3]
                vmp=aproximar(rangos_wscv_deciles,decil4)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])+vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[4] and float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[5]):

                decil5=rangos_wscv_era5_deciles[4]
                vmp=aproximar(rangos_wscv_deciles,decil5)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])+vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[5] and float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[6]):

                decil6=rangos_wscv_era5_deciles[5]
                vmp=aproximar(rangos_wscv_deciles,decil6)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])+vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[6] and float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[7]):

                decil7=rangos_wscv_era5_deciles[6]
                vmp=aproximar(rangos_wscv_deciles,decil7)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])+vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[7] and float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[8]):

                decil8=rangos_wscv_era5_deciles[7]
                vmp=aproximar(rangos_wscv_deciles,decil8)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])+vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[8] and float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[9]):

                decil9=rangos_wscv_era5_deciles[8]
                vmp=aproximar(rangos_wscv_deciles,decil9)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])+vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[9]):

                decil10=rangos_wscv_era5_deciles[9]
                vmp=aproximar(rangos_wscv_deciles,decil10)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])+vmp

        elif (ws_cv_reduced[i,2] < ws_cv_reduced[i,1]):

            if (float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[0]):
   
                decil1=rangos_wscv_era5_deciles[0]
                vmp=aproximar(rangos_wscv_deciles,decil1)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])-vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[0] and float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[1]):

                #decil1=rangos_wscv_era5_deciles[0]
                vmp=aproximar(rangos_wscv_deciles,decil1)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])-vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[1] and float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[2]):

                decil2=rangos_wscv_era5_deciles[1]
                vmp=aproximar(rangos_wscv_deciles,decil2)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])-vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[2] and float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[3]):

                decil3=rangos_wscv_era5_deciles[2]
                vmp=aproximar(rangos_wscv_deciles,decil3)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])-vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[3] and float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[4]):

                decil4=rangos_wscv_era5_deciles[3]
                vmp=aproximar(rangos_wscv_deciles,decil4)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])-vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[4] and float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[5]):

                decil5=rangos_wscv_era5_deciles[4]
                vmp=aproximar(rangos_wscv_deciles,decil5)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])-vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[5] and float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[6]):

                decil6=rangos_wscv_era5_deciles[5]
                vmp=aproximar(rangos_wscv_deciles,decil6)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])-vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[6] and float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[7]):

                decil7=rangos_wscv_era5_deciles[6]
                vmp=aproximar(rangos_wscv_deciles,decil7)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])-vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[7] and float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[8]):

                decil8=rangos_wscv_era5_deciles[7]
                vmp=aproximar(rangos_wscv_deciles,decil8)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])-vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[8] and float(ws_cv_reduced[i,2]) < rangos_wscv_era5_deciles[9]):

                decil9=rangos_wscv_era5_deciles[8]
                vmp=aproximar(rangos_wscv_deciles,decil9)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])-vmp

            elif (float(ws_cv_reduced[i,2]) >= rangos_wscv_era5_deciles[9]):

                decil10=rangos_wscv_era5_deciles[9]
                vmp=aproximar(rangos_wscv_deciles,decil10)
                ws_cv_reduced[i,3]=float(ws_cv_reduced[i,2])-vmp

ofile_ws_cv_sesgo=open('ws_era5_sesgocorr_CUATRO_VIENTOS.dat','w')
ofiles.append(ofile_ws_cv_sesgo)

for i in range(lwscvr):
    if (ws_cv_reduced[i,1] == "nan" or ws_cv_reduced[i,2] == "nan" or ws_cv_reduced[i,-1] == "nan" or np.all(ws_cv_reduced[i,:]==" ")==True):
        ofile_ws_cv_sesgo.write("\n")
    else:
        ofile_ws_cv_sesgo.write("%s %5.2f %5.2f \n" %(ws_cv_reduced[i,0],float(ws_cv_reduced[i,2]),float(ws_cv_reduced[i,3])))

close_files(ofiles)
