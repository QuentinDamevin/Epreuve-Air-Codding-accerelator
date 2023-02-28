#Creez un programme qui affiche une chaine de caracteres en évitant les caracteres identiques adjacents 
import sys
def un_seul(arg):
    resultat = ""
    lettre_suiv = ""
    for x in arg:
        if x != lettre_suiv:
            resultat += x
            lettre_suiv = x
    return resultat

def erreurs():
    if len(arguments) != 2:
        return True
    return False

arguments = sys.argv
arguments_1 = arguments[1]

if erreurs() == False:
    print(un_seul(arguments_1))
else:
    print("Erreur vous devez rentrer 1 seul arguments")