# Write a function that takes a number n and returns a list of its divisors.

def divisor(num:int) -> list:
    empty_list_with_one = [1]
    for i in range(2,num):
        if num % i == 0:
            empty_list_with_one.append(i)
    return empty_list_with_one
    

num_input = int(input("Enter number onwards 1 :: "))
print(divisor(num_input))
