# Write a Python program to calculate the distance between two points (x1, y1) and (x2, y2)


import math

def dist(x1:float ,x2 :float, y1:float , y2:float) -> float:
    return math.sqrt((x2 -x1)**2 + (y2 - y1)**2)


x1 = int(input("Enter value of x1:: "))
y1 = int(input("Enter value of y1:: "))
x2 = int(input("Enter value of x2:: "))
y2 = int(input("Enter value of y2:: "))

print(dist(x1, x2 , y1 , y2))