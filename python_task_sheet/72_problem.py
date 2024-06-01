# Write a function that takes a number and returns its factorial using recursion. 

def fact(num:int):
    if (num == 1 or num == 0):
        return 1
    else:
        return num * fact(num-1)
    

x = int(input("Enter a number::"))

print(fact(x))