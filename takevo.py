import speech_recognition as sr

import speak_now

def takevoice():
    while True:
        #if alarm_set == 1:
            #alarm_clock.check(set_time, reminder)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print ("Listening......")
            r.energy_threshold = 1000 #please change it as per the noise in your surround from 300 to 1000
            r.pause_threshold = 1  #time duration of one word after anather word
            audio = r.listen(source)

        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language='en-in')
            print("User said :", query)
            return query

        except Exception as e:
            speak_now.speak("Say that again please....")