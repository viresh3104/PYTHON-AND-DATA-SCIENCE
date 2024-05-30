# Write a Python program to count the number of vowels in a given string




inputstring = input("Input any string: ")

if inputstring.lower() == "x":
    print("String is empty")
else:
    vowels = ('a', 'e', 'i', 'o', 'u')
    count = 0
    for char in inputstring.lower():
        if char in vowels:
            count += 1
    print(f"The number of vowels in the given string is: {count}")

