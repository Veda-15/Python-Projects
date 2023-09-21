import requests

API_KEY = "8def909cdbdbf962b2c6247d95e0c881"

location = input("Enter the city name: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}"

weather_data = requests.get(url).json()     # requests.get() gives response obj ,.json() parses response obj into json obj

print(weather_data)

# Extract the relevant data from the API response
current_temperature = weather_data["main"]["temp"]
current_description = weather_data["weather"][0]["description"]
current_humidity = weather_data["main"]["humidity"]
current_pressure = weather_data["main"]["pressure"]
current_wind_speed = weather_data["wind"]["speed"]

# Print the current weather conditions
print(f"Temperature: {current_temperature}")
print(f"Description: {current_description}")
print(f"Humidity: {current_humidity}")
print(f"Pressure: {current_pressure}")
print(f"Wind Speed: {current_wind_speed}")

