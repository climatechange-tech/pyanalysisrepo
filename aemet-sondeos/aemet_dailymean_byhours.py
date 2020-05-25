import numpy as np
import pandas as pd
import os
import glob

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
    

txtfiles=glob.glob("201412*CORR.txt")
txtfiles.sort()

datedict={}

keyarr=[]
for txtf in txtfiles:
    ymdkey=txtf[:8]
    datedict[ymdkey]=lectura_datos(txtf)

keys=datedict.keys
    
for k in keys:
    keyarr.append(k)

