number = int(input("enter the number"))
if(number>0):
    if(number<=10):
         print("entered number is positive and is between 0 to 10")
    elif(number<=20):
         print("entered number is positive and is between 11 to 20")
    elif(number<=30):
         print("entered number is positive and is between 21 to 30")
    else:
         print("entered number is posotive and greater than 30")
elif(number<0):
    print("number is negative")
else:
     print("number is zero")
     

#here we can  write many if elif else condition inside a if or else condition
