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
    
def tempcorr_obs(T0,h0):
    """
    Temperatura ERA5 a 2m
    """
    Tobs_corr=T0+0.00649*(h0-2)
    return Tobs_corr
    
def tempcorr_ERA5(T0,h0):
    """
    Temperatura ERA5 a 2m
    """
    T_era5_corr=T0-0.00649*(h0-2)
    return T_era5_corr
    
    
def close_files(list_files):
    lf=len(list_files)
    for i in range(lf):
        list_files[i]

ofiles=[]
    
############################
#Guardar datos en dataframes
############################
   
ifile_bilbo="../aemet-climatologias_diarias/aemet_BILBAO_AERO_corrected.txt"
ifile_bilbo_era5L="../T_Td_ws_ERA5Land/era5Land_BILBO_AERO_dailymean.txt"

data_bilbo=lectura_datos(ifile_bilbo)
data_bilbo_era5L=lectura_datos(ifile_bilbo_era5L)

varstr_bilbo="fecha tmed tmin tmax wspeed"
varlist_bilbo=varstr_bilbo.split()

df_bilbo=pd.DataFrame(columns=varlist_bilbo)
df_bilbo.fecha=data_bilbo[:,0]
df_bilbo.tmed=data_bilbo[:,6]
df_bilbo.tmin=data_bilbo[:,8]
df_bilbo.tmax=data_bilbo[:,10]
df_bilbo.wspeed=data_bilbo[:,13]

varstr_bilbo_era5L="fecha T_2m Td_2m u_10 v_10 wind_speed_10 T_2m_max T_2m_min wind_speed_max wind_speed_min"
varlist_bilbo_era5L=varstr_bilbo_era5L.split()

df_bilbo_era5L=pd.DataFrame(data_bilbo_era5L,columns=varlist_bilbo_era5L)
df_bilbo_era5L.values[:,1:]=df_bilbo_era5L.values[:,1:].astype(np.float64)

ldfb=len(df_bilbo)
ldfbe=len(df_bilbo_era5L)        

#
#Faltan datos de aemet entre [2000-11-20 : 2001-02-01]
#

df_anom=pd.DataFrame(columns=["fechas_bilbo", "fechas_bilbo_era5L"])

df_anom.fechas_bilbo=df_bilbo.fecha
df_anom.fechas_bilbo_era5L=df_bilbo_era5L.fecha

ifalta=df_anom[df_anom.fechas_bilbo==df_anom.fechas_bilbo_era5L].index[-1]

try:
    igero=df_anom[df_anom.loc[ifalta+1].fechas_bilbo==df_anom.fechas_bilbo_era5L].index[0]
    print("Bilbo: Aemet eta ERA5 datuen matrizeak EZ DIRA tamaina berekoak: aemet ==> %i < ERA5 ==> %i" %(ldfb,ldfbe))
    gap=abs(igero-ifalta)
except:
    raise KeyError("Bilbo: Aemet eta ERA5 datuen matrizeak jada tamaina berekoak dira")    

df_bilbo1=pd.DataFrame(columns=varlist_bilbo)

"""
El indice derecho de la indexacion de los dataframes SI QUE ENTRA!!!!

CUIDADO: los valores de un dataframe que se sustituyen de otro, se hacen segun los indices!! El dataframe de Bilbo al ser mas corto,
cuando se sustituyan valores a partir del salto, los indices
no se corresponderan a los mayores que las de dentro del salto
"""

for t in range(ifalta+1):
    next_arr=[]
    for t1 in range(len(df_bilbo.loc[0])):
        next_arr.append(df_bilbo.loc[t][t1])

    next_arr=np.array(next_arr)[np.newaxis,:]
    next_df_bilbo1=pd.DataFrame(next_arr,columns=varlist_bilbo)

    df_bilbo1=pd.concat([df_bilbo1,next_df_bilbo1],ignore_index=True)

for t in range(ifalta+1,ifalta+gap):
    next_arr=[]
    for t1 in range(len(df_bilbo.loc[0])):
        next_arr.append(np.nan)
        
    next_arr=np.array(next_arr)[np.newaxis,:]   
    next_df_bilbo1=pd.DataFrame(next_arr,columns=varlist_bilbo)

    df_bilbo1=pd.concat([df_bilbo1,next_df_bilbo1],ignore_index=True)

    df_bilbo_era5L.loc[t] = np.nan

for t in range(ifalta+gap,ldfbe):
    next_arr=[]
    for t1 in range(len(df_bilbo.loc[0])):
        next_arr.append(df_bilbo.loc[t-gap+1][t1])        

    next_arr=np.array(next_arr)[np.newaxis,:]
    next_df_bilbo1=pd.DataFrame(next_arr,columns=varlist_bilbo)

    df_bilbo1=pd.concat([df_bilbo1,next_df_bilbo1],ignore_index=True)
   
df_bilbo1.values[:,1:]=df_bilbo1.values[:,1:].astype(np.float64)
   
ldfb1=len(df_bilbo1)

if ldfb1==ldfbe:
    print("Bilbon behatutako eta era5Land datu-baseak prozesatutako datuen matrizeak tamaina berekoak dira ")
else:
    raise ValueError("Bilbon behatutako eta era5Land datu-baseak prozesatutako datuen matrizeak EZ DIRA tamaina berekoak")
    
    
df_bilbo_era5L.values[:,1:]=df_bilbo_era5L.values[:,1:].astype(np.float64)

df_bilbo1=pd.concat([df_bilbo1,df_bilbo_era5L[df_bilbo_era5L.columns[1:]]],ignore_index=False,axis=1)

#################
#Regresion lineal
#################

"""
Buscar otros "nan"
"""

