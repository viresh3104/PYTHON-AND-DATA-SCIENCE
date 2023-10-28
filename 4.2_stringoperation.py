# strings are immutable means we can't change the string
name = "my name is VirEsh and i'm 19 yEAr old..................."
print(name)

print(len(name)) #len used to calculate number of character in string

print(name.upper()) #used to covert all character in string into upper case

print(name.lower()) #used to covert all character in string into lower case (Viresh to viesh)

print(name.replace("VirEsh","swayam")) # used to replace any characyer in string

print(name.split(" ")) #it is used to split the string from whatever character you want , 
# i used space in above string to split

print(name.split("a")) #here i used 'a' character to split the string

print(name.rstrip(".")) #this function removes traling character from right side of string
# we can also use lstrip to remove traling character from left side of string