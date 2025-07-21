# This is a simple CLI weather tool

import requests
from dotenv import load_dotenv
import os
from colorama import Fore, Style

load_dotenv()  # Load variables from .env

API_KEY = os.getenv("OPENWEATHER_API_KEY")  # Replace this with your actual OpenWeatherMap API key

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(Fore.CYAN + f"Weather in {city}:" + Style.RESET_ALL)
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels like: {data['main']['feels_like']}°C")
        print(f"Description: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']}%")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
