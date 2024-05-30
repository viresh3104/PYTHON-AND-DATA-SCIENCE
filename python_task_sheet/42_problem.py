# Write a Python program to calculate the factorial of a number using
# a for loop.

def factorial(n):
    if n < 0:
        return
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result

if __name__ == "__main__":
    number = int(input("Enter a number to calculate its factorial: "))
    print(f"The factorial of {number} is {factorial(number)}.")
