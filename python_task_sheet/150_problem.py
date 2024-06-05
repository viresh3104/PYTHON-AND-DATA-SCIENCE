# Design a function that efficiently sorts a list of strings based on their lengths.

def sort_string(list):
    return sorted(list , key=len)


list = ["anc","ab","a"]
print(sort_string(list))