#!/usr/bin/env python

import certifi
import urllib3
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def ordminseg(x):
    hours=int(x/3600)
    mins=int(int(x-3600*hours)/60)
    secs=x-(3600*hours+60*mins)

    if hours !=0:
        print("\nElapsed time: ",hours, "hours",mins,"minutes","%5.2f" %secs,"seconds.")
    else:
        if mins!=0:
            print("\nElapsed time: ",mins,"minutes","%5.2f" %secs,"seconds.")


print("Current Working Directory " , os.getcwd())

import cdsapi

c = cdsapi.Client()

years=[]
for i in range(1986,1993):
    years.append(str(i))

#years=['2004']

months=['01','02','03','04','05','06','07','08','09','10','11','12']
days=  ['01', '02', '03',
        '04', '05', '06',
        '07', '08', '09',
        '10', '11', '12',
        '13', '14', '15',
        '16', '17', '18',
        '19', '20', '21',
        '22', '23', '24',
        '25', '26', '27',
        '28', '29', '30',
        '31']
times=['00:00','01:00','02:00','03:00','04:00','05:00','06:00',
       '07:00','08:00','09:00','10:00','11:00','12:00','13:00',
       '14:00','15:00','16:00','17:00','18:00','19:00','20:00',
       '21:00','22:00','23:00']

#data are stored in monthly tapes
#I create a function that recovers all the data that I need from a tape.

def DownloadBassicParamentersEra5SpainNc(year,month):
    c.retrieve(
         'reanalysis-era5-land',
         {
             'product_type':'reanalysis',
             'format':'netcdf',
             'variable':['2m_temperature','2m_dewpoint_temperature','10m_u_component_of_wind','10m_v_component_of_wind'],
             'year':year,
             'month':month,
             'day':days,
             'time':times,
             'area': [35,-10,44,5],
         },
         'era5Land_Spain_T_Td_ws_'+year+month+'.nc')
   

ti=os.times()[-1]

for y in years:
    for m in months:
        try:
            print('\nDownloading'+y+m+'---------------------------\n')
            DownloadBassicParamentersEra5SpainNc(y,m)
        except:
            continue

tf=os.times()[-1]

elapsed_time=abs(ti-tf)

ordminseg(elapsed_time)
