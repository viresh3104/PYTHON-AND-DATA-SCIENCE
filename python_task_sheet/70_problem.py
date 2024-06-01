# Write a function that takes a list of numbers and returns their average. 

input_string = input("Enter the list of numbers seprated by commas:: ")
input_list = [int(x) for x in input_string.split(',')]
print("The average of the list is:: ", sum(input_list)/len(input_list))
