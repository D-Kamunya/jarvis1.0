import pyttsx3 # pip install pyttsx3

engine = pyttsx3.init() # Initialize pyttsx3

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

speak('Hello world')

