import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

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

print("Debug: ",extList,file=sys.stderr)
print("Debug: ",mineDict,file=sys.stderr)
for i in range(q):
    fname = input()

    #Recupere l'extension du fichier en majuscule
    listeChaine=fname.split('.')
    extFichier=(listeChaine[-1])
    extFichier=extFichier.upper()

    print("Debug ext: ",extFichier," / ",fname,file=sys.stderr)

    #Pas de point dans le nom de fichier
    if "." not in fname:
        resultat += "UNKNOWN"+"\n"

    #Extension pas dans la liste
    elif extFichier not in mineDict.keys():
        resultat += "UNKNOWN"+"\n"
            #print("Debug: ",resultat,file=sys.stderr)
    #Ajout du mine type au resultat
    else:
        for ext2 in mineDict.keys():
            if extFichier ==  ext2:
                resultat += mineDict[ext2] +"\n"
                #print("Debug: ",resultat,file=sys.stderr)



# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
print(resultat)
