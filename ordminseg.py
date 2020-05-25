import random

def ordminseg(x):
    hours=int(x/3600)
    mins=int(int(x-3600*hours)/60)
    secs="%5.2f" %(x-(3600*hours+60*mins))

    return hours,mins,secs

x=1000*random.random()
hours,mins,secs=ordminseg(x)

print(x,hours,mins,secs)
