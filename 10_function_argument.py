# there are 4 types of function argument
# Default Arguments
# Keyword Arguments
# Variable length Arguments
# Required Arguments


# now we see one by one 
# first is default argument
##### def AVG(a,b):
#####    AVG=("average is",(a+b)/2)
# above is a normal function , in normal function we use required arguments


def AVG(a=5,b=3):
    print("average is",(a+b)/2)
AVG()        #in this case input is not provided so function use default values i.e. 5,3
AVG(2,8)     #but here values are provided so default values are ignored


#lets see one more example of default argument

def name(firstname,middlename="somnath",lastname="navtake"):
    print("hello",firstname,middlename,lastname)
name("viresh")


# now keyword arguments
# in this argument order doesn't matter for variable 
# (a=4,b=5)==(b=5,a=4)


# moving forward required arguments
# in this if we wrote (a,b=3) then value of a is coumpulsory and b is optional
# other example (a,b,c=13) a and b are compulsory and c is optional 


# last one is variable length argument
# assume that we have to calculate avg or aum of multiplr numbers 
def AVGG(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("avg is",sum/len(numbers))

AVGG(4,6,3,3,4)
AVGG(1,1,1,1,1,1,1,1)