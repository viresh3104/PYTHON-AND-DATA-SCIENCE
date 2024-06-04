# Write a Python program to check if a given string is a valid identifier.

import keyword

def is_valid_identifier(x):
    if keyword.iskeyword(x):
        return False
    if x.isidentifier():
        return True
    return False

identifier = input("Enter a string to check if it's a valid identifier: ")
if is_valid_identifier(identifier):
    print(f"'{identifier}' is a valid identifier.")
else:
    print(f"'{identifier}' is not a valid identifier.")

    
