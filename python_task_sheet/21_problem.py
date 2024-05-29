# Implement a program that takes a sentence and a word as input and checks if the
# word is present in the sentence.

def is_word_in_sentence(sentence, word):
    words = sentence.split()
    return word in words




input_sentence = input("enter the sentence::")
input_word = input("enter the word::")
is_present = is_word_in_sentence(input_sentence, input_word)
print(f"The word '{input_word}' is {'present' if is_present else 'not present'} in the sentence.")
