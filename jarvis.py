import pyttsx3 # pip install pyttsx3
from datetime import datetime as dt
import speech_recognition as sr

import wikipedia # pip install wikipedia

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


def TakeCommand():
	r=sr.Recognizer()
	with sr.Microphone(device_index=0) as source:
		print("Listening....")
		r.adjust_for_ambient_noise(source,duration=1)
		# r.pause_threshold=1 # Will determine how long it will wait for the user to command
		audio=r.listen(source)

	try:
		print('Recognizing....')
		query = r.recognize_google(audio,language='en-US')
		print(query)

	except Exception as e:
		print(e)
		print('Say that again please....')
		return "None"

	return query	

if __name__ == "__main__":

	wishme()

	while True:

		query=TakeCommand().lower()

		if "time" in query:
			time_()
		
		elif "date" in query:
			date_()

		elif "wikipedia" in query:
			speak("Searching....")
			query=query.replace("wikipedia","")
			result=wikipedia.summary(query,sentences=3)
			speak("According to wikipedia")
			print(result)
			speak(result)
