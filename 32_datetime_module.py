from datetime import datetime , timedelta

# by using above importing tech we will able to import only those classes which is needed no need to import whole module
# like import datetime

current_time = datetime.now()
print(f"current time is {current_time}")


# time formatting 
formatted_time = current_time.strftime("%Y/%m/%d")    #here values are seprated by / sign 
print(f"\nFormatted Time: {formatted_time}")


# adding or subtracting days, hours and minutes to the date by user input

    
added_days = current_time + timedelta(days=5)   #adding 5 days to the current date
print("\nAdded Days : ", added_days)

subtracted_hours = current_time - timedelta(days=2000)     #subtracting  3 hours from the current time
print("Subtracted Hours :", subtracted_hours)



# here i wrote a code for taking user input as how many days he wants to add in current date and time
try :
    add_days = int(input("Enter number of days you want to add: "))
    added_date = current_time + timedelta(days=add_days)   #timedelta function is used for this purpose which adds given no.of days to the present 
    print(f"\nDate after adding {add_days} days: {added_date}")
except ValueError :
    print("\nInvalid Input! Please enter a valid integer.")