# Write a Python program to find the longest word in a given string. 

def longest_word(str):
    words = str.split()
    max_lenght = max(len(word)for word in words)
    x = [word for word in words if len(word) == max_lenght]
    return x

    # for word in words:
    #     if len(word) == max_lenght:
            # return word



print(longest_word("hello world vireesh"))