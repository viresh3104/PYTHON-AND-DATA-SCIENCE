# Write a Python program that accepts a sequence of comma-separated numbers
# from the user and generates a list and a tuple of those numbers.


a = input("enter a sequence of comma seperated values:: ")
numbers_as_string = a.split(',')

numbers = list(map(int, numbers_as_string))
numbers_as_string = tuple(numbers)



print("list of number :: ", numbers)
print("tuple of number::" , numbers)

