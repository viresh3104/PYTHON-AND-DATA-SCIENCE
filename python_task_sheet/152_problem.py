# Develop a function that efficiently computes the power set of a given set.

def power_set(set):
    lenght_of_set = len(set)
    power_set_size = 1 << lenght_of_set      
    result = []

    for counter in range(power_set_size):
        subset = []
        for j in range(lenght_of_set):
            if counter & (1 << j):
                subset.append(set[j])
        result.append(subset)

    return result


input_set = [3,4,6]
print(power_set(input_set))


