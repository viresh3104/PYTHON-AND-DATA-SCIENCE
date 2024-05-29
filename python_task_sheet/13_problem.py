# Create a function to reverse a given string.

def reverse_string(input_string):
    return input_string[::-1]                      #[::-1] means "take the string and step backwards by 1,


a = input("Enter a string to reverse it :: ")

reversed_string = reverse_string(a)
print(reversed_string)


