# The enumerate function is a built-in function in Python that allows you to loop over a sequence
# (such as a list, tuple, or string) and get the index and value of each element in the sequence at the same time.

# names = ["krishna","shiv","swayam","ashay","rohit","vedant"]

# for name,index in enumerate(names):
#     print(name,index)


marks = [22,34,45,56,87,37,92,19]

index = 0
for mark in marks:
    print(mark)
    if (mark==92):
        print("nice viresh")
    index +=1        #this is without using enumerate function

# now by using enumerate function

# for mark,index in enumerate(marks,start=0):
#     print(mark)
#     if(index==6):
#         print("nice viresh")     #this is using enumerate function
