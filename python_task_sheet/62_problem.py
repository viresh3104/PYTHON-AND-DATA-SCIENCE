# Write a Python program that asks the user for their name and age, and then prints a message saying how old they will be in 10 years. 

def greet_fun(name , age : int):
    age = age + 10
    return (f"Hello {name} and you will be {age} years old after the 10 years from now")


n = input ("Enter your name:: ")
a = int(input ("Enter your current age:: "))

print(greet_fun(n,a))