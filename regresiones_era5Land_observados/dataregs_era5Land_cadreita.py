import numpy as np
import pandas as pd
import scipy.stats as ss

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

def close_files(list_files):
    lf=len(list_files)
    for i in range(lf):
        list_files[i]

ofiles=[]

############################
#Guardar datos en dataframes
############################

ifile="../aemet-climatologias_diarias/aemet_CADREITA_corrected.txt"
ifile_era5L="../T_Td_ws_ERA5Land/era5Land_CADREITA_dailymean.txt"

data=lectura_datos(ifile)
data_era5L=lectura_datos(ifile_era5L)

l=len(data)
le=len(data_era5L)

varstr_all="fecha tmin tmin_era5L tmax tmax_era5L"
varlist=varstr_all.split()

fechas=data[:,0]
fechas_era5L=data_era5L[:,0]

#
#Descartar fechas ERA5 que no estan disponibles en datos observados
#

ifirst=np.where(fechas_era5L==fechas[0])[0][0]

df_comp=pd.DataFrame(columns=varlist)

for t in range(ifirst,le):
    ifecha = np.where(fechas_era5L[t]==fechas)

    if ifecha[0].shape[0] > 0:

        ifecha=ifecha[0][0]
        ifecha_era5 = np.where(fechas_era5L==fechas[ifecha])[0][0]

        fecha       = data[ifecha,0]
        tmin        = data[ifecha,7]
        tmin_era5L  = data_era5L[ifecha_era5,7]
        tmax        = data[ifecha,9]
        tmax_era5L  = data_era5L[ifecha_era5,6]

        if (tmin=="nan" or tmax=="nan"):
            next_arr=np.repeat(np.nan,len(varlist))
            next_df=pd.DataFrame([next_arr],columns=varlist)
            df_comp=pd.concat([df_comp,next_df],ignore_index=True)

        else:
            next_arr=np.array([[fecha,tmin,tmin_era5L,tmax,tmax_era5L]])
            next_df=pd.DataFrame(next_arr,columns=varlist)
            df_comp=pd.concat([df_comp,next_df],ignore_index=True)

    else:

        next_arr=np.repeat(np.nan,len(varlist))
        next_df=pd.DataFrame([next_arr],columns=varlist)
        df_comp=pd.concat([df_comp,next_df],ignore_index=True)

df_comp.values[:,1:]=df_comp.values[:,1:].astype(np.float64)

#################
#Regresion lineal
#################

ldfc=len(df_comp)

xT_max=df_comp.tmax.values.astype(np.float64)
yT_max=df_comp.tmax_era5L.values.astype(np.float64)

xT_max=xT_max[np.logical_not(np.isnan(xT_max))]
yT_max=yT_max[np.logical_not(np.isnan(yT_max))]

xT_min=df_comp.tmin.values.astype(np.float64)
yT_min=df_comp.tmin_era5L.values.astype(np.float64)

xT_min=xT_min[np.logical_not(np.isnan(xT_min))]
yT_min=yT_min[np.logical_not(np.isnan(yT_min))]

slope1,intercept1,r1,p1,stderr1=ss.linregress(xT_max,yT_max)
slope2,intercept2,r2,p2,stderr2=ss.linregress(xT_min,yT_min)


print("\nTendencia Tmax Cadreita\n=====================================\n")

print(("y_ERA5Land(t) = %.2f + %.2f T_OBS" %(intercept1,slope1)))
print(("Coeficiente de correlacion y determinacion de Tmax entre aemet-era5Land: %5.2f, %5.2f" %(r1,r1**2)))

thres_max=36
thres_era5L_max = intercept1 + slope1*thres_max

print("\nTreshold Tmax Cadreita ==> threshold Tmax Cadreita ERA5Land\n===================================================================\n")
print(("%i ºC ==> %7.2f ºC" %(thres_max,thres_era5L_max)))

thres_min=18
thres_era5L_min = intercept2 + slope2*thres_min

print("\nTendencia Tmin Cadreita\n=====================================\n")
print(("Coeficiente de correlacion y determinacion de Tmin entre aemet-era5Land: %5.2f, %5.2f" %(r2,r2**2)))
print(("y_ERA5Land(t) = %.2f + %.2f T_OBS" %(intercept2,slope2)))

print("\nTreshold Tmin Cadreita ==> threshold Tmin Cadreita ERA5Land\n===================================================================\n")
print(("%i ºC ==> %7.2f ºC\n" %(thres_min,thres_era5L_min)))


#####################
#Imprimir los valores
#####################


ofile=open("Tdata_CADREITA.dat",'w')
ofiles.append(ofile)

for i in range(len(xT_max)):
    ofile.write("%7.3f %7.3f %7.3f %7.3f\n" %(xT_max[i],yT_max[i],xT_min[i],yT_min[i]))

"""
for irow in range(ldfc):
    for ivar in range(len(df_comp.loc[0])):
        if ivar==0:
            ofile.write("%s "%df_comp.loc[irow][ivar])
        if ivar > 0 and ivar <= len(df_comp.loc[0])-1:
            ofile.write("%8.3f "%df_comp.loc[irow][ivar])
        if ivar == len(df_comp.loc[0])-1:
            ofile.write("\n")
"""

close_files(ofiles)