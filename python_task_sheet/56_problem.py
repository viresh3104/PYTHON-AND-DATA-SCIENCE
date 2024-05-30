# Write a Python program to convert a tuple to a string.


def tup_to_str(tup):
    temp_str = str(tup)
    return temp_str

tuple = (1,2,3,4,5,"black","white")
print(tup_to_str(tuple))