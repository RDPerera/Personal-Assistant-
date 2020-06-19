import Drowsiness_Detection  as dd
import os
import time
import datetime
import playsound
import subprocess
import speech_recognition as sr
from gtts import gTTS
from selenium import webdriver
WAKE = "hello system"
def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def assistant_speaks(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio(): 
  
    rObject = sr.Recognizer() 
    audio = '' 
  
    with sr.Microphone() as source: 
        print("Speak...") 
          
        # recording the audio using speech recognition 
        audio = rObject.listen(source, phrase_time_limit = 5)  
    print("Stop.") # limit 5 secs 
  
    try: 
  
        text = rObject.recognize_google(audio, language ='en-US') 
        print("You : ", text) 
        return text 
  
    except: 
  
        assistant_speaks("Could not understand your audio, PLease try again !") 
        return "0"

def search_web(input): 
	print("hello world") 
	driver = webdriver.Firefox() 
	driver.implicitly_wait(1) 
	driver.maximize_window() 

	if 'youtube' in input.lower(): 

		assistant_speaks("Opening in youtube") 
		indx = input.lower().split().index('youtube') 
		query = input.split()[indx + 1:] 
		driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query)) 
		return

	elif 'wikipedia' in input.lower(): 

		assistant_speaks("Opening Wikipedia") 
		indx = input.lower().split().index('wikipedia') 
		query = input.split()[indx + 1:] 
		driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query)) 
		return

	else: 

		if 'google' in input: 

			indx = input.lower().split().index('google') 
			query = input.split()[indx + 1:] 
			driver.get("https://www.google.com/search?q =" + '+'.join(query)) 

		elif 'search' in input: 

			indx = input.lower().split().index('google') 
			query = input.split()[indx + 1:] 
			driver.get("https://www.google.com/search?q =" + '+'.join(query)) 

		else: 

			driver.get("https://www.google.com/search?q =" + '+'.join(input.split())) 

		return

def open_application(input): 

	if "chrome" in input: 
		assistant_speaks("Opening  Chrome") 
		os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe') 
		return
	if "tracking" in input: 
		assistant_speaks("Opening  eye tracking..Drowsiness Detection Activated.") 
		dd.run()
		return
	elif "dev" in input: 
		assistant_speaks("Opening Dev C ++") 
		os.startfile("C:\Program Files (x86)\Dev-Cpp\devcpp.exe") 
		return
	elif "music" in input: 
		assistant_speaks("Playing Music") 
		os.startfile("D:\Songs\y2mate.com - blackpink_ddu_du_ddu_du_mv_IHNzOHi8sJs_1080p.mp4") 
		return
	else: 

		assistant_speaks("Application not available") 
		return


def process_text(input): 
    try: 
        if 'search' in input: 
            # a basic web crawler using selenium 
            search_web(input) 
            return
  
        elif "who are you" in input or "define yourself" in input: 
            speak = '''Hello, I am Your Digital personal Assistant.'''
            assistant_speaks(speak) 
            return
  
        elif "note" in input: 
            assistant_speaks("What would you like me to write down?")
            note_text = get_audio()
            note(note_text)
            assistant_speaks("I've made a note of that.")
            return
  
        elif 'open' in input: 
              
            # another function to open  
            # different application availaible 
            open_application(input.lower())  
            return
  
        else: 
  
            assistant_speaks("I can search the web for you, Do you want to continue?") 
            ans = get_audio() 
            if 'yes' in str(ans) or 'yeah' in str(ans): 
                search_web(input) 
            else: 
                return
    except :
        return
        #assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?") 
        #ans = get_audio() 
        #if 'yes' in str(ans) or 'yeah' in str(ans): 
        #    search_web(input)

while True:
    print("Listening")
    text = get_audio().lower()
    if text == "0":
        continue
    if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
            assistant_speaks("Ok bye, "+ name+'.') 
            break
    process_text(text)
    
