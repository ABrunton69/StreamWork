import os
import speech_recognition as sr
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
from bs4 import BeautifulSoup
import requests

warnings.filterwarnings('ignore')



def recordAudio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('System is listening!')
        audio = r.listen(source)

        data = ''
        try: 
            data = r.recognize_google(audio)
            print('System heard: ' +data)
        except sr.UnknownValueError:
            print('System could not understand what you said!')
        except sr.RequestError as e:
            print('System found a result error' +e)

        return data

def assistantResponse(text):

    print(text)

    myobj = gTTS(text= text, lang='en-uk', slow=False)
    myobj.save('response.mp3')
    os.system('start response.mp3')

def wakeWord(text):
    WAKE_WORDS = ['system']

    text = text.lower()

    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    return False

def greeting(text):

    GREETING_INPUTS = ['yo', 'hello', 'whats up']

    GREETING_RESPONSES = ['yo', 'hello', 'whats good']

    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'
    
    return ''

while True:

    text = recordAudio()
    response = ''

    if(wakeWord(text)) == True:

        response = response + greeting(text)

        if('how are you' in text):
            response = 'I am great'

    assistantResponse(response)
