#sunarthsh pou briski ton meso oro ths listas
def mesos(lista):
  sunolo=sum(lista);
  return sunolo/len(lista)
 #sunarthsh pou briskei th diakumansh thw listas
def diakumansh(lista,mo):
    meg_listas=len(lista);
    for i in range(0,meg_listas):
        lista[i]=(lista[i]-mo)**2;
    return sum(lista)/(meg_listas*1.0);
lista=list(input("dwse th lista pou epithumeis(ta stoixei na xwrizontai me komma): "));
mesos_oros=mesos(lista);
tupikh_apoklush=diakumansh(lista,mesos_oros);
#import math, gia na mporw an xrhshmopoihsw thn function sqrt
import math;
#tupikh apoklish einai h riza ths diakumanshs
tupikh_apoklush=math.sqrt(tupikh_apoklush);
print"H tupikh apoklish  twn stoixeiwn ths listas einai: %f " % tupikh_apoklush;
