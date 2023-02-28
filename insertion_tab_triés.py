import sys
#Fonction
def sorted_insert(tableaux,new_elements):
    tableaux.append(new_elements)
    for x in range(len(tableaux)):
        for y in range(len(tableaux)):
            if tableaux[x] < tableaux[y]:
                tableaux[y],tableaux[x] = tableaux[x],tableaux[y]
    return tableaux

def erreurs():
    for x in tab:
        if not x.isnumeric():
            return True
    for x in new_elements:
        if not x.isnumeric():
            return True
    if len(arguments) < 4:
        return True
    return False

#Variables
arguments = sys.argv
tab = arguments[1:-1]
new_elements = arguments[-1]
#Affichage
if erreurs() == False:  
    print(sorted_insert(tab,new_elements))
else:
    print("Erreur veuillez rentrer 3 arguments contenant que des chiffres")