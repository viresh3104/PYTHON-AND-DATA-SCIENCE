# Write a Python program to check if two strings are rotations of each other

def roation(x,y):
    if len(x) != len(y):
        return False
    temp = x + y
    if y in temp:
        return True
    else:
        return False
    

input_string = str(input("Enter the string :: "))
input_string2 = str(input("Enter the string :: "))

print(roation(input_string,input_string2))