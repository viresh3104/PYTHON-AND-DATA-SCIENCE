# Write a program that efficiently finds the maximum sum subarray within a given list of integers.

def max_sum_subarray(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
        
    return max_so_far


arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_sum_subarray(arr))