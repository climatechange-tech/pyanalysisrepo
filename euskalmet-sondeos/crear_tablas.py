import os
import numpy as np
import glob

txt_files=glob.glob("*Z.txt")
txt_files.sort()

for txtf in txt_files:
    i=0

    ifile=open(txtf,encoding="latin1")
    filename=os.path.splitext(txtf)
    filename_noext=filename[0]
    filename_ext=filename[1]
    filename_corr=filename_noext+"_dataonly"+filename_ext

    ofile=open(filename_corr,'w')

    first_line=ifile.readline()
    date=first_line[55:65]
    ofile.write("# "+date+2*"\n")

    for line in ifile:
        i+=1
        if i>=8 and"---------" in line:
            break 
        if i>=8:
            ofile.write(line)


    ifile.close()
