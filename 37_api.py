import requests

API_key = 'c81ed871789ad1a351723bca97da6b42'
city_name = input("Enter name of city to view its weather : ")

url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'

response = requests.get(url)
print(response)

if response.status_code == 200:
    weather_data = response.json()                    #we recive respone data in jason format 
    temp = weather_data["main"]["temp"] - 273.15       #here in this data tepm data is under main data and main data is under json
    print(f"temperature of {city_name} is {int(temp)} C")
else :
    print(f"city name {city_name} is not found ")
    