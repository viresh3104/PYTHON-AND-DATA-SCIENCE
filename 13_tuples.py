abc = (1,2,3,4,5,"black","white")
print(type(abc),abc)
print(abc[3])           #this is used to access the perticular index value here its is 4
# tuples are immutable , we cannot chane the tuple 

dfg = (4)     # this is not tuple, this is int, 
#  if we want to add single element to the tuple we have to add comma at the end of it : dfg=(4,) 


# tuples are same as list but the main difference is we can cange the list but cant change the tuple

countries =("india","china","nepal","bhutan")
# now in this countries tuple we have to add pakistan but we cant add it directly
temperory = list(countries)
temperory.append("pakistan")     #append for adding element 
temperory.pop(1)        #pop for removing element
temperory[3]= "usa"             #changing item , here bhutan changes to usa
countries = tuple(temperory)
print(countries)


# this are some operation on tuple