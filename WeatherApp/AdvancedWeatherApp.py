'''
name: Paul Bello
Project: Make a GUI for weather app 
Purpose: Make weather app more user friendly and work on interface skills
date: 11/28/2022

IN PROGRESS!!!!!!
'''

from tkinter import *
import requests
from pprint import pformat
#import tkinter as tk

root = Tk()

root.geometry("650x1000") 

bgimg = PhotoImage(file = "Sunny.PNG")

label1 = Label( root, image = bgimg)
label1.place(x = 0, y = 0)



#e = Entry(root, width=50)
#e.pack()

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

def Click():
  base_url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+location.get()
  weatherData = requests.get(base_url).json()
  
  #Print location in proper/title case format
  myLabel1 = Label(root, text='Here is the weather report for ' + location.get().title(), font='Helvetica 12 bold')
  myLabel1.pack()
  #Print out data from API
  myLabel2 = Label(root, text=pformat(weatherData))
  myLabel2.pack()


#Create Button for Check Weather
myButton = Button(root, text="Check Weather", command=Click)
myButton.pack()


root.mainloop()
