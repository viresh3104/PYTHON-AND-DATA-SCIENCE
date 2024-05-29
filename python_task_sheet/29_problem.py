# Create a function that takes a list of dictionaries and sorts them based on a specified key.

def sort(dict,sort_key):
    return sorted(dict , key=lambda x:x[sort_key])


dictionaries = [
    {'name': 'Alice', 'age': 25, 'city': 'New York'},
    {'name': 'Bob', 'age': 30, 'city': 'San Francisco'},
    {'name': 'Charlie', 'age': 20, 'city': 'Los Angeles'}
]



str_sorted_by_name = sort(dictionaries , "name")
print(str_sorted_by_name)