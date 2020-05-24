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

# recordAudio()
