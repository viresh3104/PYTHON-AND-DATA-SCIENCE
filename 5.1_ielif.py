#if else used for only one condition but if programmer wants to implement more than one condition
# then we use elif confition , this is same as is else if in c language 

number = int(input("enter any number"))
if(number>0):
    print("entered number is positive")
elif(number<0):
    print("entered number is negative")
else:
    print("number is zero")

    
# we can add as much as conditions we want
