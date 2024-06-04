# Write a Python program to find the perimeter of a rectangle given its
# length and width.

def perimeter(lenght:float , breadth:float) -> float:
    perimeter = 2*(lenght+breadth)
    return perimeter


lenght_input = float(input("Enter the lenght :: "))
breadth_input = float(input("Enter the breadth :: "))
print("perimeter is :", perimeter(lenght_input,breadth_input))




