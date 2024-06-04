# Write a Python program to find the second largest element in a list.



def second_largest(input_list):
    unique_sorted_list = sorted(list(set(input_list))[1:])
    return unique_sorted_list[-1]


list = list(map(int,input("Enter number seperated by comma ::").split(",")))
print(second_largest(list))