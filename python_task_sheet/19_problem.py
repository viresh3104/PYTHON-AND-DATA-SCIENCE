# Given a list of names, count the number of names that start with a vowel.
def count_names_starting_with_vowel(names):
    vowel = ('a', 'e' ,'i' , 'o' , 'u')
    count = 0
    for x in name:
        if x[0] in vowel:
            count += 1
    return count


name = ["viresh" , "shiv" , "ashay" , "esha" , "om"]
print(count_names_starting_with_vowel(name))


