# Implement a function that checks if a given string is a pangram (contains all letters
# of the alphabet).

import string

def is_pangram(sentence):
    alphabets = set(string.ascii_lowercase)
    sentence_input = set(sentence.lower())

    return alphabets.issubset(sentence_input)


sentence = input("Enter the string to check it is a pangram or not : ")
if is_pangram(sentence):
    print("given string is pangram")
else:
    print("given string is not a pangram")