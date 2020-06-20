import netCDF4 as n4
import numpy as np
import cftime

inc=n4.Dataset("geopotential_1279l4_0.1x0.1.nc")

lats=inc.variables["latitude"][:]
lons=inc.variables["longitude"][:]

times=inc.variables["time"]
timesarr=inc.variables["time"][:]
tunits=times.units
datetimes=cftime.num2date(timesarr,tunits)

z=inc.variables["z"][:]

print("Times length:",len(timesarr))

year=datetimes[0].year
month=datetimes[0].month
day=datetimes[0].day
hour=datetimes[0].hour
minute=datetimes[0].minute
second=datetimes[0].second

time="%4.4d-%2.2d-%2.2d %2.2d:%2.2d:%2.2d" %(year,month,day,hour,minute,second)

print("\nDate time:",time)

print("\nLats and lons: ",lats,lons)


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

 

    #BIZKAIA GUEÑES

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

    #lon_punto = -2.1504

    #lat_punto = 43.1808
