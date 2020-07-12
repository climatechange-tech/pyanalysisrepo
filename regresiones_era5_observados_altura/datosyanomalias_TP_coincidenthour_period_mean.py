import numpy as np
import os
import glob
import pandas as pd

#import csv #posibles fallos en el almacenado de los datos

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

def listarray2array(listarray):
    array=np.array(listarray[0],dtype=np.float64)
    array=array[np.newaxis,:]

    llarray=len(listarray)
    for i in range(llarray):
        listarray[i]=np.array(listarray[i],dtype=np.float64)
        listarray[i]=listarray[i][np.newaxis,:]
        array=np.append(array,listarray[i],axis=0)
    
    return array
    

def aproximar(lista_valores,valor_dado):
    funcion_dif_abs = lambda list_valores: abs(list_valores-valor_dado)
    valor_aproximado=min(lista_valores,key=funcion_dif_abs)
    return valor_aproximado 

def close_files(list_files):
    lf=len(list_files)
    for i in range(lf):
        list_files[i]

def remove_duplicates_matrix(dupl_matrix):
    res_matrix=np.unique(dupl_matrix,axis=0)
    return res_matrix

def remove_duplicates(lista):
    res_list=list(dict.fromkeys(lista))
    return res_list

ofiles=[]

############
#Temperatura
############

#
#Gautegiz-Arteaga
#################

gar_fechas=[]

ifiles_T_gar_comp=glob.glob("euskalmet-era5*.txt")
ifiles_T_gar_comp.sort()

sizes=[]
for gar_txtf in ifiles_T_gar_comp:
    T_gar_comp=lectura_datos(gar_txtf)
    sizes.append(T_gar_comp.size)

lTgar=max(sizes)
lTgar1=lectura_datos(ifiles_T_gar_comp[0]).shape[1]
T_gar_comp_avg=np.zeros((lTgar,lTgar1),'d')
T_gar_comp_avg=pd.DataFrame(T_gar_comp_avg)

for gar_txtf in ifiles_T_gar:
    T_gar_comp=lectura_datos(gar_txtf)
    T_gar_comp_avg += T_gar_comp
    
T_gar_comp_avg /= len(ifiles_T_gar_comp)

date0=ifiles_T_gar_comp[0][-12:-4]
datef=ifiles_T_gar_comp[-1][-12:-4]

ofile_gar_comp=open('euskalmet-era5_TP_GAUTEGIZ_ARTEAGA_'+date0+'-'+datef+'.txt,'w')
ofiles.append(ofile_gar_comp)

for ip in range(lTgar):
    for ipcol in range(lTgar1)):
        ofile_gar_comp.write("%s " %df.loc[irow][ivar])
        if ipcol == len(df.loc[0])-1:
            ofile_gar_comp.write("\n")


#
#Aeropuerto de Madrid
#####################

cv_fechas=[]

ifiles_T_cv=glob.glob("../aemet-sondeos/*201403*CORR.txt")
ifiles_T_cv.sort()

sizes=[]
for cv_txtf in ifiles_T_cv_comp:
    T_cv_comp=lectura_datos(cv_txtf)
    sizes.append(T_cv_comp.size)

lTcv=max(sizes)
lTcv1=lectura_datos(ifiles_T_cv_comp[0]).shape[1]
T_cv_comp_avg=np.zeros((lTcv,lTcv1),'d')
T_cv_comp_avg=pd.DataFrame(T_cv_comp_avg)

for cv_txtf in ifiles_T_cv:
    T_cv_comp=lectura_datos(cv_txtf)
    T_cv_comp_avg += T_cv_comp
    
T_cv_comp_avg /= len(ifiles_T_cv_comp)

date0=ifiles_T_cv_comp[0][-12:-4]
datef=ifiles_T_cv_comp[-1][-12:-4]

ofile_cv_comp=open('aemet-era5_TP_MADRID_AERO'+date0+'-'+datef+'.txt,'w')
ofiles.append(ofile_cv_comp)

for ip in range(lTcv):
    for ipcol in range(lTcv1)):
        ofile_cv_comp.write("%s " %df.loc[irow][ivar])
        if ipcol == len(df.loc[0])-1:
            ofile_cv_comp.write("\n")

close_files(ofiles)
