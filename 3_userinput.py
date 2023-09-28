a = input("enter your name :")  
print("my name is",a)

b = input("enter a number:")
c = input("enter another number:")
print("b+c=",b+c)
# assume one number is 5 and another is 10 and we have to add but this gives us result 510
# reason is python takes all user inputs as a string we have to covert them into int by using typecating
# which is eplicit type casting

d = input("enter a number:")
e = input("enter another number:")
print("d+e=",int("%d")+int("%e"))
