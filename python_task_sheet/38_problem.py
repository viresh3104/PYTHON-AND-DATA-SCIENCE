# Write a function that takes a number as input and returns True if the
# number is prime, otherwise False.



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage:
n = int(input("Enter the number to check if it is prime or not: "))
result = is_prime(n)
print(result)  
