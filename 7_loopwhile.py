# i = 3
# while (i<9):
#     print (i)
#     i = i +1    
# print("done with loop")      normal while loop


# i = int(input("Enter YOUR AGE:"))
# while (i<100):
#     i = int(input("EntER YOUR AGE:"))
#     print(i)
# print("ENTER THE VALID AGE")             while loop with user input


i = int(input("Enter YOUR AGE:"))
while (i<100):                                                                                       
    if(i<18):
        print("you can't drive")
    else:
        print("you can drive")
    i = int(input("EntER YOUR AGE:"))

print("ENTER THE VALID AGE")                      #while loop with user input and if else



multiple_of_five = ""
while multiple_of_five != 'q':
    multiple_of_five = int(input("enter any number to check it is divisible by 5 or q to quit : "))
    if multiple_of_five %5 == 0 :
        print("number is divisible by 5 ")
    else:
        print("number is not divisible by 5")

i = int(input("Enter YOUR AGE:"))
while (i<100):                                                                                       
    if(i<18):
        print("you can't drive")
    else:
        print("you can drive")
    i = int(input("EntER YOUR AGE:"))

print("ENTER THE VALID AGE")                      #while loop with user input and if else
