# A variable is a named location in memory that stores a value. 
# In Python, we can assign values to variables using the assignment operator =

# local variable : a variable which is defined within function and accesible only within that function
# global :  a variable that is defined outside of a function and is accessible from within any function in your code.

viresh = 19

def age():
    ashay = 18
    krishna = 20
    print(ashay)
    print(krishna)
    print(viresh)   #this viresh fun is accesible in age function as it defined globaly
age()

#but if i try to access the variable ashay and krishna outside age fun then it shows error
# print(ashay,krishna) this shows error

# now if we want to modify global variable within a fun then global keyword comes in use

x = 10

def my_variable():
    global x     # here 'global' keyword tells python that we are working with a global variable
    x = 1
    print (x)

print(x)    # here x will print because we change the x using global avriable from 10 to 1