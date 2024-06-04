# Write a Python program to find the frequency of each word in a
# given string.


strin = str(input("Ente a string :: "))
dict = {}

for i in strin.split() :
    if i in dict :
        dict[i] += 1
    else :
        dict[i] = 1
    
print (dict)