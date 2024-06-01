# Write a function that takes a list of strings and returns the longest string. 
# Use a while loop to iterate over the list and compare the length of each string.
# If the current string is longer than the previous longest string, update the longest string.
# Return the longest string at the end of the function.



def longest_str():
    string = input("enter the list of string seperated by comma::").split(',')
    return max(string , key = len)


print(longest_str())