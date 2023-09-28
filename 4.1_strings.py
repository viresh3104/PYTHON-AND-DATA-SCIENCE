intro = "i am studying in CSE_AI at Gh raisoni in first year"

print(intro.capitalize()) #this function capitalize first character and remaing all changes into lower case
# in this name string first letter i.e. i changes to I and remaing all goes to lower case

print(intro.center(60))
print(intro.center(100)) #used to aligns the string as per parameter given by user

print(intro.count("i"))
print(intro.count("a")) # it counts the number of times character is occured in string

print(intro.endswith("r"))
print(intro.endswith(".")) #it check the given string ends with given character

print(intro.startswith("i am")) #same as endswith but it checks staring of string

print(intro.find("at"))
print(intro.find("Gh")) #searches the first occuraces of given value and return the index where it present
#and if give a character which is not present in string then it returns -1

print("isAlnum::",intro.isalnum()) #used to check string consists of alpha numeric character i.e. A-Z, a-z, 0-9
# if any punctions or any other character is present then it gives false other wise it is true
#spaces are also not allowed

print(intro.isalpha()) #same as isalnum but it allows only A-Z, a-z. numbers are not included

print(intro.islower()) #checks the all character in string is in lower case or not 

print(intro.isprintable()) #checks the all character in string is printable or not 

print(intro.isspace()) #true when all characters are spaces in string otherwise false

print(intro.istitle()) #true when first letter of all words are in upper case

print(intro.swapcase()) #upper case converted to lower case and lower case to upper case



