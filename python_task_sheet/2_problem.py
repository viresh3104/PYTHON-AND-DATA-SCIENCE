# Write a Python program that takes a list of numbers and outputs a new list containing only the
# even numbers from the original list.

def get_even_numbers():
    numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))
    return [num for num in numbers if num % 2 == 0]

even_numbers = get_even_numbers()
print(even_numbers)





