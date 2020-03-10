import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
thor_x = 0
thor_y = 0
eclair_x = 0
eclair_y = 0
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    #Initialise les variable de position
    mouvement = ""
    if thor_x == 0  and thor_y == 0 and eclair_x == 0 and eclair_y == 0:
        thor_x = initial_tx
        thor_y = initial_ty
        eclair_x = light_x
        eclair_y = light_y
        # TODO: write code...

    #Gestion position
    #Deplacement horizontal et vertical
    if (thor_x < 40) and (thor_y<17) or ((thor_x >= 0) and (thor_y >= 0)):
        if thor_x == eclair_x:
            if thor_y > eclair_y:
                mouvement = "N"
                thor_y = thor_y - 1
            elif thor_y < eclair_y:
                mouvement = "S"
                thor_y= thor_y + 1

        if thor_y == eclair_y:
            if thor_x > eclair_x:
                mouvement = "W"
                thor_x = thor_x - 1
            elif thor_x < eclair_x:
                mouvement = "E"
                thor_x = thor_x + 1

        #Deplacement diagonale

        if (thor_x < eclair_x) and (thor_y < eclair_y):
            mouvement = "SE"
            thor_x = thor_x + 1
            thor_y= thor_y + 1
        if (thor_x > eclair_x) and (thor_y > eclair_y):
            mouvement = "NW"
            thor_x = thor_x - 1
            thor_y = thor_y - 1
        if (thor_x < eclair_x) and (thor_y > eclair_y):
            mouvement = "NE"
            thor_x = thor_x + 1
            thor_y = thor_y - 1
        if (thor_x > eclair_x) and (thor_y < eclair_y):
            mouvement = "SW"
            thor_x = thor_x - 1
            thor_y= thor_y + 1



    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(mouvement)
