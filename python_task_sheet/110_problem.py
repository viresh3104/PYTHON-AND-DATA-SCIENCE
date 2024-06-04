# Write a Python program to find the intersection of two lists.

list_1 = input("Enter the numbers seperated by comma :: ").split(",")
list_2 = input("Enter the numbers seperated by comma :: ").split(",")



list_1 = list(map(int, list_1))
list_2 = list(map(int, list_2))
# map() function is used to convert the list elements from strings to integers.



list_3 = list(set(list_1) & set(list_2))
print("Intersection of two lists :: ", list_3)