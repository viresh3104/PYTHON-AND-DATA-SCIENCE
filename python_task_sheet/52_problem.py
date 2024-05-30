# Write a Python program to find the key of the maximum value in a dictionary.


def max_value(dict):
    return max(dict, key=dict.get)

sample_dict = {
    'a': 10,
    'b': 55,
    'c': 32,
    'd': 55
}



print(max_value(sample_dict))