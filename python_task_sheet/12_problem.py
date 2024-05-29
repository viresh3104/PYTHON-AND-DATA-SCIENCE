# Given a list of words, concatenate them into a single string separated by spaces.
user_input = input("Enter a list of words separated by commas: ")
words = user_input.split(',')
single_string = ' '.join(words)
print(single_string)
