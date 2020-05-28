def bisiesto_indexes(yeari,yearf):
    bis=0
    ys=range(yeari,yearf)

    for i in ys:
        if (i/4. - int(i/4.))==0:
            bis+=1

    res=len(ys)*365+bis
    return res,bis

yeari=1979
yearf=2020

result,bis=bisiesto_indexes(yeari,yearf)

print("En",abs(yeari-yearf+1),"años",bis,"años bisiestos;",result,"indices")
