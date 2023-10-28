import time
currenttime = int(time.strftime("%H")) 
print(currenttime)
if currenttime<12:
    print("goodmorning viresh")
elif currenttime>18:
    print("goodafternoon viresh")
else:
    print("goodnight viresh")
