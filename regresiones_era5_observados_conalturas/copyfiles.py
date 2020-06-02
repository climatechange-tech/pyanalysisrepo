import os
import glob

pyfiles=glob.glob("*sesgocorr.py")

for f in pyfiles:
    filename_noext=os.path.splitext(f)[0]
    newfile=filename_noext+"_zg0_era5.py"

    ifile=open(f)
    ofile=open(newfile,'w')
    for line in ifile:
        ofile.write(line)
    ofile.close
    ifile.close

gnufiles=glob.glob("*sesgocorr.gnu")
for f in gnufiles:
    filename_noext=os.path.splitext(f)[0]
    newfile=filename_noext+"_zg0_era5.gnu"

    ifile=open(f)
    ofile=open(newfile,'w')
    for line in ifile:
        ofile.write(line)
    ofile.close
    ifile.close

