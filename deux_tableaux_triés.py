import sys
#Fonctions
def creation_tableaux(total_arg):
    global t1 
    global t2  
    for x in (range(len(total_arg))):
        if total_arg[x] == "fusion":
            t2 = total_arg[x+1:]
            break
        else:
            t1.append(total_arg[x])
    return t1,t2

def sorted_fusion(tableaux1,tableaux2):
    new_array = []
    for x in tableaux1:
        new_array.append(x)
    for y in tableaux2:
        new_array.append(y)
    for x in (range(len(new_array))):
        for y in range(len(new_array)):
            if new_array[x] < new_array[y]:
                new_array[x],new_array[y]= new_array[y],new_array[x]
    return new_array
def gestion():
    if not "fusion" in total_arg:
        return True
    if len(arguments) < 4:
        return True
    return False
#Variable
arguments = sys.argv
total_arg = arguments[1:]
t1 = []
t2 = []
#Affichage
if gestion() == False:
    creation_tableaux(total_arg)
    print(sorted_fusion(t1,t2))
else:
    print("Error")
