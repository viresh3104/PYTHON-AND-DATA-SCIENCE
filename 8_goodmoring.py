import time
currenttime = int(time.strftime("%H")) 
print(currenttime)
if currenttime<12:
    print("goodmorning srishti")
elif currenttime>18:
    print("goodafternoon srishti")
else:
    print("goodnight srishti")