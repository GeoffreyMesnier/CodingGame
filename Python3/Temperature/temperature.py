import sys
import math

tempsMin=0
n = int(input())  # the number of temperatures to analyse
# Parcours toutes les températures
for i in input().split():
    
    # t: a temperature expressed as an integer ranging from -273 to 5
    t = int(i)

    #Gere exception si aucune temperature
    if n == 0:
        tempsMin=0
    elif tempsMin == 0:
        tempsMin = t
    elif abs(tempsMin) > abs(t):
        tempsMin = t
    elif abs(tempsMin) == abs(t):
        if t > tempsMin:
            tempsMin = t
            
# Affiche le résultat
print(tempsMin)
