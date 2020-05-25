import numpy as np
import os
import glob

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

ifiles_T_gar=glob.glob("../euskalmet-sondeos/*201403*dataonly.txt")
ifiles_T_gar.sort()

for f_T_gar in ifiles_T_gar:
    filename_noext=os.path.splitext(f_T_gar)[0]
    fecha=filename_noext[29:37]   
    gar_fechas.append(fecha)

lgarf=len(gar_fechas)

gar_era5_fechas=[]

ifiles_T_era5_gar = glob.glob("../TP_ERA5/txtfiles/*TP*ARTEAGA*2014-03*.txt")
ifiles_T_era5_gar.sort()

for f_T_era5_gar in ifiles_T_era5_gar:
    filename_noext=os.path.splitext(f_T_era5_gar)[0]

    agno=filename_noext[45:49]
    mes=filename_noext[50:52]
    dia=filename_noext[53:55]
    fecha=agno+mes+dia

    gar_era5_fechas.append(fecha)

lgaref=len(gar_era5_fechas)

T_gar_comp={}

horas_era5=[]

for t in range(24):
    time=int("%2.2d00"%t)
    horas_era5.append(time)

horas_era5=np.array(horas_era5,dtype=np.int64)
#horas_era5=np.array(horas_era5,dtype='int64')
#horas_era5=np.array(horas_era5)

"""
for txtf in 

T_gar_cumul=np.zeros((lTgar,3),'d')
"""

for t in range(lgarf):
    for te in range(lgaref):
        if gar_fechas[t] == gar_era5_fechas[te]:

            if_T_era5_gar=ifiles_T_era5_gar[te]
            if_T_gar=ifiles_T_gar[t]

            T_gar_era5=lectura_datos(if_T_era5_gar)
            T_gar=lectura_datos(if_T_gar)

            if isinstance(T_gar,np.float64)==False or isinstance(T_gar_era5,np.float64)==False:
                T_gar=np.array(T_gar,dtype=np.float64)
                T_gar_era5=np.array(T_gar_era5,dtype=np.float64)

            lTgar=len(T_gar)
            lTegar=len(T_gar_era5)

            ymd=gar_fechas[t]
            T_gar_comp[ymd]=np.zeros((lTgar,4),'d')

            
            hora_gar=1200
            hora_gar_era5=aproximar(horas_era5,hora_gar)
            ihora_gar_era5=np.where(horas_era5==hora_gar_era5)[0][0]
     
            for ip in range(lTgar):
                paprox=aproximar(T_gar_era5[:,0],T_gar[ip,0])
                ipaprox=np.where(T_gar_era5[:,0]==paprox)[0][0]
                          
            #Preferencia de presiones: Euskalmet, por ser datos observados,
            #PERO las alturas de ERA5 son mas redondeadas, por lo que
            #estos datos estaran repetidos en algunas alturas,
            #y no se puede usar np.unique para remover los elementos repetidos.
            #
            #Por tanto, se cambia la preferencia a ERA5,
            #aunque el numero de datos se reduzca en un 25 pciento
            #MODIFICARLO!!!!!!
                T_gar_comp[ymd][ip,0]=T_gar[ip,0]
                T_gar_comp[ymd][ip,1]=T_gar[ip,2]
                T_gar_comp[ymd][ip,2]=T_gar_era5[ipaprox,ihora_gar_era5+1]
                T_gar_comp[ymd][ip,3]=T_gar_comp[ymd][ip,1]-T_gar_comp[ymd][ip,2]
                               

keys_gar=T_gar_comp.keys()

for k in keys_gar:
    ymd=k
    lTgar=len(T_gar_comp[ymd])
    lTgar_col=len(T_gar_comp[ymd][0])
    
    os.chdir("txtfiles")

    ofile_gar_comp=open('euskalmet-era5_TP_GAUTEGIZ_ARTEAGA_'+ymd+'.txt','w')
    ofiles.append(ofile_gar_comp)

    for ip in range(lTgar):
        for ipcol in range(lTgar_col):
            ofile_gar_comp.write("%8.2f" %T_gar_comp[ymd][ip,ipcol])
            if ipcol==lTgar_col-1:
                ofile_gar_comp.write("\n")
                
    os.chdir("..")

