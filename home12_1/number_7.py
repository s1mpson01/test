

import requests

API_KEY = "2db8906df065dcfadac07fdd68f9eff6"

# Координаты
url = f"http://api.openweathermap.org/geo/1.0/direct?q=Moscow&limit=5&appid={API_KEY}"
response = requests.get(url)


lat = response.json()[0]['lat']
lon = response.json()[0]['lon']
print(lat, lon)

# Погода
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}")
print(response.json())