for irow in range(ldfb1):
    if (pd.isna(df_bilbo1.loc[irow].tmed)==True or pd.isna(df_bilbo1.loc[irow].tmin)==True or pd.isna(df_bilbo1.loc[irow].tmax)==True or pd.isna(df_bilbo1.loc[irow].wspeed)==True or pd.isna(df_bilbo1.loc[irow].tmed)==True):
        df_bilbo1.loc[irow]=np.nan


#####################################
#Normalizar los datos observados a 2m
#####################################

ifile_z="geopotential_ERA5Land_txtfiles/geopotential_to_z_cities.txt"
z=lectura_datos(ifile_z)
h_bilbo=z[0,1].astype(np.float64)

xT=tempcorr_obs(df_bilbo1.tmed.values.astype(np.float64),h_bilbo)
yT=df_bilbo1.T_2m.values.astype(np.float64)

xT=xT[np.logical_not(np.isnan(xT))]
yT=yT[np.logical_not(np.isnan(yT))]

xT_max=tempcorr_obs(df_bilbo1.tmax.values.astype(np.float64),h_bilbo)
yT_max=df_bilbo1.T_2m_max.values.astype(np.float64)

xT_max=xT_max[np.logical_not(np.isnan(xT_max))]
yT_max=yT_max[np.logical_not(np.isnan(yT_max))]

xT_min=tempcorr_obs(df_bilbo1.tmin.values.astype(np.float64),h_bilbo)
yT_min=df_bilbo1.T_2m_min.values.astype(np.float64)

xT_min=xT_min[np.logical_not(np.isnan(xT_min))]
yT_min=yT_min[np.logical_not(np.isnan(yT_min))]

xws=df_bilbo1.wspeed.values.astype(np.float64)
yws=df_bilbo1.wind_speed_10.values.astype(np.float64)

xws=xws[np.logical_not(np.isnan(xws))]
yws=yws[np.logical_not(np.isnan(yws))]

slope1,intercept1,r1,p1,stderr1=ss.linregress(xT,yT)
slope2,intercept2,r2,p2,stderr2=ss.linregress(xT_max,yT_max)
slope3,intercept3,r3,p3,stderr3=ss.linregress(xT_min,yT_min)
slope4,intercept4,r4,p4,stderr4=ss.linregress(xws,yws)

if np.all(np.isnan(ss.linregress(xT,yT))) or np.all(np.isnan(ss.linregress(xT_max,yT_max))) or np.all(np.isnan(ss.linregress(xT_min,yT_min))) or np.all(np.isnan(ss.linregress(xws,yws))) == True :
    raise ValueError("Kontuz! Matrizeetako bat(zu)ek nan balioa dutenentz behatu")

print("\nTendencia T Aeropuerto de Bilbo\n=====================================\n")
print("y_ERA5(t) = %.2f + %.2f T_OBS" %(intercept1,slope1))
print("Coeficiente de correlacion y determinacion de T entre aemet-era5Land: %5.2f, %5.2f" %(r1,r1**2))

print("\nTendencia Tmax Aeropuerto de Bilbo\n=====================================\n")
print("y_ERA5(t) = %.2f + %.2f T_OBS" %(intercept2,slope2))
print("Coeficiente de correlacion y determinacion de Tmax entre aemet-era5Land: %5.2f, %5.2f" %(r2,r2**2))

print("\nTendencia Tmin Aeropuerto de Bilbo\n=====================================\n")
print("y_ERA5(t) = %.2f + %.2f T_OBS" %(intercept3,slope3))
print("Coeficiente de correlacion y determinacion de Tmin entre aemet-era5Land: %5.2f, %5.2f" %(r3,r3**2))

print("\nTendencia wspeed Aeropuerto de Bilbo\n=====================================\n")
print("y_ERA5(t) = %.2f + %.2f T_OBS" %(intercept4,slope4))
print("Coeficiente de correlacion y determinacion de ws entre aemet-era5Land: %5.2f, %5.2f" %(r4,r4**2))

thres_bilbo_max=35
thres_bilbo_min=17

thres_bilbo_era5L_max = intercept2 + slope2*thres_bilbo_max
thres_bilbo_era5L_min = intercept3 + slope3*thres_bilbo_min

print("\nTreshold Tmax Aeropuerto de Bilbo ==> threshold Tmax Aeropuerto de Bilbo ERA5Land\n===================================================================\n")
print("%i ºC ==> %7.2f ºC" %(thres_bilbo_max,thres_bilbo_era5L_max))

print("\nTreshold Tmin Aeropuerto de Bilbo ==> threshold Tmin Aeropuerto de Bilbo ERA5Land\n===================================================================\n")
print("%i ºC ==> %7.2f ºC\n" %(thres_bilbo_min,thres_bilbo_era5L_min))


#####################
#Imprimir los valores
#####################


ofile_bilbo=open("Tdata_BILBO_AERO_sesgocorr.dat",'w')
ofiles.append(ofile_bilbo)

for i in range(len(xT_max)):
    ofile_bilbo.write("%7.3f %7.3f %7.3f %7.3f\n" %(xT_max[i],yT_max[i],xT_min[i],yT_min[i]))

"""
for irow in range(ldfb1):
    for ivar in range(len(df_bilbo1.loc[0])):
        if ivar==0:
            ofile_bilbo.write("%s "%df_bilbo1.loc[irow][ivar])
        if ivar > 0 and ivar <= len(df_bilbo1.loc[0])-1:
            ofile_bilbo.write("%8.3f "%df_bilbo1.loc[irow][ivar])
        if ivar == len(df_bilbo1.loc[0])-1:
            ofile_bilbo.write("\n")
"""
close_files(ofiles)
