# Write a Python program that accepts a sequence of comma separated 4 digit
# binary numbers as its input. The program will print the numbers that are divisible
# by 5 in a comma separated sequence.


a = input("enter 4 digit binary comma seperated values:: ")
numbers_as_string = a.split(',')

numbers_as_integer = [int(b,2) for b in numbers_as_string]


for i in numbers_as_integer :
    if i % 5 == 0:
        print(i)
    else :
        i = i +1
        