# Write a Python program that prints all the prime numbers between 1 and 100.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
        return True
    

for i in range(1,101):
    if is_prime(i):
        print(i)


