# Write a function that takes a list of strings and returns a list of strings sorted by their length.


def len_str(list):

    return sorted(list, key=len)

len_str()
