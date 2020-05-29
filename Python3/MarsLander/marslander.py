import sys
import math

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

# Initialise les variables
pFusee = 0
angle = 0
result=""

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    
    # Augment la puissance de la fusée
    if  abs(v_speed) > 40:
        if pFusee < 4:
            pFusee = pFusee +1
            
    # Diminue la puissance de la fusée
    elif abs(v_speed) < 40:
        if pFusee < 0:
            pFusee = pFusee -1

    result = str(angle) + " " + str(pFusee)   # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    
    # Affiche le résultat
    print(result)
