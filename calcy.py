a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("+")
print("-")
print("*")
print("/")

ope = input("Enter the operation you want to perform: ")

if ope == "+":
    c = a + b
    print(a + b)
elif ope == "-":
    c = a - b
    print(a - b)
elif ope == "*":
    c = a * b
    print(a * b)
else:
    c = a / b
    print(a / b)

opp2 = input(f"Do you want to continue with {c}? 1 for yes / 2 for no: ")

while int(opp2) == 1:
    e = int(input("Enter another number: "))
    print("+")
    print("-")
    print("*")
    print("/")
    opes = input("Enter the operation you want to perform: ")
    if opes == "+":
        c += e
        print(c)
    elif opes == "-":
        c -= e
        print(c)
    elif opes == "*":
        c *= e
        print(c)
    else:
        c /= e
        print(c)
    opp2 = input(f"Do you want to continue with {c}? 1 for yes / 2 for no: ")

if int(opp2) == 2:
    a  = float(input("Enter first number again:"))
    b = float(input("Enter second number again:"))
                     
                    
