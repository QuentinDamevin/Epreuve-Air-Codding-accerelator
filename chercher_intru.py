#creez un programme qui retourne la valeur d'une liste qui n'a pas de paire.
import sys
def chercher_intru(tableaux):
    intru = []
    for x in tableaux:
        if tab.count(x) % 2 != 0:
            if not x in intru:
                intru.append(x)
    return intru
def erreurs_arg():
    if len(arguments) < 3:
        return True
    return False
         
#variables
arguments = sys.argv 
tab = arguments[1:]

#affichage 
if erreurs_arg() ==  False:
    print(chercher_intru(tab))
else:
    print("Vous devez rentrer 2 arguments minimum")


