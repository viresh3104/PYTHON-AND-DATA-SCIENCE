# Write a function that takes a string as input and returns the string with reversed words.

def reverse_words(str):
    words = str.split()
    words.reverse()
    return words
    # return ' '.join(words)

input_str = input("Enter a string:")
print(reverse_words(input_str))