import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
tempsMin=0
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5

    t = int(i)

    #Gere le cas aucune temperature
    if n == 0:
        tempsMin=0
    elif tempsMin == 0:
        tempsMin = t
    elif abs(tempsMin) > abs(t):
        tempsMin = t
    elif abs(tempsMin) == abs(t):
        if t > tempsMin:
            tempsMin = t

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(tempsMin)