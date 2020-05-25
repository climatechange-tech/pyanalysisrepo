#Codificacion utf-8 y utf-16 invalidos --> usar latin1

#BASES DE DATOS CON SINTAXIS PUNTUAL INCORRECTA, EXCEPTO AEROPUERTO DE BILBO Y CUATRO VIENTOS (nere errua)

import pandas as pd
import json
import numpy as np
from netCDF4 import Dataset
import csv


#MADRID AEROPUERTO######################################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet
with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-aeropuerto-1993_1997.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-aeropuerto-1998_2002.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-aeropuerto-2003_2007.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-aeropuerto-2008_2012-12-30.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-aeropuerto-2012-12-31_2016.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

#Actualizar indices para que nos e repitan, ya que se conservan al unir los dataframe
df.index = range(df.shape[0])


#RETIRO#########################################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet
with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-retiro-1993_1997.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-retiro-1998_2002.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-retiro-2003_2007.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-retiro-2008_2012-12-30.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-retiro-2012-12-31_2016.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

#Actualizar indices para que nos e repitan, ya que se conservan al unir los dataframe
df.index = range(df.shape[0])


#CIUDAD UNIVERSITARIA#########################################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet
with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-ciudad_universitaria-1997.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-ciudad_universitaria-1998_2002.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-ciudad_universitaria-2003_2007-11-29.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-ciudad_universitaria-2008-01-08_2012-12-30.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-ciudad_universitaria-2012-12-31_2016.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

#Actualizar indices para que nos e repitan, ya que se conservan al unir los dataframe
df.index = range(df.shape[0])

#CUATRO VIENTOS#########################################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-cuatro_vientos-1986_1989.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-cuatro_vientos-1990_1992.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-cuatro_vientos-1993_1997.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-cuatro_vientos-1998_2002.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-cuatro_vientos-2003_2007.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-cuatro_vientos-2008_2012-12-30.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/madrid-cuatro_vientos-2012-12-31_2016.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

#Actualizar indices para que nos e repitan, ya que se conservan al unir los dataframe
df.index = range(df.shape[0])

#
#Guardar los datos_y_calculos en formato tabular y escribir ficheros de datos
#

df_CV_array=np.array(df)
ofile_cv=open('aemet_CUATRO_VIENTOS.txt','w')

ldf=len(df_CV_array)
ldfcol=len(df_CV_array[0])
for i in range(ldf):
    for j in range(ldfcol):
        ofile_cv.write("%s " %str(df_CV_array[i,j]))
        if j==ldfcol-1:
            ofile_cv.write("\n")

ofile_cv.close()


#BILBAO AEROPUERTO######################################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/bizkaia-bilbao_aeropuerto-1986_1989.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/bizkaia-bilbao_aeropuerto-1990_1992.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/bizkaia-bilbao_aeropuerto-1993_1997.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/bizkaia-bilbao_aeropuerto-1998_2002.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/bizkaia-bilbao_aeropuerto-2003_2007.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/bizkaia-bilbao_aeropuerto-2008_2012-12-30.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/bizkaia-bilbao_aeropuerto-2012-12-31_2016.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

#
#Guardar los datos_y_calculos en formato tabular y escribir ficheros de datos
#

df_ABILBO_array=np.array(df)
ofile_abilbo=open('aemet_BILBAO_AERO.txt','w')

ldf=len(df_ABILBO_array)
ldfcol=len(df_ABILBO_array[0])
for i in range(ldf):
    for j in range(ldfcol):
        ofile_abilbo.write("%s " %str(df_ABILBO_array[i,j]))
        if j==ldfcol-1:
            ofile_abilbo.write("\n")

ofile_abilbo.close()


#GÜEÑES######################################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet
with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/bizkaia-guennes-1997-04-01_1997-12-31.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/bizkaia-guennes-1998_2002.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/bizkaia-guennes-2003_2007.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/bizkaia-guennes-2008_2012-12-30.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/bizkaia-guennes-2012-12-31_2016.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])



#LEKEITIO######################################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet
with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/bizkaia-lekeitio-1997-04-01_1997-12-31.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/bizkaia-lekeitio-1998-01-03_2002.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/bizkaia-lekeitio-2003_2007.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/bizkaia-lekeitio-2008_2012-12-30.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

with open('/home/jonander/Documentos/16-Lana/Tecnalia/proyecto_PET/datos_y_calculos/aemet-climatologias_diarias/bizkaia-lekeitio-2012-12-31_2016.json', 'r', encoding='latin1') as json_file:  
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df])

