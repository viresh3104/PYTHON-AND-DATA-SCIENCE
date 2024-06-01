# Write a Python program that checks whether a given year is a leap year. 

curr_year = int(input("Enter the year  :: "))


def is_leap(year):
    if year % 4 == 0:
        print("year is leap")
    else :
        print("year is not leap")



print (is_leap(curr_year))