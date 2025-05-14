import requests
import tkinter as tk
from tkinter import messagebox

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"]
        }
    else:
        return None

def show_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    weather = get_weather(city, API_KEY)
    if weather:
        result = (
            f"🌤️ Weather in {weather['city']}:\n"
            f"Temperature: {weather['temperature']}°C\n"
            f"Humidity: {weather['humidity']}%\n"
            f"Wind Speed: {weather['wind_speed']} m/s\n"
            f"Condition: {weather['description'].capitalize()}"
        )
        output_label.config(text=result)
    else:
        messagebox.showerror("Error", "Could not retrieve weather data.")

API_KEY = "c55aab85cd50a58314cbbeb9acf06c4e"


root = tk.Tk()
root.title("Weather App")

tk.Label(root, text="Enter City Name:").pack(pady=5)
city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=show_weather).pack(pady=10)

output_label = tk.Label(root, text="", justify="left", font=("Helvetica", 10))
output_label.pack(pady=10)

root.mainloop()
