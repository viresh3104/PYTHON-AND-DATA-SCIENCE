# Write a function that takes a list of numbers and returns the largest
# number in the list.



def largest_number():
    numbers = input("enter numbers seprated by spaces::")
    numbers = list(map(int,numbers.split()))
    return max(numbers)


largest_numbers = largest_number()
print(largest_numbers)