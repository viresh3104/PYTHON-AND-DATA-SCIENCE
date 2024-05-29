# Write a Python program to find the length of the longest word in a sentence.

def longest_word(input_string):
    words = input_string.split()
    longest = max(words, key=len)
    return longest

input_string = input("enter the string:: ")
longest = longest_word(input_string)
print(longest)
