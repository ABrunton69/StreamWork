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

res = requests.get('https://www.bbc.co.uk/news')
soup = BeautifulSoup(res.text, 'lxml')

news_box = soup.find('a', {'class': 'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-paragon-bold nw-o-link-split__anchor'})
all_news = news_box.find_all('h3')

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

def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    month_names = ['January' 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st',
                   '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
    
    return 'Today is '+weekday+' '+month_names[monthNum -2]+' the '+ ordinalNumbers[dayNum -1]+' .'

while True:

    text = recordAudio()
    response = ''

    if(wakeWord(text)) == True:

        response = response + greeting(text)

        if('how are you' in text):
            response = 'I am great'

        if('latest news' in text):
            for news in all_news:
                response = 'The latest news headline on BBC News is'+'. '+news.text
        if('time' in text):
            now = datetime.datetime.now()
            meridiem = ''
            if now.hour >=12:
                meridiem = 'p.m'
                hour = now.hour - 12
            else:
                meridiem = 'a.m'
                hour = now.hour

            if now.minute < 10:
                minute: '0'+str(now.minute)
            else:
                minute = str(now.minute)
            response = response +' '+'It is '+str(hour)+ ':'+ str(minute)+ ' '+meridiem+ ' .'
        if('date' in text):
            get_date = getDate()
            response = response +' '+get_date

    assistantResponse(response)
