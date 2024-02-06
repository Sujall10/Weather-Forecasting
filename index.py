'''If you find any error in this code 
then you can directly contact me sujal0710rajput@gmail.com'''  

import tkinter as tk
from tkinter import ttk
from geopy.geocoders import Nominatim
import requests
from text import Api_key #importing Api_key from text.py

def get_weather():
    city = city_entry.get()
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city)
    
    if location:
        latitude = location.latitude
        longitude = location.longitude
        #Your API_key here
        url = f'http://api.weatherapi.com/v1/current.json?key={Api_key}&q={latitude},{longitude}'
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            weather_data = response.json()
            
            if 'error' not in weather_data:
                weather_info['text'] = f"Weather: {weather_data['current']['condition']['text']}\nTemperature: {weather_data['current']['temp_c']}°C"
            else:
                weather_info['text'] = 'Failed to fetch weather data. Please try again.'
        except requests.exceptions.RequestException as e:
            weather_info['text'] = f'Error: {e}'
    else:
        weather_info['text'] = 'Location not found.'

window = tk.Tk()
window.title("Weather Forecast")


style = ttk.Style(window)
style.theme_use('clam')

background_color = '#f0f0f0'
foreground_color = '#333333'
button_color = '#4CAF50'

style.configure('TLabel', background=background_color, foreground=foreground_color, font=("Helvetica", 14))
style.configure('TButton', background=button_color, foreground=foreground_color, font=("Helvetica", 14))

city_label = ttk.Label(window, text="Enter city:")
city_entry = ttk.Entry(window, font=("Helvetica", 14))
get_weather_button = ttk.Button(window, text="Get Weather", command=get_weather)
weather_info = ttk.Label(window, text="")

city_label.grid(row=0, column=0, padx=10, pady=10)
city_entry.grid(row=0, column=1, padx=10, pady=10)
get_weather_button.grid(row=1, columnspan=2, padx=10, pady=10)
weather_info.grid(row=2, columnspan=2, padx=10, pady=10)

city_entry.focus()

label1=ttk.Label(text="Created by: Rajput Sujal")
label1.grid(row=4, columnspan=5, padx=10, pady=50)

window.mainloop()
