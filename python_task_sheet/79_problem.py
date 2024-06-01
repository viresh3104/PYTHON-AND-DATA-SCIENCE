# Write a Python program to count the number of words in a given string. 

def count_n(string):
    words = string.split(" ")
    num_words = len(words)
    return num_words

    
print(count_n("Hello World viresh here"))