# function is a block of code that performs specific task 
# two type of functions are there one is user defined function and other is build in function
# built in function is the function which is predefined such as sum(),len(),range(),print(),tuple()
# user defined fun is we can create function to perfrom specific task as per our need 
# user defined function always starts with def ha bs itna kafi hai abhi aao code likhte hai



def Gmean(a,b):       #here we defind the function named Gmean
    mean=(a*b)/(a+b)
    print(mean)       #this is task we want to perform when we call function named Gmean

c=6
d=6
Gmean(c,d)          

e=10
f=34
Gmean(e,f)              # here we used the Gmean function to calculate the mean

def IsGreater(x,z):
    if(x>z):
        print("first number is greater")
    elif(x<z):
        print("second number is greater")
    else:
        print("both numbers are equal")

# here we made function named IsGreater chala baghu he ks kam krte 

h=13
f=12
IsGreater(h,f)

g=4
q=4
IsGreater(g,q)



