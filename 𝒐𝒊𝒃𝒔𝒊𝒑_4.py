import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

def get_weather(city):
    API_key = "6be19753f287cf7411b28cffc50e82bd"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)
    
    if res.status_code == 404:
        messagebox.showerror("Error","City not found")
        return None
    
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temperature = weather['main']['temp'] - 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']


    icon_url = f" https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return(icon_url, temperature, description, city, country)



def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    icon_url, temperature, decription, city, country = result
    location_label.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon
    
    
    temperature_label.configure(text=f"Temperature: {temperature:.2f} °C")
    description_label.configure(text=f"Description: {description}")





top = ttkbootstrap.Window(themename="morph")
top.title("Weather Forecast App")
top.geometry("500x500")

city_entry=ttkbootstrap.Entry(top, font="Helvetica, 18")
city_entry.pack(pady=10)

search_button = ttkbootstrap.Button(top, text="Search", command=search, bootstyle="warning")
search_button.pack(pady=10)

location_label = tk.Label(top, font="Helvetica, 25")
location_label.pack(pady=10)

icon_label = tk.Label(top)
icon_label.pack()

temperature_label = tk.Label(top, font="Helvetica, 20")
temperature_label.pack()

description_label = tk.Label(top, font="Helvetica, 20")
description_label.pack()


top.mainloop()

