# Write a Python program to calculate the area of a rectangle given its
# width and height.


lenght = int(input("Enter the lenght of a rectanle to find its area::"))
breadth = int(input("Enter he breadth of a rectangle to find its area::"))


def area(lenght , breadth):
    area_of_r = lenght * breadth
    return area_of_r


a = area(lenght , breadth)

print("area of given rectangle is :: ",a,"ms^2")