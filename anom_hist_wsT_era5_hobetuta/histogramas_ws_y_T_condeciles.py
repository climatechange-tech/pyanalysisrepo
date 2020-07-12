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

def close_files(filelist):
    lf=len(filelist)
    for i in range(lf):
        filelist[i].close()

ofiles=[]

#####################
#Velocidad del viento
#####################

#
#Aeropuerto de Bilbo 
####################

ifile_bilbo='../aemet-climatologias_diarias/aemet_BILBAO_AERO_corrected.txt'
ifile_bilbo_era5L='../T_Td_ws_ERA5Land/era5Land_BILBO_AERO_dailymean.txt'

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
        t0=te
    elif (data_bilbo_era5[te,0]=="2001-02-01"):
        t1=te

ws_bilbo1=np.zeros((lb,2),"d")

ws_bilbo1[:t0+1,0]=data_bilbo[:t0+1,13]
ws_bilbo1[:t0+1,1]=data_bilbo_era5[:t0+1,-1]

ws_bilbo1[t0+1:,0]=data_bilbo[t0+1:,13]
ws_bilbo1[t0+1:,1]=data_bilbo_era5[t1:,-1]

#
#Calculo de histogramas
#

nmin1=int(np.nanmin(ws_bilbo1))
nmax1=int(np.nanmax(ws_bilbo1))

rangos_wsb=np.arange(nmin1,nmax1)
ws_bilbo_hist=np.histogram(ws_bilbo1[:,0],rangos_wsb)
data_bilbo_era5_hist=np.histogram(ws_bilbo1[:,1],rangos_wsb)

if ws_bilbo_hist[1][:].shape == data_bilbo_era5_hist[1][:].shape:
    lwsbh=len(ws_bilbo_hist[1])
 
ofile_hist_ws_bilbo=open('hist_ws_BILBAO_AERO.dat','w')
ofiles.append(ofile_hist_ws_bilbo)

for i in range(lwsbh-1):
    ofile_hist_ws_bilbo.write("%5.2f %4i %6.2f %4i \n" %(ws_bilbo_hist[1][i],ws_bilbo_hist[0][i],data_bilbo_era5_hist[1][i],data_bilbo_era5_hist[0][i]))

ofile_hist_ws_bilbo.write("%5.2f %4s %6.2f %4s" %(ws_bilbo_hist[1][-1],"   ",data_bilbo_era5_hist[1][-1],"   "))

#
#Calculo de histogramas por DECILES
#

ws_bilbo_deciles=np.zeros((10,4),'d')
lwsdb=len(ws_bilbo_deciles)
for i in range(lwsdb):
    decil=np.nanpercentile(ws_bilbo1,i*10+10)
    ws_bilbo_deciles[i,0]=i+1
    ws_bilbo_deciles[i,1]=decil

for i in range(lwsdb):
    ws_bilbo_deciles[i,2]=len(np.where(ws_bilbo1[:,0] < ws_bilbo_deciles[i,1])[0])
    ws_bilbo_deciles[i,3]=len(np.where(ws_bilbo1[:,1] < ws_bilbo_deciles[i,1])[0])

ws_bilbo_deciles[-1,2]=len(np.where(ws_bilbo1[:,0] <= ws_bilbo_deciles[-1,1])[0])
ws_bilbo_deciles[-1,3]=len(np.where(ws_bilbo1[:,1] <= ws_bilbo_deciles[-1,1])[0])
 
ofile_deciles_ws_bilbo=open('hist_decil_ws_BILBAO_AERO.dat','w')
ofiles.append(ofile_deciles_ws_bilbo)

for i in range(lwsdb):
    ofile_deciles_ws_bilbo.write("%i %5.2f %9.2f %6.2f \n" %(ws_bilbo_deciles[i,0],ws_bilbo_deciles[i,1],ws_bilbo_deciles[i,2],ws_bilbo_deciles[i,3]))


#
#Madrid, Cuatro Vientos
#######################

ifile_cv='../aemet-climatologias_diarias/aemet_CUATRO_VIENTOS_corrected.txt'
ifile_cv_era5L='../T_Td_ws_ERA5Land/era5Land_CUATRO_VIENTOS_dailymean.txt'

data_cv=lectura_datos(ifile_cv)
data_cv_era5=lectura_datos(ifile_cv_era5L)
lcv=len(data_cv)

#
#Fechas en fichero de datos era5 ya recortadas a [1986-01-01 : 2016-12-31]
#
#No hay discontinuidades
#

ws_cv1=np.zeros((lcv,2),"d")

