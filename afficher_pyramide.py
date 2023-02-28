#Afficher un escalier constitué d'un caractere et d'un nombre d'étages donné en parametre.
import sys
arguments = sys.argv
#Fonction
def afficher_pyramide(symbole,etage):
    for i in range(etage+1):
        for y in range(etage-i):
            print(" ",end="")
        for x in range(1,2*i):
            print(symbole,end="")
        print()

def erreurs_arg():
    if len(arguments) != 3:
        return True
    if not arguments[2].isnumeric():
        return True
    return False


#Affichage
if erreurs_arg() == False:
    symbole = arguments[1]
    nb_etage = int(arguments[2])
    pyramide = afficher_pyramide(symbole,nb_etage)
else:
    print("Vous devez rentrer un symbole et un nombre d'étages pour generer la pyramide")
   
