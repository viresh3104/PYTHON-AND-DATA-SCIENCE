# Write a Python program to print numbers from 1 to 100, but for multiples of 3 print "Fizz" 
# instead of the number and for the multiples of 5 print "Buzz". For numbers which are multiples 
# of both three and five print "FizzBuzz". 

def fibi(start , end):
    for i in range(start ,end +1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else :
            print (i)


print(fibi(1,100))