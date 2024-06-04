# Write a Python program to merge two dictionaries and keep the values of common keys in a list.

def marge_dict(dict_1 ,dict_2):
    merge_dict = {**dict_1 , **dict_2}
    for key,value in list(merge_dict.items()):
        if key in dict_1 and key in dict_2:
            merge_dict[key] = [value,dict_2[key]]
    return merge_dict


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(marge_dict(dict1, dict2))


# not solved 
#  cgpt