ws_cv1[:,0]=data_cv[:,14]
ws_cv1[:,1]=data_cv_era5[:,-1]

ws_cv1[:,0]=data_cv[:,14]
ws_cv1[:,1]=data_cv_era5[:,-1]

#
#Calculo de histogramas
#

nmin2=int(np.nanmin(ws_cv1))
nmax2=int(np.nanmax(ws_cv1))

rangos_wscv=np.arange(nmin2,nmax2)
ws_cv_hist=np.histogram(ws_cv1[:,0],rangos_wscv)
ws_cv_era5_hist=np.histogram(ws_cv1[:,1],rangos_wscv)

if ws_cv_hist[1][:].shape == ws_cv_era5_hist[1][:].shape:
    lwscvh=len(ws_cv_hist[1])
 
ofile_hist_ws_cv=open('hist_ws_CUATRO_VIENTOS.dat','w')
ofiles.append(ofile_hist_ws_cv)

for i in range(lwscvh-1):
    ofile_hist_ws_cv.write("%5.2f %4i %6.2f %4i \n" %(ws_cv_hist[1][i],ws_cv_hist[0][i],ws_cv_era5_hist[1][i],ws_cv_era5_hist[0][i]))

ofile_hist_ws_cv.write("%5.2f %4s %6.2f %4s" %(ws_cv_hist[1][-1],"   ",ws_cv_era5_hist[1][-1],"   "))

#
#Calculo de histogramas por DECILES
#

ws_cv_deciles=np.zeros((10,4),'d')
lwsdcv=len(ws_cv_deciles)
for i in range(lwsdcv):
    decil=np.nanpercentile(ws_cv1,i*10+10)
    ws_cv_deciles[i,0]=i+1
    ws_cv_deciles[i,1]=decil

for i in range(lwsdcv):
    ws_cv_deciles[i,2]=len(np.where(ws_cv1[:,0] < ws_cv_deciles[i,1])[0])
    ws_cv_deciles[i,3]=len(np.where(ws_cv1[:,1] < ws_cv_deciles[i,1])[0])

ws_cv_deciles[-1,2]=len(np.where(ws_cv1[:,0] <= ws_cv_deciles[-1,1])[0])
ws_cv_deciles[-1,3]=len(np.where(ws_cv1[:,1] <= ws_cv_deciles[-1,1])[0])
 
ofile_deciles_ws_cv=open('hist_decil_ws_CUATRO_VIENTOS.dat','w')
ofiles.append(ofile_deciles_ws_cv)

for i in range(lwsdcv):
    ofile_deciles_ws_cv.write("%i %5.2f %9.2f %6.2f \n" %(ws_cv_deciles[i,0],ws_cv_deciles[i,1],ws_cv_deciles[i,2],ws_cv_deciles[i,3]))


##################
#Temperatura media
##################

#
#Aeropuerto de Bilbo 
####################

#
#Fechas en fichero de datos era5 ya recortadas a [1986-01-01 : 2016-12-31]
#
#Faltan datos de aemet entre [2000-11-20 : 2001-02-01],
#

for te in range(lbe):
    if (data_bilbo_era5[te,0]=="2000-11-20"):
        t0=te
    elif (data_bilbo_era5[te,0]=="2001-02-01"):
        t1=te

T_bilbo1=np.zeros((lb,2),"d")

T_bilbo1[:t0+1,0]=data_bilbo[:t0+1,6]
T_bilbo1[:t0+1,1]=data_bilbo_era5[:t0+1,1]

T_bilbo1[t0+1:,0]=data_bilbo[t0+1:,6]
T_bilbo1[t0+1:,1]=data_bilbo_era5[t1:,1]

#
#Calculo de histogramas
#

nmin3=int(np.nanmin(T_bilbo1))
nmax3=int(np.nanmax(T_bilbo1))

rangos_Tb=np.arange(nmin3,nmax3)
T_bilbo_hist=np.histogram(T_bilbo1[:,0],rangos_Tb)
T_bilbo_era5_hist=np.histogram(T_bilbo1[:,1],rangos_Tb)

if T_bilbo_hist[1][:].shape == T_bilbo_era5_hist[1][:].shape:
    lTbh=len(T_bilbo_hist[1])
 
ofile_hist_T_bilbo=open('hist_T_BILBAO_AERO.dat','w')
ofiles.append(ofile_hist_T_bilbo)

for i in range(lTbh-1):
    ofile_hist_T_bilbo.write("%5.2f %4i %6.2f %4i \n" %(T_bilbo_hist[1][i],T_bilbo_hist[0][i],T_bilbo_era5_hist[1][i],T_bilbo_era5_hist[0][i]))

