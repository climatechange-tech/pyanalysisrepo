import numpy as np
import pandas as pd


a=[]
b=[]

for iyear in range(1997,1999):
    for imon in range(1,13):
        ym="%4.4d-%2.2d" %(iyear,imon)
        a.append(ym)

a=np.array(a,dtype='O')
a=np.delete(a,[1,3,4,7,11,16])

for iyear in range(1986,2017):
    for imon in range(1,13):
        ym="%4.4d-%2.2d" %(iyear,imon)
        b.append(ym)

varstr="a b c d e f g h i j"
varlist=varstr.split()

bdf=pd.DataFrame(columns=varlist)
bdf.a=b

ifirst=bdf[a[0]==bdf.a].index[0]
bdf=bdf.loc[ifirst:]

for i in range(ifirst,len(b)):
    if bdf.a[i] in a:
        print((bdf.a[i],"is in aemet array"))
    else:
        print((bdf.a[i],"is NOT in aemet array"))
        bdf.loc[i]=np.nan

#bdf.index=RangeIndex(start=132, stop=372, step=1) !!!!
