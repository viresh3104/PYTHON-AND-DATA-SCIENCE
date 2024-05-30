# Write a Python program to check if two strings are anagrams of each other.


def is_anagram(str_1 , str_2):
    if len(str_1) != len(str_2):
        return False
    
    dict_count = {}

    for char in str_1:
        if char in dict_count:
            dict_count[char] += 1 
        else:
            dict_count[char] = 1

    for char in str_2 :
        if char not in dict_count or dict_count[char] == 0:
            return False
        else:
            dict_count[char] -= 1
    
    return True


str_1 = input("Enter a string ::")
str_2 = input("Enter second string ::")

output = is_anagram(str_1 , str_2)
print(output)