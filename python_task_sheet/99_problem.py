# Write a Python program to find the greatest common divisor (GCD)
# of two numbers using a loop.

def gcd(n,m):
    gcd = 1
    for i in range(1 , min(m,n) + 1):
        if m % i == 0 and n % i == 0:
            gcd = i
    return gcd
    
# now find lcm::
def lcm(n,m):
    return (n*m)// gcd(n,m)



first_num = int(input("Enter a number :: "))
second_num = int(input("Enter a number :: "))
print("GCD is ::",gcd(first_num,second_num))
print("LCM is ::",lcm(first_num,second_num))