# Write a Python program to find the sum of all odd numbers between 1 and 100. 


def sum_of_odds(start,end):
    sum = 0
    for i in range(start , end+1):
        if i % 2 != 0:
            sum += i
    return sum

print(sum_of_odds(1,100))