#Créez un programme qui affiche le contenu d’un fichier donné en argument.
import sys
arguments = sys.argv
#Fonctions
def ouvrir_lire_fichier(nomfichier):
    try:
        with open(nomfichier,"r+") as file:
            print(file.readlines())
            file.close()
    except:
        print("erreur")

def erreurs():
    if len(arguments) < 2:
        return True
    return False

#Affichage
if erreurs() == False:
    nom_fichier = arguments[1]
    ouvrir_lire_fichier(nom_fichier)
else:
    print("erreur")


