#synarthsh gia na metraw tis parentheseis
def metrhma(parenthesh,akolouthia):
    return akolouthia.count(parenthesh)
par_dexia="(";
par_aristera=")";
parentheseis=raw_input("Dwse thn akolouthia twn parenthesewn: ")
#brisko th thesh ths teleytaias parentheshs
lastchar=len(parentheseis);
lastchar=parentheseis[lastchar-1];
#elegxw oti h akolouthia jekinaei me ( kai teleiwnei me )
if parentheseis[0]=="(" and lastchar==")":
    #stelnw sth sunarthsh thn akolouthia gia na metrhsei tis parentheseis,mia fora gia tiw dejia kai mai gia tiw aristeres
    arithmos_par_dexia=metrhma(par_dexia,parentheseis);
    arithmos_par_aristera=metrhma(par_aristera,parentheseis);
    #elegxw oti oi dejia parentheseis eina ises me tis aristera.Am eimnai ises mas kanoun, alliws den mas kanoun
    if arithmos_par_dexia==arithmos_par_aristera:
        print"TRUE";
    else:
        print"FALSE";
else:
    print"FALSE";
