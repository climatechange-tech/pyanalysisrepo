#Codificacion utf-8 y utf-16 invalidos --> usar latin1

def close_files(list_files):
    lf=len(list_files)
    for i in range(lf):
        list_files[i]

ofiles=[]


import pandas as pd
import json
import numpy as np
from netCDF4 import Dataset
import csv



#BILBAO AEROPUERTO######################################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet

with open('bizkaia-bilbao_aeropuerto-1986_1989.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('bizkaia-bilbao_aeropuerto-1990_1992.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('bizkaia-bilbao_aeropuerto-1993_1997.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('bizkaia-bilbao_aeropuerto-1998_2002.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('bizkaia-bilbao_aeropuerto-2003_2007.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('bizkaia-bilbao_aeropuerto-2008_2012-12-30.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('bizkaia-bilbao_aeropuerto-2012-12-31_2016.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

#
#Guardar los datos_y_calculos en formato tabular y escribir ficheros de datos
#

ofile_bilbo=open('aemet_BILBAO_AERO.txt','w')
ofiles.append(ofile_bilbo)

for irow in range(len(df)):
    for ivar in range(len(df.loc[0])):
        ofile_bilbo.write("%s " %df.loc[irow][ivar])
        if ivar == len(df.loc[0])-1:
            ofile_bilbo.write("\n")


#GUEÑES######################################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet
with open('bizkaia-guennes-1997-04-01_1997-12-31.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('bizkaia-guennes-1998_2002.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('bizkaia-guennes-2003_2007.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('bizkaia-guennes-2008_2012-12-30.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('bizkaia-guennes-2012-12-31_2016.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

ofile_gue=open("aemet_GUENES.txt",'w')
ofiles.append(ofile_gue)

for irow in range(len(df)):
    for ivar in range(len(df.loc[0])):
        ofile_gue.write("%s " %df.loc[irow][ivar])
        if ivar == len(df.loc[0])-1:
            ofile_gue.write("\n")



#LEKEITIO######################################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet
with open('bizkaia-lekeitio-1997-04-01_1997-12-31.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('bizkaia-lekeitio-1998-01-03_2002.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('bizkaia-lekeitio-2003_2007.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('bizkaia-lekeitio-2008_2012-12-30.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('bizkaia-lekeitio-2012-12-31_2016.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

ofile_lek=open("aemet_LEKEITIO.txt",'w')
ofiles.append(ofile_lek)

for irow in range(len(df)):
    for ivar in range(len(df.loc[0])):
        ofile_lek.write("%s " %df.loc[irow][ivar])
        if ivar == len(df.loc[0])-1:
            ofile_lek.write("\n")

#AEROPUERTO DE DONOSTIA#########################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet

with open('gipuzkoa-ss-aeropuerto-2011_2015-12-30.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('gipuzkoa-ss-aeropuerto-2015-12-30_2016.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

#
#Guardar los datos_y_calculos en formato tabular y escribir ficheros de datos
#

ofile_ss_aero=open('aemet_DONOSTIA_AERO.txt','w')
ofiles.append(ofile_ss_aero)

for irow in range(len(df)):
    for ivar in range(len(df.loc[0])):
        ofile_ss_aero.write("%s " %df.loc[irow][ivar])
        if ivar == len(df.loc[0])-1:
            ofile_ss_aero.write("\n")


#IGELDO######################################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet
with open('gipuzkoa-igeldo-1986_1989.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('gipuzkoa-igeldo-1990_1992.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('gipuzkoa-igeldo-1993_1997.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('gipuzkoa-igeldo-1998_2002.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('gipuzkoa-igeldo-2003_2007.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('gipuzkoa-igeldo-2008_2012-12-30.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('gipuzkoa-igeldo-2012-12-31_2016.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)


ofile_igeldo=open("aemet_IGELDO.txt",'w')
ofiles.append(ofile_igeldo)

for irow in range(len(df)):
    for ivar in range(len(df.loc[0])):
        ofile_igeldo.write("%s " %df.loc[irow][ivar])
        if ivar == len(df.loc[0])-1:
            ofile_igeldo.write("\n")


#HONDARRIBIA-MALKARROA######################################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet
with open('gipuzkoa-hondarribia-malkarroa-1986_1989.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('gipuzkoa-hondarribia-malkarroa-1990_1992.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('gipuzkoa-hondarribia-malkarroa-1993_1997.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('gipuzkoa-hondarribia-malkarroa-1998_2002.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('gipuzkoa-hondarribia-malkarroa-2003_2007.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('gipuzkoa-hondarribia-malkarroa-2008_2012-12-30.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('gipuzkoa-hondarribia-malkarroa-2012-12-31_2016.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

ofile_hond=open("aemet_HONDARRIBIA-MALKARROA.txt",'w')
ofiles.append(ofile_hond)

for irow in range(len(df)):
    for ivar in range(len(df.loc[0])):
        ofile_hond.write("%s " %df.loc[irow][ivar])
        if ivar == len(df.loc[0])-1:
            ofile_hond.write("\n")


#ELGOIBAR######################################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet
with open('gipuzkoa-elgoibar-1997-04-01_1997-12-31.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('gipuzkoa-elgoibar-1998_2002.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('gipuzkoa-elgoibar-2003_2007.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('gipuzkoa-elgoibar-2008_2012-12-30.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('gipuzkoa-elgoibar-2012-12-31_2016.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

ofile_elg=open("aemet_ELGOIBAR.txt",'w')
ofiles.append(ofile_elg)

for irow in range(len(df)):
    for ivar in range(len(df.loc[0])):
        ofile_elg.write("%s " %df.loc[irow][ivar])
        if ivar == len(df.loc[0])-1:
            ofile_elg.write("\n")


#ZUMARRAGA######################################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet
with open('gipuzkoa-zumarraga-2007-12-19_2007-12-31.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('gipuzkoa-zumarraga-2008_2012-12-30.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('gipuzkoa-zumarraga-2012-12-31_2016.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

ofile_zumar=open("aemet_ZUMARRAGA.txt",'w')
ofiles.append(ofile_zumar)

for irow in range(len(df)):
    for ivar in range(len(df.loc[0])):
        ofile_zumar.write("%s " %df.loc[irow][ivar])
        if ivar == len(df.loc[0])-1:
            ofile_zumar.write("\n")


#ZUMAIA######################################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet
with open('gipuzkoa-zumaia-1997-04-01_1997-12-31.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('gipuzkoa-zumaia-1998_2002.json', 'r', encoding='latin1') as json_file:

    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('gipuzkoa-zumaia-2003_2007.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('gipuzkoa-zumaia-2008_2012-12-30.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('gipuzkoa-zumaia-2012-12-31_2016.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

ofile_zumaia=open("aemet_ZUMAIA.txt",'w')
ofiles.append(ofile_zumaia)

for irow in range(len(df)):
    for ivar in range(len(df.loc[0])):
        ofile_zumaia.write("%s " %df.loc[irow][ivar])
        if ivar == len(df.loc[0])-1:
            ofile_zumaia.write("\n")



#FORONDA-TXOKIZA######################################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet
with open('araba-foronda-txokiza-1986_1989.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('araba-foronda-txokiza-1990_1992.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('araba-foronda-txokiza-1993_1997.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('araba-foronda-txokiza-1998_2002.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('araba-foronda-txokiza-2003_2007.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('araba-foronda-txokiza-2008_2012-12-30.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('araba-foronda-txokiza-2012-12-31_2016.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

ofile_fortx=open("aemet_FORONDA.txt",'w')
ofiles.append(ofile_fortx)

for irow in range(len(df)):
    for ivar in range(len(df.loc[0])):
        ofile_fortx.write("%s " %df.loc[irow][ivar])
        if ivar == len(df.loc[0])-1:
            ofile_fortx.write("\n")


#PAMPLONA AEROPUERTO######################################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet
with open('nafarroa-pamplona-aeropuerto-1986_1989.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('nafarroa-pamplona-aeropuerto-1990_1992.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('nafarroa-pamplona-aeropuerto-1993_1997.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('nafarroa-pamplona-aeropuerto-1998_2002.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('nafarroa-pamplona-aeropuerto-2003_2007.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('nafarroa-pamplona-aeropuerto-2008_2012-12-30.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('nafarroa-pamplona-aeropuerto-2012-12-31_2016.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

ofile_pamplona=open("aemet_PAMPLONA.txt",'w')
ofiles.append(ofile_pamplona)

for irow in range(len(df)):
    for ivar in range(len(df.loc[0])):
        ofile_pamplona.write("%s " %df.loc[irow][ivar])
        if ivar == len(df.loc[0])-1:
            ofile_pamplona.write("\n")


#NAFARROA-CADREITA######################################################################################
###LECTURA DE DATOS Y CREACIóN DE DATAFRAME###
#Leer json con las observaciones de Aemet
with open('nafarroa-cadreita-1991_1992.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
#Creación del dataframe con los datos_y_calculos
df = pd.DataFrame(data)

with open('nafarroa-cadreita-1993_1997.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('nafarroa-cadreita-1998_2002.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('nafarroa-cadreita-2003_2007.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('nafarroa-cadreita-2008_2012-12-30.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

with open('nafarroa-cadreita-2012-12-31_2016.json', 'r', encoding='latin1') as json_file:
    data = json.load(json_file)
next_df = pd.DataFrame(data)
df = pd.concat([df, next_df],ignore_index=True)

ofile_cadreita=open("aemet_CADREITA.txt",'w')
ofiles.append(ofile_cadreita)

for irow in range(len(df)):
    for ivar in range(len(df.loc[0])):
        ofile_cadreita.write("%s " %df.loc[irow][ivar])
        if ivar == len(df.loc[0])-1:
            ofile_cadreita.write("\n")


close_files(ofiles)
