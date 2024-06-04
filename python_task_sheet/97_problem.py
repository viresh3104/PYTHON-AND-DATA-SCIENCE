# Write a Python program to find the sum of the first n natural numbers using a while loop.


def sum_num(num):
    sum = 0
    numi = 1
    while numi <= num:
        sum += numi
        numi += 1
    return sum
    
print(sum_num(8))
