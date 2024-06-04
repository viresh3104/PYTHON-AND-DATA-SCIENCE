# Write a function that takes a string and returns the string with each word capitalized.


def capitalized(string):
    words = str(string)
    capital = words.title()
    return capital

x = input("enter a string::")
print(capitalized(x))