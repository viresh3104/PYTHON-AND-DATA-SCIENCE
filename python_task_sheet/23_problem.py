# Write a program that finds the most frequent element in a list

from collections import Counter

def freq_ele(list):
    if not list:
        return None
    counter = Counter(list)
    freq_ele , Count = counter.most_common(1)[0]
    return freq_ele



list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"The most frequent element is: {freq_ele(list)}")
