list = []

list.insert(0 , 1)                 #this will enter 1 number at 0th index number
list.insert(1, 7)
list.insert(2, 9)
print("list ::",list)                        # this will print the list



list.remove(int(input("enter the number you want to remove:: ")))                     #this will remove the occurance of 7 
print("list after removing a item from list::", list)


list.append(int(input("enter the number you want to append:: ")))
print("list after adding a item in the end of list:: ", list)


list.sort()
print("list will be sorted in ascending order:: ", list)


list.pop()
print("last element from the list is removed:: ", list)


list.reverse()
print("this will reverse the whole list::", list)





