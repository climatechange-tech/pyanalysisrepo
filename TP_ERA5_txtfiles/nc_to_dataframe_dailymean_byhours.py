import numpy as np
import pandas as pd
import glob
import os

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
        lista.append(eval(hilera[i]))
    return lista

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


var_time_list=["level"]

for i in range(24):
    time="%2.2d:00"%i
    var_time_list.append(time)

#################
#Gautegiz-Arteaga
#################

gar_era5_txtfiles=glob.glob("*ARTEAGA*.txt")
gar_era5_txtfiles.sort()

th=os.times()[-1]

shapes=[]
for txtf in gar_era5_txtfiles:
    sizer=lectura_datos(txtf)
    shapes.append(sizer.shape)

#if shapes[1:]==shapes[:-1]
if len(set(shapes))>1:
    raise ValueError("Matrize guztiek ez dute tamaina bera, ondoko tamainak daude:", set(shapes))
    
gar_era5_oneday=np.zeros((sizer.shape),'d')

for txtf in gar_era5_txtfiles:
    M=lectura_datos(txtf)
    gar_era5_oneday+=M    

gar_era5_oneday/=len(gar_era5_txtfiles)

init_date=gar_era5_txtfiles[0][37:-4]
fin_date=gar_era5_txtfiles[-1][37:-4]

ofile_gar_oneday=open("era5_TP_GAUTEGIZ-ARTEAGA_"+init_date+"_"+fin_date+"_dailymean_byhours.txt",'w')

for var in var_time_list:
    ofile_gar_oneday.write("#  %s"%var)
ofile_gar_oneday.write("\n")

for ilev in range(len(gar_era5_oneday)):
    for it in range(len(gar_era5_oneday[0])):
        ofile_gar_oneday.write("%8.2f" %gar_era5_oneday[ilev,it])
        if it==len(gar_era5_oneday[0])-1:
            ofile_gar_oneday.write("\n")

#####################
#Aeropuerto de Madrid
#####################

cv_era5_txtfiles=glob.glob("*MADRID*.txt")
cv_era5_txtfiles.sort()

shapes=[]
for txtf in cv_era5_txtfiles:
    sizer=lectura_datos(txtf)
    shapes.append(sizer.shape)

if len(set(shapes))>1:
    raise ValueError("Matrize guztiek ez dute tamaina bera, ondoko tamainak daude:", set(shapes))
    
cv_era5_oneday=np.zeros((sizer.shape),'d')

for txtf in cv_era5_txtfiles:
    M=lectura_datos(txtf)
    cv_era5_oneday+=M    

cv_era5_oneday/=len(cv_era5_txtfiles)

init_date=cv_era5_txtfiles[0][32:-4]
fin_date=cv_era5_txtfiles[-1][32:-4]

ofile_cv_oneday=open("era5_TP_MADRID-AERO_"+init_date+"_"+fin_date+"_dailymean_byhours.txt",'w')

for var in var_time_list:
    ofile_cv_oneday.write("#  %s"%var)
ofile_cv_oneday.write("\n")

for ilev in range(len(cv_era5_oneday)):
    for it in range(len(cv_era5_oneday[0])):
        ofile_cv_oneday.write("%8.2f" %cv_era5_oneday[ilev,it])
        if it==len(cv_era5_oneday[0])-1:
            ofile_cv_oneday.write("\n")

tb=os.times()[-1]

        
ofile_gar_oneday.close()
ofile_cv_oneday.close()

elapsed_time=abs(th-tb)

ordminseg(elapsed_time)
