# Implement a function that removes a key-value pair from a dictionary.

def remove_key(dict , key):
    if key in dict:
        del dict[key]
    return dict

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict)
key_to_remove = input("enter key to remove::")


print(remove_key(my_dict, key_to_remove))