# Write a function that takes a list of numbers and returns the list
# sorted in ascending order without using the built-in sort() method.

def sorting(list):

    n = len(list)
    for i in range(n):
        for j in range(0 , n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


list = [2,1,3,4,8,5]
print(sorting(list))