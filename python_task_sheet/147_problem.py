# Implement an algorithm to efficiently find the longest increasing subsequence in a list of integers.


def longest_subsequence(arr):
    if not arr:
        return 0

    dp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i] , dp[j]+1)
    return max(dp)



arra = [10, 9, 2, 5, 3, 7, 101, 18]
print(longest_subsequence(arra)) 


