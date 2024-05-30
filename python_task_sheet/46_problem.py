# Write a Python program to find the first non-repeating character in a given string.

def count(input_str):
    char_count = {}

    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else :
            char_count[char] = 1

    for char in input_str:
        if char_count[char] == 1 :
            return char
        


input_str = input("any strug hrere to find first non repeting char in it ::")
output = count(input_str)
print(output)