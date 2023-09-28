# Error in Python can be of two types i.e. Syntax errors and Exceptions. 
# Syntax Errors:These are the compile time errors which means that there is a problem with your code syntax
# Exceptional Errors : These are run-time errors which occur when you execute some piece of code.
# try….. except blocks are used in python to handle errors and exceptions.
# The code in try block runs when there is no error. If the try block catches the error, 
# then the except block is executed

try:
    num = int(input("Enter an integer: "))
    num1 = int(input("Enter another number"))
    addition = num1+num
    print(addition)
except ValueError:
    print("Number entered is not an integer.")


# The finally block is always executed, so it is generally used for doing the concluding tasks like 
# closing file resources or closing database connection or may be ending the program execution with
# a delightful message.

try:
    x = 10 / 0             # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always be executed")  

