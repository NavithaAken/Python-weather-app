import tkinter as tk
import requests

def fetch_weather():
    api_key = 'YOUR_API_KEY'
    city = city_entry.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather_data = response.json()

    if weather_data['cod'] == 200:
        temperature_label.config(text=f"Temperature: {weather_data['main']['temp']}°C")
        humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
        wind_speed_label.config(text=f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        temperature_label.config(text="City not found")
        humidity_label.config(text="")
        wind_speed_label.config(text="")

# Create the GUI
root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter city:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather)
fetch_button.pack()

temperature_label = tk.Label(root, text="")
temperature_label.pack()

humidity_label = tk.Label(root, text="")
humidity_label.pack()

wind_speed_label = tk.Label(root, text="")
wind_speed_label.pack()

root.mainloop()
