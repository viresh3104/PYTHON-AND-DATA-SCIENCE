
def reverse_str(str):
    word = str.split()
    reverse_words = word[::-1]
    reverse_str = " ".join(reverse_words)
    return reverse_str



input_str = input("enter a string to reverse it::")
output_str = reverse_str(input_str)
print(output_str)

