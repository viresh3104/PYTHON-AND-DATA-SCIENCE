# Write a Python program that counts the number of occurrences of each character in a given string using a dictionary.

def char_countt(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1  
    return char_count


if __name__ == "__main__":
    input_string = input("Enter the string to find occurrence of each character in that string: ")
    result = char_countt(input_string)
    print(result)
