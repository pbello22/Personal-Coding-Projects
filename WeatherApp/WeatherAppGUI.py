'''
name: Paul Bello
Project: Make a GUI for basic weather app (add on from original project)
Purpose: Make weather app more user friendly, work on interface skills, and more work on using API's and API implementation
date: 11/28/2022

Project inspired by freeCodeCamp
The only part of code that was the same as freeCodeCamp is the defining of API_Key, base_url, and weatherData. The rest of the code is my own idea and code.

IN PROGRESS!!!!!!
working on implementing changing background for each weather report type (rainy, cloudy, sunny, etc).
'''

from tkinter import *
import requests
from pprint import pformat
import json

#import tkinter as tk

root = Tk()
root.title('Current Weather App')

root.geometry("650x1000") 

bgimg = PhotoImage(file = "Sunny.PNG")
label1 = Label( root, image = bgimg)
label1.place(x = 0, y = 0)


#Clear message from entry area
def click(event):
   location.configure(state=NORMAL)
   location.delete(0, END)
   location.unbind('<Button-1>', clicked)

  
#Initialize API
API_Key = 'd55b38e38c5606daabc3bb36a7f07f61'
#Get location and create entry area
location = Entry(root, width=30)
location.insert(0, 'Enter location here...')
location.pack()
#Clear out the entry area for user input
clicked = location.bind('<Button-1>', click)





#Create click command for the button
def Click():
  textBox.delete("1.0", "end") 
  base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+location.get()
  weatherData = requests.get(base_url).json()
  
  #Print location in proper/title case format 
  textBox.insert(INSERT, 'Here is the weather report for ' + location.get().title() + '\n')

  temp = int(weatherData['main']['temp'] - 273.15)
  feels_like = int(weatherData['main']['feels_like'] - 273.15)
  humidity = int(weatherData['main']['humidity'])
  
  if int(weatherData['clouds']['all']) >= 60:
    clouds = 'Cloudy'
  elif int(weatherData['clouds']['all']) >= 25:
    clouds = 'Some clouds'
  else:
    clouds = 'Clear'

  pressure = round(int(weatherData['main']['pressure'])/33.863886666667, 2)
  weatherDesc = weatherData['weather'][0]['description']
  
  
  weatherText = f"Temperature (Celsius): {temp}°\nFeels Like (Celsius): {feels_like}°\nCloud status: {clouds}\nHumidity: {humidity}%\nPressure: {pressure}inHg\nWeather: {weatherDesc}\n"
  textBox.insert(INSERT, weatherText) 







  
#Create Button for Check Weather
myButton = Button(root, text="Check Weather", command=Click)
myButton.pack()

textBox = Text(root, width=60, height=10)
textBox.pack()

root.mainloop()
