name = "viresh"
# everything in "?" or '?' is known as string
print(name)
print("my name is",name)
print("hello",name)
# if we have to write a multiple line string or a multiple line paragraph then we use """?""" or '''?''' 


# accesing character in string
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

# accesing character in string for using for loop beacause above process is too lenghty and time counsuming
for character in name:
    print(character)


# for accesing a particular characters in string (also known as string slicing)
print(name[0:3]) 
# gives characters from 0 to 3, including 0 but not including 3
print(name[:3])
# if we didn't write initial address , python takes it as 0
print(name[4:6])


# we can directly calculate the length of string by using len function
print(len(name))
# write len infront of string name is compulsory

