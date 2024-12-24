import requests

API_KEY = "API_KEY"
city_name = input(str('Enter your city name: \n'))
URL = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'

response = requests.get(URL).json()

print(f"{response}")