#
#Aeropuerto de Madrid
#####################

cv_fechas=[]

ifiles_T_cv=glob.glob("../aemet-sondeos/*201403*CORR.txt")
ifiles_T_cv.sort()

for f_T_cv in ifiles_T_cv:
    filename_noext=os.path.splitext(f_T_cv)[0]

    fecha=filename_noext[17:25]
  
    cv_fechas.append(fecha)

lcvf=len(cv_fechas)

cv_era5_fechas=[]

ifiles_T_era5_cv = glob.glob("../TP_ERA5/txtfiles/*TP*MADRID*2014-03*.txt")
ifiles_T_era5_cv.sort()

for f_T_era5_cv in ifiles_T_era5_cv:
    filename_noext=os.path.splitext(f_T_era5_cv)[0]

    agno=filename_noext[40:44]
    mes=filename_noext[45:47]
    dia=filename_noext[48:50]
    fecha=agno+mes+dia

    cv_era5_fechas.append(fecha)

lcvef=len(cv_era5_fechas)

T_cv_comp={}

for t in range(lcvf):
    for te in range(lcvef):
        if cv_fechas[t] == cv_era5_fechas[te]:

            if_T_era5_cv=ifiles_T_era5_cv[te]
            if_T_cv=ifiles_T_cv[t]

            T_cv_era5=lectura_datos(if_T_era5_cv)
            T_cv=lectura_datos(if_T_cv)

            if isinstance(T_cv,np.float64)==False or isinstance(T_cv_era5,np.float64)==False:
                T_cv=np.array(T_cv,dtype='float64')
                T_cv_era5=np.array(T_cv_era5,dtype='float64')

            lTcv=len(T_cv)
            lTecv=len(T_cv_era5)
 
            ymd=cv_fechas[t]
            T_cv_comp[ymd]=np.zeros((lTcv,4),'d')


            filename_cv_noext=os.path.splitext(ifiles_T_cv[t])[0]
            hora_cv=float(filename_cv_noext[26:30])

            hora_cv_era5=aproximar(horas_era5,hora_cv)
            ihora_cv_era5=np.where(horas_era5==hora_cv_era5)[0][0]
     
            for ip in range(lTcv):
                paprox=aproximar(T_cv_era5[:,0],T_cv[ip,0])
                ipaprox=np.where(T_cv_era5[:,0]==paprox)[0][0]
                

            #Preferencia de presiones: aemet, por ser datos observados
            #Puede que cada presion que se seleccione de la tabla de datos de Euskalmet,
            #haya dos igualmente proximas de ERA5, 
            #por lo que se podrian repetir los datos de esta ultima.

                T_cv_comp[ymd][ip,0]=T_cv[ip,0]
                T_cv_comp[ymd][ip,1]=T_cv[ip,2]
                T_cv_comp[ymd][ip,2]=T_cv_era5[ipaprox,ihora_cv_era5+1]
                T_cv_comp[ymd][ip,3]=T_cv_comp[ymd][ip,1]-T_cv_comp[ymd][ip,2]


keys_cv=T_cv_comp.keys()

for k in keys_cv:
    ymd=k

    lTcv=len(T_cv_comp[ymd])
    lTcv_col=len(T_cv_comp[ymd][0])
    
    os.chdir("txtfiles")

    ofile_cv_comp=open("aemet-era5_TP_MADRID_AERO_"+ymd+".txt",'w')
    ofiles.append(ofile_cv_comp)

    for ip in range(lTcv):
        for ipcol in range(lTcv_col):
            ofile_cv_comp.write("%8.2f" %T_cv_comp[ymd][ip,ipcol])
            if ipcol==lTcv_col-1:
                ofile_cv_comp.write("\n")

    os.chdir("..")

close_files(ofiles)
