# Write a Python program to check if a given number is a palindrome.

def is_palindrome(num):
    num_to_str = str(num)
    if num_to_str == num_to_str[::-1]:
        return True
    else:
        return False


number = input("Enter the number to check it is palindrome or not:: ")
print(is_palindrome(number))