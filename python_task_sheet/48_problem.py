# Write a Python program to replace all occurrences of a specified
# substring in a given string with another substring.



def replace_occ(input_str , replace_substring , new_substring):
    return input_str.replace(replace_substring , new_substring)



a = input("Enter the string :: ")
b = input("Enter the substring to be replaced :: ")
c = input("Enter the new substring :: ")

output = replace_occ(a , b , c)
print(output)