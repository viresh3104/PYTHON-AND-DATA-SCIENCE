# Given a list of numbers, create a NumPy array and find the sum and product of its elements. 

import numpy as np

def sum_and_product(input_str):
    values = [val.strip() for val in input_str.split(",")]
    num_arr = np.array(values, dtype=int)
    sum_elements = np.sum(num_arr)
    product_elements = np.prod(num_arr)
    
    return sum_elements, product_elements


input_str = input("enter a string::")
sum_elements, product_elements = sum_and_product(input_str)
print(f"Sum: {sum_elements}, Product: {product_elements}")
