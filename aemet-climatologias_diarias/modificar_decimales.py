import glob
import os

files=glob.glob("aemet*.txt")

for f in files:
    ifile=open(f,"r")
    path_noext=os.path.splitext(f)[0]
    file_noext=os.path.basename(path_noext)

    ofile=open(file_noext+"_corrected.txt","w")
    for line in ifile:
        if "," in line:
            
            l=list(line)
            ll=len(l)
            index=[]
            for i in range(ll):
                if l[i]==",":
                    l[i]="."
            delim=""
            line1=delim.join(l)
            ofile.write(line1)
        else:
            ofile.write(line)

    ofile.close()
    ifile.close()
