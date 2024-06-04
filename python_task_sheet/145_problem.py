# Implement a program that calculates the moving average of a NumPy array with a specified window size.


import numpy as np
def moving_avg(arr,ws):
    return np.convolve(arr , np.ones(ws)/ws , mode='valid')


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(moving_avg(arr, 4))
