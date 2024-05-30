# Write a Python program that takes a user's age and prints whether
# they are a minor (under 18), an adult (18-65), or a senior (65+).

age = int(input("ENter your age :: "))


if (age>=18):
    if(age<=65):
        print("you are a adult")
    else:
        print("you are senior")
else:
    print("you are minor")