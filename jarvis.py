import pyttsx3 # pip install pyttsx3
from datetime import datetime as dt

engine = pyttsx3.init() # Initialize pyttsx3

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def time_():
	time_=dt.now().strftime("%I:%M:%S") # 12 hour clock
	speak("The  current time is ")
	speak(time_)

def date_():
	day=dt.now().day
	month=dt.now().month
	year=dt.now().year
	speak("The current date is ")
	speak(day)
	speak(month)
	speak(year)

date_()


