import sys
import math

# Don't let the machines win. You are humanity's last hope...
#Class pour les noeuds
class Noeud:
    def __init__(self,coordonnee_x, coordonnee_y):
        self.x =coordonnee_x
        self.y = coordonnee_y
        #print("x y valeur",coordonnee_x, coordonnee_y,valeur, file=sys.stderr)
        self.coordNoeud=str(self.x)+" "+str(self.y)

        self.resultat=""
        #self.coordNoeud=""
        self.coordNoeudDroit="-1 -1"
        self.coordNoeudBas="-1 -1"

listeComplete=[]

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
listeResultat=""

#Création des noeud
#On parcours la grille sur la hauteur
for y in range(height):
    listeNoeud=[]
    line = input()  # width characters, each either 0 or .
    print("y : ",y," line : ",line, file=sys.stderr)
    #On parcours la grille sur la largeur
    for x in range (width):
        print("x : ",x," line : ",line, file=sys.stderr)
        if line[x] == "0":
            p = Noeud(x,y)
            listeNoeud.append(p)
    if len(listeNoeud)!=0:
        listeComplete.append(listeNoeud)

#print("coord noeud x=0 y=0 ",listeComplete[0][0].coordNoeud , file=sys.stderr)
#print("coord noeud x=0 y=1 ",listeComplete[1][0].coordNoeud , file=sys.stderr)
#print("coord noeud x=0 y=1 ",listeComplete[1][0].coordNoeud , file=sys.stderr)
#Deuxieme parcours liste des noeuds pour ajout voisin


print("longueur liste y ",len(listeComplete), file=sys.stderr)
print("longueur liste x ",len(listeComplete[0]) , file=sys.stderr)
print("Liste 0: :", listeComplete[0][0].coordNoeud, file = sys.stderr)
print("Liste 1 :" ,listeComplete[0][1].coordNoeud, file = sys.stderr)
print("Liste 2 :" ,listeComplete[1][0].coordNoeud, file = sys.stderr)
print("Liste 3 :" ,listeComplete[1][1].coordNoeud, file = sys.stderr)



#On parcours la liste crée
#On parcours sur la hauteur
for y in range(len(listeComplete)):
    #On parcours sur la largeur
    print("Y : ",y , file = sys.stderr)
    for x in range(len(listeComplete[y])):
        #Horizontale
        #if x > y:

        #if ((x < len(listeComplete[y])-1) and ( y <= len(listeComplete)-1) and (y != 1)):
        #print("X : ",x , file = sys.stderr)
        #Noeud de droite:
        if len(listeComplete[y]) !=1:
            if x < len(listeComplete[y])-1 and ((y < len(listeComplete)-1 or (y==0))) :
                print("Noeud y x : ", y, x, "ajout noeud droit y x : ", y, x+1, file = sys.stderr)
                listeComplete[y][x].coordNoeudDroit=listeComplete[y][x+1].coordNoeud
                #On rempli la coordonnée du noeud en bas
                #print("Y : ",x , file = sys.stderr)

        #Noeud du bas
        if len(listeComplete) != 1:
            if ((y < len(listeComplete)-1) and ((x < len(listeComplete[y])-1) or (x==0)):
            #if ((y < len(listeComplete)-1) and (x <= len(listeComplete[y])-1 ) and (x != 1)):
                print("Noeud y x : ", y , x, "ajout noeud bas y x :", y+1, x,file = sys.stderr)
                listeComplete[y][x].coordNoeudBas = listeComplete[y+1][x].coordNoeud

"""      if x < y:
            if y < len(listeComplete)-1:
                listeComplete[y][x].coordNoeudBas=listeComplete[y+1][x].coordNoeud
                if x < len(listeComplete[y])-1:
                    listeComplete[y][x].coordNoeudDroit=listeComplete[y][x+1].coordNoeud
"""


for y in range(len(listeComplete)):
    for x in range(len(listeComplete[y])):
        listeResultat += listeComplete[y][x].coordNoeud+" "
        listeResultat += listeComplete[y][x].coordNoeudDroit+" "
        listeResultat += listeComplete[y][x].coordNoeudBas+"\n"

        print("noeud ",listeComplete[y][x].coordNoeud, file=sys.stderr)
        print("noeuddroit ",listeComplete[y][x].coordNoeudDroit, file=sys.stderr)
        print("noeudbas ",listeComplete[y][x].coordNoeudBas, file=sys.stderr)
# Three coordinates: a node, its right neighbor, its bottom neighbor
print(listeResultat, file=sys.stderr)
print(listeResultat)
