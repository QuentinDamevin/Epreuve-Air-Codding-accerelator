#Créez un programme qui découpe une chaîne de caractères en tableau (séparateurs : espaces, tabulations, retours à la ligne).
import sys
arguments = sys.argv
#fonction
def gestion_erreurs():
    for x in arguments_1:
        if x.isnumeric():
            return False
    return True

def fonction_split(string_coupé):
    tab = []
    mot = ""
    for c in string_coupé:
        if c in [" ","\t", "\n"]:
            if mot != "":
                tab.append(mot)
                mot=""
        else:
            mot+=c
    if mot != "":
        tab.append(mot)
    return tab
#affichage
if gestion_erreurs == True and len(arguments) == 2:
    arguments_1 = arguments[1]
    for x in fonction_split(arguments_1):
        print(x)
else:
    print("Veuillez rentrer une chaine de caracteres contenant que des lettres")