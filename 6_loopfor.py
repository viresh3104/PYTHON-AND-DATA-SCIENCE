# Sometimes a programmer wants to execute a group of statements a certain number of times.
#  This can be done using loops. 
# 2 types of loops one is for loop and another is while loop

# for loop:
# for loops can iterate over a sequence of iterable objects in python.
# itrating over a string
intro = "viresh"
for name in intro:
    print(name)

introd = "shiv"
for x in introd:
    print(x)

# itrating over a list
friends = ["shiv","swayam","vinayak","krishna","yash","rohit"]
for names in friends:
    print(names)
    for x in names:
        print(x) #we can use any variable insted of x and names in loop
# Similarly, we can use loops for sets and dictionaries.



# What if we do not want to iterate over a sequence? What if we want to use 
# for loop for a specific number of times?
# Here, we can use the range() function
for p in range(6):    #this is aslo writeen as (0,6)
    print(p) 

for q in range(1,9):
    print("q::",q)

for r in range(3,20,2): #check logic (startvalue, stop value, steps)
    print("r:::",r)
