# Write a Python program to count the frequency of each character in
# a given string using a dictionary.


def count_char(str):
    dict = {}
    for char in str:
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict


print(count_char("HelloWorld"))