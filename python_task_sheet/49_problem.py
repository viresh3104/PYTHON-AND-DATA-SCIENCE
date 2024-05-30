# Write a Python program to create a dictionary from two lists, one of keys and one of values.

key_list = [1,2,3,4,5]
value_list = ["a",2,3,4,5]

def create_dict(key_list ,value_list):
    if len(key_list) != len(value_list):
        raise ValueError("keys and values must be equal ")
    return dict(zip(key_list,value_list))


print(create_dict(key_list,value_list))