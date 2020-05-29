import sys
import math

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

# Initialisation liste
extList=[]
mineList=[]
mineDict={}
fichList =[]
resultat = ""

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    #Ajout des éléments dans la liste
    extList.append(ext)
    mineList.append(mt)
    mineDict[ext.upper()]=mt
    
# Parcours la liste des fichiers
for i in range(q):
    fname = input()
    
    #Recupere l'extension du fichier en majuscule
    listeChaine=fname.split('.')
    extFichier=(listeChaine[-1])
    extFichier=extFichier.upper()

    #Gestion des noms de fichiers sans "."
    if "." not in fname:
        resultat += "UNKNOWN"+"\n"

    #Gestion des extensions inconnus
    elif extFichier not in mineDict.keys():
        resultat += "UNKNOWN"+"\n"
    
    #Ajout du mine type au resultat
    else:
        for ext2 in mineDict.keys():
            if extFichier ==  ext2:
                resultat += mineDict[ext2] +"\n"
              
# Affiche le résultat
print(resultat)
