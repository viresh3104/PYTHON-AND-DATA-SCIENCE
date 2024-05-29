# Given a list of dictionaries, find the dictionary with the highest value for a specific key.

def highest_value(dict, key):
    if not dict:
        return None
    
    max_dict = None
    max_value = float("-inf")

    for d in dict:
        if key in d and d[key] > max_value:
            max_value = d[key]
            max_dict = d
        return max_dict
    

dict = [
    {'name': 'Alice', 'age': 30, 'score': 85},
    {'name': 'Bob', 'age': 25, 'score': 90},
    {'name': 'Charlie', 'age': 35, 'score': 88}
]


key = input("enter key to find highest value of ::")


result = highest_value(dict, key)
print(f"The dictionary with the highest value for key '{key}' is: {result}")



# Using float('-inf') guarantees that max_value will be 
# updated to the value of the first dictionary key we encounter, regardless of what that value is.