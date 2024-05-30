# Write a Python program to print all the keys and values in a dictionary

dict_1 = {1:"a" , 2:"b"}

def printing_dict(dict):
    for key , value in dict.items():
        print(key ,":", value)


print(printing_dict(dict_1))