import netCDF4 as n4
import numpy as np
import pandas as pd
import datetime
import glob
import os

def ordminseg(x):
    hours=int(x/3600)
    mins=int(int(x-3600*hours)/60)
    secs=x-(3600*hours+60*mins)

    if hours !=0:
        print("\nElapsed time: ",hours, "hours",mins,"minutes","%5.2f" %secs,"seconds.")
    else:
        if mins!=0:
            print("\nElapsed time: ",mins,"minutes","%5.2f" %secs,"seconds.")
        else:
            print("\nElapsed time: %5.2f" %secs,"seconds.")


ncfiles=glob.glob("../ncfiles/era5*nc")
ncfiles.sort()

var_time_list=["level"]

for i in range(24):
    time="%2.2d:00"%i
    var_time_list.append(time)

lvar=len(var_time_list)

df_dict={}

th=os.times()[-1]

for ncf in ncfiles:
    inc=n4.Dataset(ncf)
    lats_era5=inc.variables["latitude"][:]
    lons_era5=inc.variables["longitude"][:]

    times=inc.variables["time"]
    times_arr=inc.variables["time"][:]
    tunits=times.units
    recs=len(times_arr)

    levels=inc.variables["level"][:]
    T=inc.variables["t"][:]

    #Puntos de los que queremos extraer la serie de era5

 

    #MADRID AEROPUERTO

    lon_punto = -3.592496

    lat_punto = 40.509356

 

    #MADRID RETIRO

    #lon_punto = -3.683565

    #lat_punto = 40.412934

 

    #MADRID CIUDAD UNIVERSITARIA

    #lon_punto =  -3.732461

    #lat_punto = 40.445790

 

    #MADRID CUATRO VIENTOS

    #lon_punto = -3.786111

    #lat_punto = 40.375556

 

    #BILBAO AEROPUERTO

    #lon_punto = -2.906389

    #lat_punto = 43.293056

 

    #BIZKAIA GÜEÑES

    #lon_punto = -3.093440

    #lat_punto = 43.209887

 

    #BIZKAIA LEKEITIO

    #lon_punto = -2.505488

    #lat_punto = 43.364536

 
    #BIZKAIA GAUTEGIZ-ARTEAGA

    #lon_punto = -2.657
 
    #lat_punto = 43.347
 

    #Conseguir la celda en la que se encuentra la coordenada que queremos estudiar

    ilon = (np.abs(lons_era5 - lon_punto)).argmin()

    ilat = (np.abs(lats_era5 - lat_punto)).argmin()

    datetimes=n4.num2date(times_arr,tunits)

    #for it in range(recs):
    #    year = datetimes[it].year
    #    month = datetimes[it].month
    #    day = datetimes[it].day
    #    hour = datetimes[it].hour
    #    minute = datetimes[it].minute

    #    print("%4.4d-%2.2d-%2.2d %2.2d:%2.2d:%2.2d" %(year,month,day,hour,minute,second),T[it,ilev,ilat,ilon])

    #    print("%s %8.3f" %(df.loc[it].fecha,df.loc[it].temperatura_a_2_metros))

    df_dict[ncf]=pd.DataFrame(columns=var_time_list)
    
    df_dict[ncf][var_time_list[0]]=levels

    T0=273.15

    for t in range(1,lvar):
        df_dict[ncf][var_time_list[t]]=T[t-1,:,ilat,ilon]-T0

    for it in range(recs):
        year = datetimes[it].year
        month = datetimes[it].month
        day = datetimes[it].day
        hour = datetimes[it].hour
        minute = datetimes[it].minute

        ymd="%4.4d-%2.2d-%2.2d"%(year,month,day)

        ofile_T=open("era5_TP_MADRID_AERO_"+ymd+".txt",'w')
        for var in var_time_list:
            ofile_T.write("#  %s"%var)
        ofile_T.write("\n")
    
        for ilev in range(len(levels)):
            for var in var_time_list:
                ofile_T.write("%8.2f" %(df_dict[ncf][var][ilev]))
                if var==var_time_list[-1]:
                    ofile_T.write("\n")

        ofile_T.close()

    inc.close()

tb=os.times()[-1]

elapsed_time=abs(th-tb)

ordminseg(elapsed_time)