import sys
#Fonctions
def controle(tableaux , string):
    new_tab = []
    for x in tableaux:
        x.lower()
        if not string.lower() in x:
            new_tab.append(x)
    return new_tab

def erreurs():
    if len(arguments) < 3:
        return True
    for x in tab:
        if x.isnumeric():
            return True
    return False
    
#Variable
arguments = sys.argv
tab = arguments[1:-1]
string = arguments[-1]
#Affichage
if erreurs() == False:
    print(controle(tab,string))
else:
    print("error")