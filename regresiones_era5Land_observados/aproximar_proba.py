import numpy as np
import pandas as pd

def aproximar(rangos,given_value):
    funcion_dif_abs = lambda lista_deciles: abs(lista_deciles-given_value)
    valor_aproximado=min(rangos,key=funcion_dif_abs)
    return valor_aproximado


M=(np.random.normal(1,3,size=10)).round(3)
x=(np.mean(np.random.normal(size=1))).round(3)

val_aprox=aproximar(M,x).round(8)
iaprox=np.where(M==val_aprox)[0][0]
print(("M=",M,"\n\nValor mas cercano de",x,"es",val_aprox, "con índice",iaprox))

Mdf=pd.DataFrame(M)

iaprox1=Mdf[Mdf==x].index[0]

print(("\nM_dataframe\n",Mdf,"\n\nValor mas cercano de",x,"usando Pandas es",val_aprox, "con índice",iaprox))
