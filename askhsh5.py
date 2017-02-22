#sunarthsh pou briskei to athroisma twn psufiwn enos arithmou
def athroisma_psufiwn(arithmos):
    summ=0;
    while arithmos:
        arithmos,remainder=divmod(arithmos,10);
        summ+=remainder;
    return(summ)
#sunarthsh pou elegxei an o arithmos einai arithmos harshad
def elegxos(arithmos):
    summ=athroisma_psufiwn(arithmos);
    if arithmos%summ==0:
        endeixh=1;
    else:
        endeixh=0;
    return(endeixh)
#sunarthsh pou vriskei to ginomeno twn psufiwn enos arithmou
def ginomeno_psufiwn(arithmos):
    ginomeno=1;
    while arithmos:
        arithmos,remainder=divmod(arithmos,10);
        ginomeno*=remainder;
    return(ginomeno)
# kuriws programma to opoio perna tous arithmous apo to 1 mexri to 1000 gia na vrei tous arithmous harshad
for number in range(1,1000):
    arithmos_harshad=elegxos(number);
    if  arithmos_harshad:
        ginomeno=ginomeno_psufiwn(number);
#elegxos gia an mhn kanw diairesh me to mhden
        if ginomeno!=0:
            if number%ginomeno==0:
               print"To ginomeno twn psufiwn tou %d ton  diairei \n" % number;
#telos programmatos
