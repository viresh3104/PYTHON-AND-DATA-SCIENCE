import random as rd

list_of_words = ['raigad', 'torna' ,'sinhgad','shivneri','rajgad']
word_which_is_selected_for_game = rd.choice(list_of_words)

list_of_letter_in_word = list(word_which_is_selected_for_game)
print(list_of_letter_in_word)


list_of_underscores = list(len(list_of_letter_in_word)*"_")
print(list_of_underscores)

x = len(list_of_letter_in_word)*1000000000000
counter_for_wrong_attempts = 0

for each_word in range(x):
    user_guess= str(input("Enter your guess :: "))
    if user_guess in list_of_letter_in_word:
        index_of_that_input = list_of_letter_in_word.index(user_guess)
        list_of_underscores[index_of_that_input] = user_guess
        print(list_of_underscores)
        print("congrates you have guessed it right, enter the next letter :: ")

    else:
        if counter_for_wrong_attempts <= 6 :
            counter_for_wrong_attempts += 1
            print(f"opps you have entered the worng letter you have 6 attempts from which you used {counter_for_wrong_attempts}")
        else :
            print("Game Over , you have gussed wrong letter 6 times ")
            break
        

        
    

            


