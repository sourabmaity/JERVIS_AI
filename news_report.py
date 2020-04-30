
from selenium import webdriver
import takevo
import speak_now
import speech_recognition as sr
import pyautogui
import find
def news_report():
    driver = webdriver.Chrome("C:/Users/sourab/Desktop/jervis/chromedriver.exe")
    driver.get('http://feeds.bbci.co.uk/news/video_and_audio/world/rss.xml')
    speak_now.speak("Today important newses are....")
    for x in range(1, 20):
        news = driver.find_element_by_xpath("/ html / body / div[3] / div[1] / div/div["+str(x)+"]/ul/li/a")
        speak_now.speak(news.text)
        query = takevoice(1).lower()
        query_match = find.matching(query)
        if int(query_match)==19:
            news.click()
            while(True):
                query = takevoice(0).lower()
                query_match = find.matching(query)
                if int(query_match)==20:
                    pyautogui.hotkey('Alt', 'left')
                    break
        elif int(query_match)==21:
            y = x -1
            news = driver.find_element_by_xpath("/ html / body / div[3] / div[1] / div/div[" + str(y) + "]/ul/li/a")
            speak_now.speak(news.text)
            query = takevoice(0).lower()
            query = find.matching(query)
            if int(query_match)==19:
                news.click()
        elif int(query_match)==16:
            return
def takevoice(data):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.energy_threshold = 1000
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print("User said :", query)
        return query

    except Exception as e:
        if data==1:
            speak_now.speak("Next news is ")
        return "0"


