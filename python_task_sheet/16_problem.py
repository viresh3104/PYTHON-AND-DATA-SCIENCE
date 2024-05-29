# Given a string, write a function to remove all vowels from it and return the
# modified string.



inputstring = input("input any string:: ")

if inputstring == "x":
    print("string is empty")
else :
    newstr = inputstring

vowels = ('a', 'e', 'i', 'o', 'u');

for x in inputstring.lower():
    if x is vowels:
        newstr = newstr.replace(x, "")
print(newstr)
