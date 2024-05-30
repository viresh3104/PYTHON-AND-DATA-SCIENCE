# Write a Python program that takes a list of numbers and prints the
# sum of all the numbers using a loop.

def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

user_input = input("Enter a list of numbers separated by commas: ")
numbers = [float(num) for num in user_input.split(',')]
total_sum = sum_of_numbers(numbers)
print(f"The sum of all the numbers is: {total_sum}")

