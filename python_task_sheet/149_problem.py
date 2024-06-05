# Create a program that efficiently checks if a given string contains all unique characters.

def unique_ele(string):
    return len(set(string)) == len(string)

s = "abcdf"
print(unique_ele(s))