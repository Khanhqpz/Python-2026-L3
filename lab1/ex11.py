
import math

x1 = float(input("Enter for x1: "))
y1 = float(input("Enter for y1: "))
x2 = float(input("Enter for x2: "))
y2 = float(input("Enter for y2: "))

distance = math.sqrt((x1-x2) ** 2 + (y1-y2) ** 2)
print ("Answer = ", distance)