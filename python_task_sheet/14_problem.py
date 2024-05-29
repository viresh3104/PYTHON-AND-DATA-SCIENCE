# Write a program that takes sentence  as input and counts the number of single_word in it.

def count_words(a):
    single_word = a.split()
    return len(single_word)


a = input("Enter a sentence : ")
word_count = count_words(a)
print(f"The number of single_word in the a is: {word_count}")