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
        lista.append(hilera[i])
    return lista



txt_files=glob.glob("*.csv")
txt_files.sort()

varstr="Pressure,O3PartialPressure,Temperature,WindSpeed,WindDirection,LevelCode,Duration,GPHeight,RelativeHumidity,SampleTemperature"
varlist=varstr.split(",")

for txtf in txt_files:
    i=0

    ifile=open(txtf,encoding="latin1")
    filename=os.path.splitext(txtf)
    filename_noext=filename[0]
    #filename_ext=filename[1]

    for line in ifile:
        i+=1
        if i==24:
            date_line=line
            date=date_line[10:20]
            time=date_line[21:26]

    filename_corr=filename_noext[:8]+"_"+time[:2]+time[3:5]+"_MADRID_corrected.txt"

    ofile=open(filename_corr,'w')
    ofile.write("# "+date+" "+time+2*"\n")

    ifile=open(txtf,encoding="latin1")

    df=pd.DataFrame(columns=varlist)

    i=0
    for line in ifile:
        i+=1
        if i>=54:
            lline=line.split(",")
            lline[-1]=lline[-1][:-1]
            if len(lline)==10:
                for i in range(len(lline)):
                    if lline[i]=="":
                        lline[i]=str(np.nan)

                lline_arr=np.array(lline)
                lline_arr=lline_arr[np.newaxis,:]
    
                next_df=pd.DataFrame(lline_arr,columns=varlist)
                df=df.append(next_df, ignore_index=True)          

            elif len(lline)==9:
                for i in range(len(lline)):
                    if lline[i]=="":
                        lline[i]=str(np.nan)

                lline.append(np.nan)

                lline_arr=np.array(lline)
                lline_arr=lline_arr[np.newaxis,:]
    
                next_df=pd.DataFrame(lline_arr,columns=varlist)
                df=df.append(next_df, ignore_index=True)          

            elif len(lline)==8:
                for i in range(len(lline)):
                    if lline[i]=="":
                        lline[i]=str(np.nan)

                lline.append(str(np.nan))
                lline.append(str(np.nan))
         
                lline_arr=np.array(lline)
                lline_arr=lline_arr[np.newaxis,:]
    
                next_df=pd.DataFrame(lline_arr,columns=varlist)
                df=df.append(next_df, ignore_index=True)          


    for var in varlist:
        ofile.write("# %s "%var)
    ofile.write("\n")

    for irow in range(len(df)):
        for var in varlist:
            ofile.write("%7s" %df[var][irow])
            if var==varlist[-1]:
                ofile.write("\n")

    ifile.close()    
    ofile.close()
