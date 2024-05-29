def factorial(n):
    if (n == 0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1              this is how recursion works in backend


# Recursion is the process of defining something in terms of itself.
# In Python, we know that a function can call other functions. 
# It is even possible for the function to call itself.
# These types of construct are termed as recursive functions.
# in this example we are using factorial function inside factorial function ,
# bs yahi toh hai rucursion ki ak func khudko hi call krta hai.


    