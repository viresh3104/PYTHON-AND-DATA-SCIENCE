# Write a program that reads a text file containing numerical data and calculates the FFT (Fast Fourier Transform) using NumPy.

import numpy as np

def read_data(file_path: str) -> np.ndarray:
    data = np.loadtxt(file_path)
    return data

def calculate_fft(data: np.ndarray) -> np.ndarray:
    return np.fft.fft(data)


def main():
    file_path = 'numpy.txt'

    data = read_data(file_path)
    print("Original Data:")
    print(data)
    
    fft_result = calculate_fft(data)
    print("\nFFT of the Data:")
    print(fft_result)


if __name__ == "__main__":
    main()
