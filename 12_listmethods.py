#list methods means some operations performed on list 
#similar to string operation in 4.1 and 4.2

abc = [1,2,3,4,5]
colours = ["green","blue","red","white","orange","voilet"]
#            0        1     2      3       4        5
abc.reverse()
colours.reverse()
print(abc)
print(colours)

#abc.sort()    this function sorts the list in ascending order 
#abc.sort(reverse=True)   this function sorts the list in decending order
#abc.reverse()      this method reverses the string
#colours.index("red")   this method returns the index of first occurance of that list item, here it is 2
#colours.count("blue")  this method count the number of times given list item repeated in string
#colours.append("black") this method adds given item to end of the list
# colours.insert(3,"black") this method adds black to colours list at 3rd index value
# colours.extend(abc)  this method add entire abc list to end of colours list
# if we dont want to use extend we can also concatenate list as below
# print(colours+abc)  that set , ho gye saare operations list ke upr itne hi hai