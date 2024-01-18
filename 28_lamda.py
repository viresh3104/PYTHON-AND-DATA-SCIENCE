# this is used to write one liner function 
# we can write a function inside a function using lamda

cube = lambda x : x*x*x  #here we write lambda function for cube without defining it 
print(cube(5)) 

def double(x):
    return x*2
# now for above function we can simply write 
double = lambda x : x*2
# both are same but lambda do it in more eficient way

# we can also write multiple values in lambda function
avg = lambda x , y ,z : print((x+y+z)/3) 
avg(1,2,3)

# checking git status 
# hi this is omkar and i am gchecking git stat