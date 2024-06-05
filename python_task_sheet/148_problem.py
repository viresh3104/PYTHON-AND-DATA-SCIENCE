# Develop a function that efficiently computes the square root of a given number without using built-in functions.

def sqrt(x):
    if x < 0:
        return None
    
    if x == 0:
        return 0
    
    left , right = 0 , x
    
    while right - left > 1e-10:
        mid = (left+right) / 2

        if mid * mid > x:
            right = mid
        else:
            left = mid
    return (left+right) / 2




print(sqrt(16))  # Output: 4
print(sqrt(25))  # Output: 5
print(sqrt(2))   # Output: approximately 1.41421356237

