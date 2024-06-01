# Write a Python program that takes a character as input and checks if it is a vowel or consonant

vowels = ("a" , "b" , "c", "d" ,"e" , "A" , "E" , "I" , "O" , "U")

input_char = input("Enter a character::: ")

if input_char in vowels:
    print("The character is a vowel")
else:
    print("The character is a consonant")