#Créez un programme qui décale tous les éléments d’un tableau vers la gauche. Le premier élément devient le dernier à chaque rotation.
import sys
#Fonction
def decalage(tableaux):
    premier_elements = tableaux[0]
    for x in range(len(tableaux)-1):
        tableaux[x] = tableaux[x+1]
    tableaux[-1] = premier_elements
    return tableaux
def erreurs():
    if len(arguments) < 3:
        return True
    return False
#Variables
arguments = sys.argv
t = arguments[1:]
#Affichage
if erreurs() ==False:  
    print(decalage(t))
else:
    print("Erreur veuillez entrer 2 arguments minimum")