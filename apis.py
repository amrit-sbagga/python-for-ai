import requests

# Coordinates to get weather data
latitude = 21.25   # Raipur latitude
longitude = 81.62   # Raipur longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(f"Temperature in {latitude}, {longitude} is {data['current']['temperature_2m']}")