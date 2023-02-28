import sys
def fonction_concat(tableaux,separateur):
    string = str()
    for x in tableaux:
        string = string + x + separateur
    return string
def erreurs_arg():
    if len(tab) < 2:
        return True
    return False
#Variable
arguments = sys.argv
tab = arguments[1:-1]
separateur = arguments[-1]
#Affichage
if erreurs_arg() == False:
    print(fonction_concat(tab,separateur))
else:
    print("Erreur vous devez rentrer deux arguments suivi d'un separateur de votre choix")
