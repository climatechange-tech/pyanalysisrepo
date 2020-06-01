import netCDF4 as n4
import numpy as np
import cftime

inc=n4.Dataset("../../geopotential_ERA5Land_ncfiles/geopotential_1279l4_0.1x0.1.nc")

lats_era5L=inc.variables["latitude"][:]
lons_era5L=inc.variables["longitude"][:]

times=inc.variables["time"]
timesarr=inc.variables["time"][:]
tunits=times.units
datetimes=cftime.num2date(timesarr,tunits)

zg0=inc.variables["z"][:].data

latlondict={"BILBAO_AEROPUERTO":              [-2.5423,43.1753],\
            "BIZKAIA_GUENES":                 [-3.0617,43.1212],\
            "BIZKAIA_LEKEITIO":               [-2.3037,43.2237],\
            "GIPUZKOA_HONDARRIBIA-MALKARROA": [-1.4732,43.2125],\
            "GIPUZKOA_IGELDO":                [-2.0228,43.1823],\
            "GIPUZKOA_ELGOIBAR":              [-2.2448,43.1234],\
            "GIPUZKOA_ZUMARRAGA":             [-2.1903,43.0448],\
            "GIPUZKOA_ZUMAIA" :               [-2.1504,43.1808]
}

cities=latlondict.keys()

ofile=open("geopotential_cities.txt",'w')

if len(times)==1:
    for city in cities:

        ilat=(abs(lats_era5L-latlondict[city][1])).argmin()
        ilon=(abs(lons_era5L-(latlondict[city][0]+360))).argmin()
        zg0_era5L=zg0[0,lat_idx,lon_idx]

        g0=9.80665
        z_era5L=zg0_era5L/g0

        #ofile_ind=open(city+".txt",'w')
        #ofile_ind.write("%s %f"%(city,z_era5L))
        #ofile_ind.close()

        ofile.write("%s %f\n" %(city,z_era5L))

ofile.close()
