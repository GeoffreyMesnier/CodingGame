game loop
while True:
   IndexCible = 0
   mountainMax = 0
   for i in range(8):
       mountain_h = int(input())  # represents the height of one mountain.
       if i == 0:
           mountainMax = mountain_h
       elif mountain_h > mountainMax:
           mountainMax = mountain_h
           IndexCible = i
   # Write an action using print
   # To debug: print("Debug messages...", file=sys.stderr)

   # The index of the mountain to fire on.
   print(IndexCible)
