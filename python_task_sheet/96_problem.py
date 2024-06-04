# Write a Python program to find the sum of the first n natural
# numbers using a for loop.






def sun(num):
    sum = 0
    for i in range(1 , num+1):
        sum += i
    return sum





num = int(input("number::"))
print(sun(num))