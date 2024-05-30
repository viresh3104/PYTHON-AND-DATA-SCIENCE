# Write a Python program that converts temperatures from Celsius to
# Fahrenheit. The formula is F = C * 9/5 + 32.

input_temp = int(input("Enter the temp in celsius to convert it into fahrnheit :: "))


def temp_f(input_temp):
    x = input_temp + (273)
    return x


print(temp_f(input_temp),"farhnheit .")