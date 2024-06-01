# Write a Python program to calculate the simple rest given the principal, rate, and time.
def simple_es(p :float, r:float , n) -> float:
    return (p * r * n) / 100

p = float(input("Enter the principle amout:::"))
r = float(input("Enter the rate of rest:::"))
n = float(input("Enter the time period:::"))
print("The simple rest is::",simple_es(p , r , n))