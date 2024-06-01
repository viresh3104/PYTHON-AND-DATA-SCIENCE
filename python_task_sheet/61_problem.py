# Write a Python program to calculate the area of a triangle given its base and height. 


def area_of_triangle(base:float,height:float) -> float:
    area = (base*height)/2
    return area


b = int(input("Enter the base of traingle:: "))
h = int(input("Enter the height of traingle:: "))

print("Area of this traingle is :: ", area_of_triangle(b ,h))