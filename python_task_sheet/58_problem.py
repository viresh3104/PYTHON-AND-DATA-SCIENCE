# Write a Python program to remove an item from a tuple.

tuple = (1,2,3,4,5,"black","white")
print(tuple)


drop_item = input("enter the item which you want to drop")

for i in tuple:
    temp_str = str(tuple)
    if i == drop_item:
        temp_str = temp_str.replace(i,"")
        break
    print(temp_str)


