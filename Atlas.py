import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import requests
import time 

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#engine.say('hello.. my name is Atlas..')
#engine.say('how can i help you')

def talk(text):
	engine.say(text)
	engine.runAndWait()

def take_command():
	command = ''
	try:
		with sr.Microphone() as source:
			print('listening..')
			audio = r.listen(source)
			command = r.recognize_google(audio)
			command = command.lower()
			if 'atlas' in command:
				command = command.replace('atlas', '')
				print(command)
			else:
				take_command()
	except:
		pass
	return command


def run_atlas():
	command = take_command()
	Time = time.strftime("%I:%M %p").lower()
	if 'play' in command:
		song = command.replace('play', '')
		talk('playing ' + song)
		pywhatkit.playonyt(song)
	elif 'time' in command:
		time1 = datetime.datetime.now().strftime('%I:%M %p')
		talk(time1)
		talk('current time is ' + time1)
	elif 'set alarm for' in command:
		talk('{}'.format(command))
		command = command.replace('set alarm for', '')
		command = command.replace('.','' )
		command = command.lstrip(' ')
		print(command)

		while command != Time:
			print(Time)
			Time = time.strftime("%I:%M %p").lower()
			time.sleep(5)
		if command == Time:
			print('time to wake up')
			talk('time to wake up')
			pywhatkit.playonyt('https://www.youtube.com/results?search_query=suicide+silence+wake+up')
	elif 'who is' or 'what is a' in command:
		person = command.replace('who is', '')
		person = command.replace('what is a', '')
		info = wikipedia.summary(person, 1)
		talk(info)
	elif 'what is the weather in' in command:
		api_address='http://api.openweathermap.org/data/2.5/weather?appid=48e7991b9835bb0122d235b684632446&q='
		command = command.replace('what is the weather in', '')
		temp = '&units=imperial'
		url = api_address + command + temp
		json_data = requests.get(url).json()
		format_add = json_data['main']
		str_format = str(format_add)
		talk('the weather for {} is: '.format(command))
		talk(str_format)
	elif 'open' in command:
		command = command.replace('open', '')
		talk('opening ' + command)
		os.startfile(command)
		
			
	elif 'joke' in command:
		talk(pyjokes.get_joke())
	else:
		talk('sorry.. please say that again.. i did not understand')



while True:

	 run_atlas()