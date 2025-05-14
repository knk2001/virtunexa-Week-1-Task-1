import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
        return weather
    else:
        return {"error": data.get("message", "Unable to retrieve data")}


def display_weather(weather):
    if 'error' in weather:
        print("Error:", weather['error'])
    else:
        print(f"\nWeather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description'].capitalize()}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")


def main():
    api_key = "c55aab85cd50a58314cbbeb9acf06c4e"
    city_name = input("Enter city name: ")
    weather = get_weather(city_name, api_key)
    display_weather(weather)


if __name__ == "__main__":
    main()
