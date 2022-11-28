'''
Name: Paul Bello
Project: Weather Application
Purpose: Show current weather data for any location (Also to work on using API's in python)
Date: 11/28/2022
'''

import requests
from pprint import pprint

API_Key = 'd55b38e38c5606daabc3bb36a7f07f61'
location = input('Which city would you like to see the weather report for? ')

base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+location

weatherData = requests.get(base_url).json()

pprint(weatherData)
