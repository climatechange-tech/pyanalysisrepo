import numpy as np

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

ifile="arteaga_20121111_1200Z_CORR.txt"

data=lectura_datos(ifile)

#
#Ultima fila de la matriz "data" igual a linea horizontal
#eliminarla con numpy
#

data=np.delete(data,-1)
