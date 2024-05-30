# Write a function that takes a list of strings and returns a new list with
# each string capitalized.


def capitalize_strings(strings):
    return [s.upper() for s in strings]

strings = ["hello", "world", "python"]


new_string = capitalize_strings(strings)
print(f"Capitalized strings: {new_string}")  
