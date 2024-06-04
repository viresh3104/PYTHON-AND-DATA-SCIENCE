# Write a Python program to create a dictionary from a list of keys and a list of values.

list_of_keys = input("Enter the comma seperated keys :: ")
list_of_values = input("Enter the comma seperated values :: ")
list_of_keys = list_of_keys.split(",")
list_of_values = list_of_values.split(",")

dict = dict(zip(list_of_keys, list_of_values))
print(dict)