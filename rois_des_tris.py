#Créez un programme qui trie une liste de nombres. Votre programme devra implémenter l’algorithme du tri rapide (QuickSort).
import sys
#fonction
def quick_sort(tableaux):
    longueur = len(tableaux)
    if longueur <= 1:
        return tableaux
    else:
        pivot = tableaux.pop()
    chiffre_haut = [] #Creation de 2 tableaux les elements de notre liste seront triés grace au pivot
    chiffre_bas = []
    for x in tableaux:
        if x > pivot:
            chiffre_haut.append(x)
        else:
            chiffre_bas.append(x)
    return quick_sort(chiffre_bas) + [pivot] + quick_sort(chiffre_haut)

def erreurs_arg():
    if len(arguments) < 3:
        return True
    for x in tab:
        if not x.isnumeric():
            return True
    return False

#Variable
arguments = sys.argv
tab = arguments[1:]
#Affichage
if erreurs_arg() == False:
    print(quick_sort(tab))
else:
    print("Veuillez rentrer une liste de nombre")


