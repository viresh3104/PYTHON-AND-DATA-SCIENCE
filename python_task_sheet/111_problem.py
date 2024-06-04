# Write a Python program to flatten a nested list.

def flatten_list(nested_list):
    flattened = []
    
    def _flatten(sublist):
        for element in sublist:
            if isinstance(element, list):
                _flatten(element)
            else:
                flattened.append(element)
    
    _flatten(nested_list)
    return flattened

# Example usage
nested_list = [1, [2, 3, [4, 5]], 6, [7, [8, [9, 10]]]]
flattened_list = flatten_list(nested_list)
print(flattened_list)