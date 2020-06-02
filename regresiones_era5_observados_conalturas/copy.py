import os
import glob

copyfiles=glob.glob("*sesgocorr.py")

for f in copyfiles:
    filename_noext=os.path.splitext(f)[0]
    newfile=filename_noext+"_zg0_era5.py"

    ifile=open(f)
    ofile=open(newfile,'w')
    for line in ifile:
        ofile.write(line)
    ofile.close
    ifile.close
