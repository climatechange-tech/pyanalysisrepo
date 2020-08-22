import netCDF4 as n4
import numpy as np
import cftime

inc=n4.Dataset("../../../geopotential_ERA5Land_ncfiles/geo_1279l4_0.1x0.1.grib2_v4_unpack.nc")

lats_era5L=inc.variables["latitude"][:]
lons_era5L=inc.variables["longitude"][:]

times=inc.variables["time"]
timesarr=inc.variables["time"][:]
tunits=times.units
datetimes=cftime.num2date(timesarr,tunits)

zg0=inc.variables["z"][:].data

latlondict={"BILBAO_AEROPUERTO":              [-2.90643,43.29806,42],\
            "BIZKAIA_GUENES":                 [-3.10468,43.20331,208],\
            "BIZKAIA_LEKEITIO":               [-2.5103,43.37693,12],\
            "GIPUZKOA_HONDARRIBIA-MALKARROA": [-1.8509,43.31406,4],\
            "GIPUZKOA_IGELDO":                [-2.0409,43.30631,251],\
            "GIPUZKOA_ELGOIBAR":              [-2.41331,43.21618,119],\
            "GIPUZKOA_ZUMARRAGA":             [-2.31743,43.07993,420],\
            "GIPUZKOA_ZUMAIA" :               [-2.2511,43.30218,28],\
            "ARABA_FORONDA":                  [-2.7351,42.88193,513],\
            "ARABA_GASTEIZ_AEROPUERTO":       [-2.73281,42.87193,513],\
            "PAMPLONA_AEROPUERTO":            [-1.645271,42.769901,459],\
            "NAFARROA_CADREITA":              [-1.685134,42.225150,268],\
}


cities=list(latlondict.keys())

ofile=open("geopotential_to_z_cities.txt",'w')

if len(times)==1:
    for city in cities:

        ilat=(abs(lats_era5L-latlondict[city][1])).argmin()
        ilon=(abs(lons_era5L-(latlondict[city][0]+360))).argmin()
        zg0_era5L=zg0[0,ilat,ilon]

        g0=9.80665
        z_era5L=zg0_era5L/g0

        ofile_ind=open("era5Land_"+city+".txt",'w')
        ofile_ind.write("%s %f"%(city,z_era5L))
        ofile_ind.close()

        z_real=latlondict[city][-1]
        ofile.write("%s: %.0f %i\n" %(city,z_era5L,z_real))

ofile.close()
