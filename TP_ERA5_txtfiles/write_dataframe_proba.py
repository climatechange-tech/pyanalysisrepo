import pandas as pd
import numpy as np

a=np.random.normal(1,3,size=(5,5))

varlist=["level"]
for i in range(len(a)-1):
    time="%2.2d:00"%i
    varlist.append(time)

b=pd.DataFrame(a,columns=varlist)
b=b.round(2)

ofile=open("write_dataframe_proba.txt",'w')

for irow in range(len(a)):
    for var in varlist:
        ofile.write("%5.2f " %b[var][irow])
        if var==varlist[-1]:
            ofile.write("\n")

ofile.write("\n")

for irow in range(len(a)):
    for var in varlist:
        ofile.write("%5.2f\n" %b[var][irow])
