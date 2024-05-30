# Write a Python program to find the index of an item in a tuple.

def index_find(tuple_, item):
    if item in tuple_:
        index = tuple_.index(item)
        return index
    else:
        return -1

tuple = (1,2,3,4,5,"black","white")
print(tuple)
item = input("enter a item to find its index number:: ")
x = (index_find(tuple,item))
print(x)