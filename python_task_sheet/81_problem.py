# Write a Python program to check if a given string is a valid email address. 

import string

def remove_punc(input_str):
    x = str.maketrans('','',string.punctuation)
    # he first is a string specifying the set of characters to be translated, the second is a string 
    # specifying the set of characters to translate to 
    # and the third is a string (or set of characters) that we want to replace.

    return input_str.translate(x)

print(remove_punc("hello world !!??"))