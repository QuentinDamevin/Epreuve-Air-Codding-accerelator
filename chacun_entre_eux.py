import sys
#FONCTIONS
def operation_soustraction(tab,operateur):
    new_tab =[]
    nombre_acalculer = int(operateur[1:]) #on enlève le l'operateur "-" ou "+" 
    for x in range(len(tab)):
        if "-" in operateur:
            new_tab.append(int(tab[x])-nombre_acalculer)
        if "+" in operateur:
            new_tab.append(int(tab[x])+nombre_acalculer)
    return new_tab
def erreurs():
    if len(arguments) < 3:
        return True
    if not "-" or not "+" in derniers_elements:
        return True
    if not derniers_elements[1:].isnumeric():
        return True
    for x in tab:
        if not x.isnumeric():
            return True
    return False
#VARIABLE
arguments = sys.argv
tab = arguments[1:-1]
derniers_elements = arguments[-1]
#AFFICHAGE
if erreurs() == False:
    print(operation_soustraction(tab,derniers_elements))
else:
    print("Veuillez rentrer des nombres suivi d'une soustraction ou d'une addition")