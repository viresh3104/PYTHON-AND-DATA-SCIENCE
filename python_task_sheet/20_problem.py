# Write a function to remove all duplicate characters from a given string.


def duplicate_char(input_str):
    char_already_seen = set()
    final_list = []

    for x in input_str:
        if x not in char_already_seen:
            char_already_seen.add(x)
            final_list.append(x)
    return ''.join(final_list)

input_str = input("enter the string::") 
output = duplicate_char(input_str)
print(output)