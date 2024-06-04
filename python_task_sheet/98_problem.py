# Write a Python program to print all the numbers between 1 and 100
# that are divisible by 7.


def divisible():
    list = []
    for i in range(1, 101): 
        if i % 7 == 0:
            list.append(i)
    return list
            
        
print(divisible())