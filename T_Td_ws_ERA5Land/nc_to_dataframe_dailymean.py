import netCDF4 as n4
import numpy as np
import pandas as pd
import glob
import os

def ordminseg(x):
    hours=int(x/3600)
    mins=int(int(x-3600*hours)/60)
    secs=x-(3600*hours+60*mins)

    if hours !=0:
        print("\nElapsed time: ",hours, "hours",mins,"minutes %5.2f" %secs,"seconds.")
    else:
        if mins!=0:
            print("\nElapsed time: ",mins,"minutes %5.2f" %secs,"seconds.")
        else:
            print("\nElapsed time: %5.2f" %secs,"seconds.")

th=os.times()[-1]

ncfiles=glob.glob("*.nc")
ncfiles.sort()

varstr="fecha T_2m Td_2m u_10 v_10 wind_speed_10 T_2m_max T_2m_min wind_speed_max wind_speed_min"
varlist=varstr.split()

df_daily=pd.DataFrame(columns=varlist)

for ncf in ncfiles:
    inc=n4.Dataset(ncf)
    lats_era5=inc.variables["latitude"][:]
    lons_era5=inc.variables["longitude"][:]

    times=inc.variables["time"]
    times_arr=inc.variables["time"][:]
    tunits=times.units
    recs=len(times_arr)

    datetimes=n4.num2date(times_arr,tunits)

    t2m=inc.variables["t2m"][:].data
    d2m=inc.variables["d2m"][:].data
    T0=273.15

    u10=inc.variables["u10"][:].data
    v10=inc.variables["v10"][:].data
    speed_10=np.sqrt(u10**2+v10**2)

    
    #Puntos de los que queremos extraer la serie de era5

 

    #MADRID AEROPUERTO

    #lon_punto = -3.3320

    #lat_punto = 40.2800

 

    #MADRID RETIRO

    #lon_punto = -3.4041

    #lat_punto = 40.2443

 

    #MADRID CIUDAD UNIVERSITARIA

    #lon_punto =  -3.4327

    #lat_punto = 40.2706

 

    #MADRID CUATRO VIENTOS

    #lon_punto = -3.4710

    #lat_punto = 40.2232

 

    #BILBAO AEROPUERTO

    #lon_punto = -2.906389

    #lat_punto = 43.293056

 

    #BIZKAIA GÜEÑES

    #lon_punto = -3.0617

    #lat_punto = 43.1212

 

    #BIZKAIA LEKEITIO

    #lon_punto = -2.3037

    #lat_punto = 43.2237

 
    #BIZKAIA GAUTEGIZ-ARTEAGA

    #lon_punto = -2.657
 
    #lat_punto = 43.347


    #GIPUZKOA HONDARRIBIA-MALKARROA (MISMO QUE EL AEROPUERTO DE DONOSTIA)

    #lon_punto = -1.4732

    #lat_punto = 43.2125


    #GIPUZKOA IGELDO

    #lon_punto = -2.0228

    #lat_punto = 43.1823


    #GIPUZKOA ELGOIBAR

    #lon_punto = -2.2448

    #lat_punto = 43.1234


    #GIPUZKOA ZUMARRAGA

    #lon_punto = -2.1903

    #lat_punto = 43.0448


    #GIPUZKOA ZUMAIA

    lon_punto = -2.1504

    lat_punto = 43.1808


    ilon = (np.abs(lons_era5 - lon_punto)).argmin()
    ilat = (np.abs(lats_era5 - lat_punto)).argmin()

    for t in range(0,recs,24):
        t2m_avg=t2m[t:t+24,ilat,ilon].mean()-T0
        t2m_max=t2m[t:t+24,ilat,ilon].max()-T0
        t2m_min=t2m[t:t+24,ilat,ilon].min()-T0       
        
        d2m_avg=d2m[t:t+24,ilat,ilon].mean()-T0

        u10_avg=u10[t:t+24,ilat,ilon].mean()
        v10_avg=v10[t:t+24,ilat,ilon].mean()
        speed10_avg=speed_10[t:t+24,ilat,ilon].mean()
        speed10_max=speed_10[t:t+24,ilat,ilon].max()
        speed10_min=speed_10[t:t+24,ilat,ilon].min()        
        
        date=datetimes[t]

        year=date.year
        month=date.month
        day=date.day
        ymd="%4.4d-%2.2d-%2.2d" %(year,month,day)

        next_df=pd.DataFrame([[ymd,t2m_avg,d2m_avg,u10_avg,v10_avg,speed10_avg,t2m_max,t2m_min,speed10_max,speed10_min]],columns=varlist)
        df_daily=df_daily.append(next_df, ignore_index=True)

        print(df_daily)

ofile=open("era5Land_ZUMAIA_dailymean.txt",'w')
for var in varlist:
    ofile.write("#  "+var)
ofile.write(2*"\n")

for irow in range(len(df_daily)):
    for ivar in range(len(varlist)):
        if ivar==0:
            ofile.write("%s " %df_daily.loc[irow][ivar])
        if ivar > 0 and ivar <= len(varlist)-1:
            ofile.write("%7.2f " %df_daily.loc[irow][ivar])        
        if ivar==len(varlist)-1:
             ofile.write("\n")

tb=os.times()[-1]

elapsed_time=abs(th-tb)

ordminseg(elapsed_time)

ofile.close()
