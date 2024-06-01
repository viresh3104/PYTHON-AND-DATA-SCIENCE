# Write a function that takes two strings and returns True if they are anagrams, otherwise False. 

def is_anagram(str_1 ,str_2):
    if len(str_1) != len(str_2):
        return False
    else:
        x= sorted(str_1) == sorted(str_2)
        return x
    

str_input = input("enter first string::")
str_input = input("Enter second string::")

print(is_anagram(str_input,str_input))
