#Créez un programme qui découpe une chaîne de caractères en tableau en fonction du séparateur donné en 2e argument.
import sys
arguments = sys.argv
#Fonctions
def split_fonction(arg1,arg2):
    tab= []
    mot=""
    mot_split = arg2
    for x in arg1:
        if mot == mot_split: 
            tab.append("\n")
            mot=""
        if x in [" ","\t","\n"]:
            if mot != "":
                tab.append(mot)
                mot=""
        else:
            mot +=x #rajout des lettres dans un variable mot 
    if mot == mot_split:
        tab.append("\n")
        mot=""
    if mot !="":
        tab.append(mot)
    return tab

if len(arguments) != 3:
    print("Erreur veuillez rentrer deux arguments")
    exit()

arguments_1 = arguments[1]
arguments_2 = arguments[2]
for x in split_fonction(arguments_1,arguments_2):
    print(x,end=" ")
print()
