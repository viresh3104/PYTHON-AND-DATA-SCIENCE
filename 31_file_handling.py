# writing in a text file , if this file is not present in current directory , it will make that file and then write it
with open("write.txt" , "w") as file:
    file.write("this is my first file using python \n w is used to write in a file")


# when we use w i.e write , and if we want to save and add anoter line then it is not possible write in that case append use
with open("append.txt","a") as file:
    file.write("\n a is used for append and when we use a it saves previous file \n it saves this text how many time you run this file")


# lets see how to read a file which we created im append 
with open("append.txt","r") as file :
    abc = file.read()        #we have to print it so we stored in a variable 
print(abc)


with open("names.txt" ,"r") as file :
    abcd = file.readlines()               #this readlines function read each line one by one
for each_line in abcd:
    print(f"hello and welcome {each_line.rstrip()} ")                #rstrip only cuts tralling charac from right
