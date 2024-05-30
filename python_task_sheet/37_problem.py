# Write a function that checks if a given string is a palindrome (reads
# the same forwards and backwards).


def palindrome(word):
    return word == word[::-1]


word = input("enter a word to check it is a palindrome or not :: ")
print(palindrome(word))