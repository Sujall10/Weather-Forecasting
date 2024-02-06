'''If you find any error in this code 
then you can directly contact me sujal0710rajput@gmail.com'''  

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from geopy.geocoders import Nominatim
import requests
from text import Api_key  # Import API key from config.py

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo

def get_weather():
    city = city_entry.get()
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city)
    
    if location:
        latitude = location.latitude
        longitude = location.longitude
        url = f'http://api.weatherapi.com/v1/current.json?key={Api_key}&q={latitude},{longitude}'
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            weather_data = response.json()
            
            if 'error' not in weather_data:
                weather_info.config(text=f"Weather: {weather_data['current']['condition']['text']}\nTemperature: {weather_data['current']['temp_c']}°C")
            else:
                weather_info.config(text='Failed to fetch weather data. Please try again.')
        except requests.exceptions.RequestException as e:
            weather_info.config(text=f'Error: {e}')
    else:
        weather_info.config(text='Location not found.')

# Create tkinter window
window = tk.Tk()
window.title("Weather Forecast")

# Set a custom theme
style = ttk.Style(window)
style.theme_use('clam')

# Custom colors
background_color = '#f0f0f0'
foreground_color = '#333333'
button_color = '#4CAF50'

# Set custom colors for the theme
style.configure('TLabel', background=background_color, foreground=foreground_color, font=("Helvetica", 14))
style.configure('TButton', background=button_color, foreground=foreground_color, font=("Helvetica", 14))


# Load background image and resize it to cover the full GUI
original_image = Image.open("image.jpg")
copy_of_image = original_image.copy()  # Make a copy to prevent issues with garbage collection
photo = ImageTk.PhotoImage(original_image)

# Create canvas
label = tk.Label(window, image=photo)
label.bind('<Configure>', resize_image)  # Bind the resize function to the label
label.pack(fill=tk.BOTH, expand=True)

# Create widgets
city_label = ttk.Label(window, text="Enter city:")
city_entry = ttk.Entry(window, font=("Helvetica", 14))
get_weather_button = ttk.Button(window, text="Get Weather", command=get_weather)
weather_info = ttk.Label(window, text="")

# Place widgets in the window
city_label.place(x=100, y=50)
city_entry.place(x=200, y=50)
get_weather_button.place(x=300, y=100)
weather_info.place(x=50, y=200)

city_entry.focus()

# Run the tkinter event loop
window.mainloop()
