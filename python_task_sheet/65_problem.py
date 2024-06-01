# Write a Python program to find the largest of three numbers. 

a = input("Enter the number :: ")
b = input("Enter the number :: ")
c = input("Enter the number :: ")



if (a > b and a > c):
    print("The largest number is ", a)
elif(b>a and b>c):
    print("The largest number is ", b)
else:
    print("The largest number is ", c)