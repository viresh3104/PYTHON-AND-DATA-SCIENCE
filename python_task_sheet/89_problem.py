# Write a Python program to check if a given number is divisible by 5 and 11.

input_num = int(input("Enter the number:: "))
if input_num % 5 == 0 and input_num % 11 == 0:
    print("The number is divisible by 5 and 11")
else:
    print("The number is not divisible by 5 and 11")