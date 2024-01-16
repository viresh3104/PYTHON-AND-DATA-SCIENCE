# The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.
# read (r): This mode opens the file for reading only and gives an error if the file does not exist.
# write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.

# for reading
file = open("viresh.txt", "r")
print(file.read())

# and if we want to read specific number of characters then :
file = open("viresh.txt", "r")
print(file.read(8))  #here 8 character from that file is displayed

# for writing
file = open('geek.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close() #this overwrites the data in file and write above  statements to it

# for append 
file = open("geek.txt","a")
file.write("this wil write this line at the end of that file")