# This is a simple CLI weather tool

import requests
from dotenv import load_dotenv
import os
from colorama import Fore, Style

load_dotenv()  # Loads variables from .env

API_KEY = os.getenv("OPENWEATHER_API_KEY")  # Replace this with your actual OpenWeatherMap API key

def get_weather(city):

    while True:
        temp_unit = input("Choose temperature unit:\n1.Celsius\n2.Fahrenheit\nType 1 or 2: ")
        if temp_unit == '1':
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units=metric"
            break
        elif temp_unit == '2':
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}&units=imperial"
            break
        else:
            print("Wrong input. Please try again.")

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(Fore.CYAN + f"Weather in {city}:" + Style.RESET_ALL)
        print(f"Temperature: {data['main']['temp']}")
        print(f"Feels like: {data['main']['feels_like']}")
        print(f"Description: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']}m/s")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
