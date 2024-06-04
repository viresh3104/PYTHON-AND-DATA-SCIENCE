# Write a Python program to count the frequency of each word in a
# given text using a dictionary.

strin = str(input("Ente a string :: "))
dict = {}

for i in strin :
    if i in dict :
        dict[i] += 1
    else :
        dict[i] = 1
    
print (dict)