
def is_anagram(str_1 ,str_2):
    if len(str_1) != len(str_2):
        return False
    
    count = {}
    for char in str_1:
        count[char] = count.get(char , 0)+1
    for char in str_2:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
    return True



str1 = "listen"
str2 = "silent"
print("Are the strings anagrams?", is_anagram(str1, str2))
