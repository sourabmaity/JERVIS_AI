'''import speech_recognition as sr
import pyttsx3
import wikipedia
import trace
import webbrowser
from threading import *
import time
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)
query =""
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    return 0
def takevoice():
    global query
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print ("Listening......")
            r.energy_threshold = 1000 #please change it as per the noise in your surround from 300 to 1000
            r.pause_threshold = 0.8  #time duration of one word after anather word
            audio = r.listen(source)

        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language='en-in')
            query = query.lower()
            print("User said :", query)
            #return query
        except Exception as e:
            print(e)
            #speak("Say that again please....")
def work():
    global query
    while True:
        print(query)
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            que = query.replace("wikipedia", "")
            result = wikipedia.summary(que, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif 'open twitter' in query:
            t = Thread(target=speak,args=('Opening please wait',))
            t.start()
            print("Doneljvsldvla")
            t.killed=True

            print("Doneljvsldvla")
            #speak('opening....please wait')
            #webbrowser.open("www.twitter.com")
            #in_process = 1

        query="0"


t1 = Thread(target=takevoice)
t2 = Thread(target=work)
t1.start()
t2.start()
print("khvjh")'''




