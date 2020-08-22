def bisiesto_indexes(yeari,yearf):
    bis=0
    ys=list(range(yeari,yearf))

    for i in ys:
        if (i/4. - int(i/4.))==0:
            bis+=1

    res=len(ys)*365+bis
    return ys,bis,res

years,bisiestos,ibis=bisiesto_indexes(1986,2017)

print((years[0],"-",years[-1],":",len(years)-1,"años,",bisiestos,"bisiestos;",ibis,"indices"))
