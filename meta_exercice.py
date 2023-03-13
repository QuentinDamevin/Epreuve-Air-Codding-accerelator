#Créez un programme qui vérifie si les exercices de votre épreuve de l’air sont présents dans le répertoire et qu’ils fonctionnent (sauf celui là). Créez au moins un test pour chaque exercice.
import subprocess
import os.path
from subprocess import PIPE,Popen
import os
def test0():
    sortie_attendu = b"coucou\nla\nfamille\n"
    (sortie, erreurs) = subprocess.Popen(["python3",  "/Users/Quentin/Desktop/Epreuve-Air-Codding-accerelator/split.py","coucou la famille"], stdout=PIPE).communicate()
    if sortie == sortie_attendu:
        print("air00 (1/1) : success")
    else:
        print("air00 (0/1) : failure")
    return test0
        
def test1():
    sortie_attendu = b"coucou \n famille \n"
    (sortie, erreurs) = subprocess.Popen(["python3",  "/Users/Quentin/Desktop/Epreuve-Air-Codding-accerelator/split_fonction.py","coucou la famille", "la"], stdout=PIPE).communicate()
    if sortie == sortie_attendu:
        print("air01 (1/1) : success")
    else:
        print("air01 (0/1) : failure")
    return test1

def test2():
    sortie_attendu = b"coucou,la,famille,\n"
    (sortie, erreurs) = subprocess.Popen(["python3","/Users/Quentin/Desktop/Epreuve-Air-Codding-accerelator/concat.py","coucou","la","famille",","], stdout=PIPE).communicate()
    if sortie == sortie_attendu:
        print("air02 (1/1) : success")
    else:
        print("air02 (0/1) : failure")
    return test2
def test3():
    sortie_attendu = b"['5']\n"
    (sortie, erreurs) = subprocess.Popen(["python3","/Users/Quentin/Desktop/Epreuve-Air-Codding-accerelator/chercher_intru.py","1","2","3","4","5","4","3","2","1"], stdout=PIPE).communicate()
    if sortie == sortie_attendu:
        print("air03 (1/1) : success")
    else:
        print("air03 (0/1) : failure")
    return test3
def test4():
    sortie_attendu = b"coucou la famile ?\n"
    (sortie, erreurs) = subprocess.Popen(["python3","/Users/Quentin/Desktop/Epreuve-Air-Codding-accerelator/un_seul_fois.py","coucou  la   famille ??"], stdout=PIPE).communicate()
    if sortie == sortie_attendu:
        print("air04 (1/1) : success")
    else:
        print("air04 (0/1) : failure")
    return test4
def test5():
    sortie_attendu = b"[3, 4, 5, 6, 7]\n"
    (sortie, erreurs) = subprocess.Popen(["python3","/Users/Quentin/Desktop/Epreuve-Air-Codding-accerelator/chacun_entre_eux.py","1","2","3","4","5","+2"], stdout=PIPE).communicate()
    if sortie == sortie_attendu:
        print("air05 (1/1) : success")
    else:
        print("air05 (0/1) : failure")
    return test5
def test6():
    sortie_attendu = b"['Albert']\n"
    (sortie, erreurs) = subprocess.Popen(["python3","/Users/Quentin/Desktop/Epreuve-Air-Codding-accerelator/pass_sanitaire.py","Quentin","Albert","Benoit","n"], stdout=PIPE).communicate()
    if sortie == sortie_attendu:
        print("air06 (1/1) : success")
    else:
        print("air06 (0/1) : failure")
    return test6
def test7():
    sortie_attendu = b"['1', '2', '3', '4']\n"
    (sortie, erreurs) = subprocess.Popen(["python3","/Users/Quentin/Desktop/Epreuve-Air-Codding-accerelator/insertion_tab_triés.py","1","3","4","2"], stdout=PIPE).communicate()
    if sortie == sortie_attendu:
        print("air07 (1/1) : success")
    else:
        print("air07 (0/1) : failure")
    return test7
def test8():
    sortie_attendu = b"['10', '15', '20', '25', '30', '35']\n"
    (sortie, erreurs) = subprocess.Popen(["python3","/Users/Quentin/Desktop/Epreuve-Air-Codding-accerelator/deux_tableaux_triés.py","10","20","30","fusion","15","25","35"], stdout=PIPE).communicate()
    if sortie == sortie_attendu:
        print("air08 (1/1) : success")
    else:
        print("air08 (0/1) : failure")
    return test8
def test9():
    sortie_attendu = b"['damien', 'franc', 'maelyne', 'quentin']\n"
    (sortie, erreurs) = subprocess.Popen(["python3","/Users/Quentin/Desktop/Epreuve-Air-Codding-accerelator/rotation_gauche.py","quentin","damien","franc","maelyne"], stdout=PIPE).communicate()
    if sortie == sortie_attendu:
        print("air09 (1/1) : success")
    else:
        print("air09 (0/1) : failure")
    return test9
def test10():
    sortie_attendu = b'[\'print("coucou la famille")\']\n'
    (sortie, erreurs) = subprocess.Popen(["python3","/Users/Quentin/Desktop/Epreuve-Air-Codding-accerelator/afficher_contenue.py","/Users/Quentin/Desktop/test2.py"], stdout=PIPE).communicate()
    if sortie == sortie_attendu:
        print("air10 (1/1) : success")
    else:
        print("air10 (0/1) : failure")
    return test10
def test11():
    sortie_attendu = b'     \n    0\n   000\n  00000\n 0000000\n000000000\n'
    (sortie, erreurs) = subprocess.Popen(["python3","/Users/Quentin/Desktop/Epreuve-Air-Codding-accerelator/afficher_pyramide.py","0","5"], stdout=PIPE).communicate()
    if sortie == sortie_attendu:
        print("air11 (1/1) : success")
    else:
        print("air11 (0/1) : failure")
    return test11
def test12():
    sortie_attendu = b"['1', '2', '3', '4', '5', '6']\n"
    (sortie, erreurs) = subprocess.Popen(["python3","/Users/Quentin/Desktop/Epreuve-Air-Codding-accerelator/rois_des_tris.py","6","5","4","3","2","1"], stdout=PIPE).communicate()
    if sortie == sortie_attendu:
        print("air12 (1/1) : success")
    else:
        print("air12 (0/1) : failure")
    return test12

fonctions_test = test0,test1,test2,test3,test4,test5,test6,test7,test8,test9,test10,test11,test12

for fonction in fonctions_test:
    fonction()