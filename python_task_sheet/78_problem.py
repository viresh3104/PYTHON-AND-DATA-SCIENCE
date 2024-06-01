# Write a Python program to find the sum of the digits of a number using a while loop.

def sum_of_digits(num):
    sum = 0
    for digits in str(num):
        sum += int(digits)
    return sum
    

print(sum_of_digits(1111))