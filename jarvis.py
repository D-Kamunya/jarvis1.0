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

def wishme():
	speak("Welcome back Dennis!")
	time_()
	date_()

	hour=dt.now().hour

	if hour>=6 and hour<12:
		speak("Good morning Sir!")
	elif hour>=12 and hour<18:
		speak("Good Afternoon Sir!")
	elif hour>=18 and hour<24:
		speak("Good evening Sir!")
	else:
		speak("Good night Sir!")

	speak("Jarvis at your service. Please  tell me how can I help you today?")


wishme()
