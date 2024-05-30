# Write a function that takes two numbers as arguments and returns
# their sum.


def sum(a,b):
    addition = a+b
    return addition


a = int(input("Enter a number :: "))
b = int(input("Enter second number :: "))

output = sum(a , b)
print("sum of two numbers is : ",output)