ofile_hist_T_bilbo.write("%5.2f %4s %6.2f %4s" %(T_bilbo_hist[1][-1],"   ",T_bilbo_era5_hist[1][-1],"   "))

#
#Calculo de histogramas por DECILES
#

T_bilbo_deciles=np.zeros((10,4),'d')
lTdb=len(T_bilbo_deciles)
for i in range(lTdb):
    decil=np.nanpercentile(T_bilbo1,i*10+10)
    T_bilbo_deciles[i,0]=i+1
    T_bilbo_deciles[i,1]=decil

for i in range(lTdb):
    T_bilbo_deciles[i,2]=len(np.where(T_bilbo1[:,0] < T_bilbo_deciles[i,1])[0])
    T_bilbo_deciles[i,3]=len(np.where(T_bilbo1[:,1] < T_bilbo_deciles[i,1])[0])

T_bilbo_deciles[-1,2]=len(np.where(T_bilbo1[:,0] <= T_bilbo_deciles[-1,1])[0])
T_bilbo_deciles[-1,3]=len(np.where(T_bilbo1[:,1] <= T_bilbo_deciles[-1,1])[0])
 
ofile_deciles_T_bilbo=open('hist_decil_T_BILBAO_AERO.dat','w')
ofiles.append(ofile_deciles_T_bilbo)

for i in range(lTdb):
    ofile_deciles_T_bilbo.write("%i %5.2f %9.2f %6.2f \n" %(T_bilbo_deciles[i,0],T_bilbo_deciles[i,1],T_bilbo_deciles[i,2],T_bilbo_deciles[i,3]))



#
#Madrid, Cuatro Vientos
#######################

#
#Fechas en fichero de datos era5 ya recortadas a [1986-01-01 : 2016-12-31]
#
#No hay discontinuidades
#

T_cv1=np.zeros((lcv,2),"d")

T_cv1[:,0]=data_cv[:,7]
T_cv1[:,1]=data_cv_era5[:,1]

#
#Calculo de histogramas
#

nmin4=int(np.nanmin(T_cv1))
nmax4=int(np.nanmax(T_cv1))

rangos_Tcv=np.arange(nmin4,nmax4)
T_cv_hist=np.histogram(T_cv1[:,0],rangos_Tcv)
T_cv_era5_hist=np.histogram(T_cv1[:,1],rangos_Tcv)

if T_cv_hist[1][:].shape == T_cv_era5_hist[1][:].shape:
    lTcvh=len(T_cv_hist[1])
 
ofile_hist_T_cv=open('hist_T_CUATRO_VIENTOS.dat','w')
ofiles.append(ofile_hist_T_cv)

for i in range(lTcvh-1):
    ofile_hist_T_cv.write("%5.2f %4i %6.2f %4i \n" %(T_cv_hist[1][i],T_cv_hist[0][i],T_cv_era5_hist[1][i],T_cv_era5_hist[0][i]))

ofile_hist_T_cv.write("%5.2f %4s %6.2f %4s" %(T_cv_hist[1][-1],"   ",T_cv_era5_hist[1][-1],"   "))

#
#Calculo de histogramas por DECILES
#

T_cv_deciles=np.zeros((10,4),'d')
lTdcv=len(T_cv_deciles)
for i in range(lTdcv):
    decil=np.nanpercentile(T_cv1,i*10+10)
    T_cv_deciles[i,0]=i+1
    T_cv_deciles[i,1]=decil

for i in range(lTdcv):
    T_cv_deciles[i,2]=len(np.where(T_cv1[:,0] < T_cv_deciles[i,1])[0])
    T_cv_deciles[i,3]=len(np.where(T_cv1[:,1] < T_cv_deciles[i,1])[0])

T_cv_deciles[-1,2]=len(np.where(T_cv1[:,0] <= T_cv_deciles[-1,1])[0])
T_cv_deciles[-1,3]=len(np.where(T_cv1[:,1] <= T_cv_deciles[-1,1])[0])
 
ofile_deciles_T_cv=open('hist_decil_T_CUATRO_VIENTOS.dat','w')
ofiles.append(ofile_deciles_T_cv)

for i in range(lTdcv):
    ofile_deciles_T_cv.write("%i %5.2f %9.2f %6.2f \n" %(T_cv_deciles[i,0],T_cv_deciles[i,1],T_cv_deciles[i,2],T_cv_deciles[i,3]))


close_files(ofiles)
