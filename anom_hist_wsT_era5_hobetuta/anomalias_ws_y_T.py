import numpy as np
import os
import glob

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


####################
#Aeropuerto de Bilbo
####################

ifile_bilbo="../aemet-climatologias_diarias/aemet_BILBAO_AERO_corr.txt"
ifile_era5L_bilbo="../T_Td_ws_ERA5Land/era5Land_BILBAO_AERO.txt"

data_bilbo=lectura_datos(ifile_bilbo)
data_bilbo_era5=lectura_datos(ifile_era5L_bilbo)
lb=len(data_bilbo)
leb=len(data_bilbo_era5)

#
#Velocidad media del viento
###########################

#Datos de aemet: [1986-01-01 : 2016-12-31]
#Datos de era5, ya recortadas a [1986-01-01 : 2016-12-31]

anom_ws_bilbo=np.zeros((leb,2),'U10')

for te in range(leb):
    if data_bilbo_era5[te,0]=="2000-11-20":
        iok=te
    elif data_bilbo_era5[te,0]=="2001-02-01":
        ifalta=te

gap=abs(iok-ifalta)

#
#Faltan datos de aemet entre [2000-11-20 (7994 de era5): 2001-02-01 (8067 de era5)]
#  

for i in range(leb):

    if i<=iok:
        date=data_bilbo_era5[i,0]
        anom_ws_bilbo[i,0]=date
        anom_ws_bilbo[i,-1]=float(data_bilbo[i,13])-float(data_bilbo_era5[i,-1])
        
    elif (i>iok and i<ifalta):
        anom_ws_bilbo[i,:]=" "

    elif i>=ifalta:
        newi=abs(i-gap+1)

        date=data_bilbo_era5[i,0]
        anom_ws_bilbo[i,0]=date
        anom_ws_bilbo[i,-1]=float(data_bilbo[newi,13])-float(data_bilbo_era5[i,-1]) 
   
ofile_anom_ws_bilbo=open('anom_ws_BILBAO_AERO.dat','w')

for i in range(leb):
    if (anom_ws_bilbo[i,-1] == ' ' or anom_ws_bilbo[i,-1] == np.nan):
        ofile_anom_ws_bilbo.write("\n")
    else:
        ofile_anom_ws_bilbo.write("%s %5.2f \n" %(anom_ws_bilbo[i,0],float(anom_ws_bilbo[i,1])))


#
#Temperatura media
##################

#Datos de era5: [1979-01-01 : 2019-12-31]
#Datos de aemet: [1986-01-01 : 2016-12-31]

#Las fechas ya estan recortadas, se tienen dimensiones iguales

anom_T_bilbo=np.zeros((leb,2),'U10')

for i in range(leb):
    if data_bilbo_era5[i,0]=="2000-11-20":
        iok=i
    elif data_bilbo_era5[i,0]=="2001-02-01":
        ifalta=i

gap=abs(iok-ifalta)

for i in range(leb):

#
#   Faltan datos de aemet entre [2000-11-20 (7994 de era5): 2001-02-01 (8067 de era5)]
#  

    if i<=iok:
        date=data_bilbo_era5[i,0]
        anom_T_bilbo[i,0]=date
        anom_T_bilbo[i,-1]=float(data_bilbo[i,6])-float(data_bilbo_era5[i,1])
                                #Esta matriz proviene del fichero que ya tiene datos de T, ws, rachas de viento, etc.
    elif (i>iok and i<ifalta):
        anom_T_bilbo[i,:]=" "

    elif i>=ifalta:
        newi=abs(i-gap+1)

        date=data_bilbo_era5[i,0]
        anom_T_bilbo[i,0]=date
        anom_T_bilbo[i,-1]=float(data_bilbo[newi,6])-float(data_bilbo_era5[i,1])
   
ofile_anom_T_bilbo=open('anom_T_BILBAO_AERO.dat','w')

for i in range(leb):
    if (anom_T_bilbo[i,-1] == ' ' or anom_T_bilbo[i,-1] == np.nan):
        ofile_anom_T_bilbo.write("\n")
    else:
        ofile_anom_T_bilbo.write("%s %5.2f \n" %(anom_T_bilbo[i,0],float(anom_T_bilbo[i,1])))

#######################
#Madrid, Cuatro Vientos
#######################

ifile_cv='../aemet-climatologias_diarias/aemet_CUATRO_VIENTOS_corr.txt'
ifile_era5L_cv='../T_Td_ws_ERA5Land/era5Land_CUATRO_VIENTOS.txt'

data_cv=lectura_datos(ifile_cv)
data_cv_era5=lectura_datos(ifile_era5L_cv)
lcv=len(data_cv)
lecv=len(data_cv_era5)

#
#Velocidad media del viento
###########################

#Datos de aemet: [1986-01-01 : 2016-12-31]
#Datos de era5, ya recortadas a [1986-01-01 : 2016-12-31]

#No hay discontinuidades

anom_ws_cv=np.zeros((lecv,2),'U10')

for i in range(lecv):

    date=data_cv_era5[i,0]
    anom_ws_cv[i,0]=date
    anom_ws_cv[i,-1]=float(data_cv[i,14])-float(data_cv_era5[i,-1])

ofile_anom_ws_cv=open('anom_ws_CUATRO_VIENTOS.dat','w')

for i in range(lecv):
    if anom_ws_cv[i,-1] == np.nan:
        ofile_anom_ws_cv.write("\n")
    else:
        ofile_anom_ws_cv.write("%s %5.2f \n" %(anom_ws_cv[i,0],float(anom_ws_cv[i,1])))


#
#Temperatura media
##################

#Datos de era5: [1979-01-01 : 2019-12-31], ya recortadas a [1986-01-01 : 2016-12-31]
#Datos de aemet: [1986-01-01 : 2016-12-31]

#Las fechas ya estan recortadas, se tienen dimensiones iguales

anom_T_cv=np.zeros((lecv,2),'U10')

#
#No hay discontinuidades
#   

for i in range(lecv):

    date=data_cv_era5[i,0]
    anom_T_cv[i,0]=date
    anom_T_cv[i,-1]=float(data_cv[i,7])-float(data_cv_era5[i,1])

ofile_anom_T_cv=open('anom_T_CUATRO_VIENTOS.dat','w')

for i in range(lecv):
    if anom_T_cv[i,-1] == np.nan:
        ofile_anom_T_cv.write("\n")
    else:
        ofile_anom_T_cv.write("%s %5.2f \n" %(anom_T_cv[i,0],float(anom_T_cv[i,1])))

###################
#Cierre de ficheros
###################

ofile_anom_ws_bilbo.close()
ofile_anom_ws_cv.close()
