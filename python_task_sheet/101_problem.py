# Write a Python program to count the number of substrings in a given string.

strin = str(input("Ente a string :: "))
count = 0
words = strin.split()
for i in words:
    count += 1
   
print("Number of substrings in the given string is :: ", count)