# Write a function that takes a list and returns a new list with unique elements (removes duplicates)

def remove_dup():
    stringg = input("Enter the numbers seperated by comma ").split(',')
    string = set(stringg)
    new_list = list(string)
    return new_list

print(remove_dup())