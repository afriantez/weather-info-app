import requests

def get_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
    
def display_weather(data):
    if data:
        city_name = data['name']
        temperature = data['main']['temp']
        weather = data['weather'][0]['description']
        print(f"City: {city_name}")
        print(f"Temperature: {temperature} degree in Celcius")
        print(f"Weather: {weather}")
    else:
        print("Could not retrieve weather data. Please check the city name.")

if __name__ == "__main__":
    api_key = "0a84a782d7e534ab71bff428550db262"
    city = input("Enter city name ")
    weather_data = get_weather_data(city, api_key)
    display_weather(weather_data)
    