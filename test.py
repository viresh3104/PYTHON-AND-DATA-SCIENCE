n = int(input())
arr = list(map(int,input().split(",")))
max_element = max(arr)
pop = arr.pop(arr.index(max_element))
arr1 = arr
max_element_in_arr_1 = max(arr1)
print(max_element_in_arr_1)

# max = max(arr)
