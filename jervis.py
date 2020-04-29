import datetime
import wikipedia
import webbrowser
import os
import requests
import pyautogui
import screen_short
import news_report
import whatsapp
import random
import speak_now
import selected_speak
import takevo
import psutil
import wmi
import find
#import translate
import cam_face
#import alarm_clock


c=wmi.WMI(namespace='wmi')
method = c.WmiMonitorBrightnessMethods()[0]
in_process = 256
alarm_set = 0
url_start = 'https://api.openweathermap.org/data/2.5/weather?q='
url_end = '&appid=6e9484c75f7ae54279a3107143392639'
youtube_url = "https://www.youtube.com/results?search_query="
google_url = "https://www.google.com/search?source=hp&ei=YOxDXZ_FCp2SvQSU_7TIBg&q="

def start():
    hour=int(datetime.datetime.now().hour)  # 1 to 24 hour give
    if hour>=0 and hour<12:
        speak_now.speak("Good Morning sir!")
    elif hour>=12 and hour<18:
        speak_now.speak("Good Afternoon sir!")
    else:
        speak_now.speak("Good Evening sir!")
    speak_now.speak("I am JERVIS. How can i help you sir ?")

def file():
    f_location = 'D:/'
    speak("OK sir, which operation do you want to do ?")
    while True:
        work = takevoice().lower()
        if 'open' in work:
            while True:
                work = work.replace('open ', '')
                files = f_location+'/'+work
                print(files)
                try:
                    os.startfile(files)
                    f_location = files
                    break
                except:
                    speak("Tell me the specific name of the file")
                    work = takevoice().lower()
        elif 'create new' in work:
            speak("Tell me the name of the file")
            while True:
                name = takevoice().lower()
                speak("Sir please check that the spelling of the word and kindly say that is perfect or not")
                check = takevoice().lower()
                if 'yes' in check:
                    os.chdir('C:\\Users\\Maity Gini Palace\\Desktop')
                    os.mkdir(name)
                    speak("Folder is created on your desktop")
                    break
                elif'no' in check:
                    speak("Ok Sir please tell me the file name another time")
        elif 'delete' in work:
            speak("Tell me the name of the file")
            while True:
                name = takevoice().lower()
                try:
                    os.rmdir(name)
                    speak("Folder is deleted")
                    break
                except:
                    speak("Folder is not found , tell me the folder name another time")
        elif 'rename' in work:
            speak("Which folder do you want to rename ?")
            re_name = takevoice().lower()
            speak("Whats the new folder name ?")
            name = takevoice().lower()
            os.rename(re_name,name)
            speak("Folder name is changed")
        elif 'go back' in work:
            speak("Back to the previous location")
            f_location = os.path.dirname(f_location)
            os.startfile(f_location)

if __name__=="__main__":
    cam_face.face_matching()
    speak_now.speak("Face matched")
    start()
    while True:
        #if alarm_set == 1:
            #alarm_clock.check(set_time, reminder)
        query = takevo.takevoice().lower()
        query_match = find.matching(query)
        if int(query_match)==2:
            speak_now.speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            speak_now.speak("According to wikipedia")
            print(result)
            speak_now.speak(result)

        elif 'open youtube' in query:
            speak_now.speak('let me open youtube for you')
            webbrowser.open("www.youtube.com")
            in_process = 1
        elif 'in youtube' in query:
            query = query.replace("in youtube", "")
            query = query.replace("search", "")
            webbrowser.open(youtube_url + query)
            in_process = 1
        elif 'open google' in query:
            speak_now.speak('here is your google')
            webbrowser.open("www.google.com")
            in_process = 1

        elif int(query_match)==4:
            speak_now.speak('opening facebook for you')
            webbrowser.open("www.facebook.com")
            in_process = 1

        elif int(query_match)==0:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak_now.speak("Sir the time is")
            speak_now.speak(strTime)
        elif 'jarvis are you there' in query:
            speak_now.speak("At your service sir...")
        elif int(query_match)==27:
            speak_now.speak("Bye sir have a good day")
            break
        elif 'hi jarvis' in query:
            message = ['yes sir', 'hello sir', 'hi sir']
            speak_now.speak(random.choice(message))
        elif int(query_match)==5:
            speak_now.speak("Please tell me the name of the city")
            while True:
                city = takevo.takevoice().lower()
                url = url_start + city + url_end
                json_data = requests.get(url).json()
                try:
                    weather = json_data['weather'][0]['main']
                    temp_max = str(int(json_data['main']['temp_max']) / 10)
                    temp_min = str(int(json_data['main']['temp_min']) / 10)
                    temp = str(int(json_data['main']['temp']) / 10)
                    humidity = str(int(json_data['main']['humidity']))
                    cloud = str(json_data['clouds']['all'])
                    wind_speed = str(json_data['wind']['speed'])
                    print(wind_speed)
                    concat = "today in"+city+"there will be"+weather+"temperature is"+temp+"max temperature is"+temp_max+\
                          "and min temperature is"+temp_min+"today humidity is"+humidity+"wind speed is"+wind_speed+\
                          "sky is"+cloud+"% cloudy"
                    speak_now.speak(concat)
                    break
                except:
                    speak_now.speak("city is not found")
                    speak_now.speak("please tell me the correct name of the city")


        elif ('open a file' in query) or ('close a file' in query):
            '''file()
            f_location = 'explorer C:'
            a = '\\'
            while True:
                if 'open' in query:
                    speak("Which file do you want to open?")
                    take_name = takevoice().lower()
                    f_name = take_name.replace('open', '')
                    file = f_location+a+f_name
                    try:
                        os.system(file)
                        f_location = file
                    except:
                        speak("Tell me the specific name of the file")
                elif 'close' in query:
                    speak("Tell me the extension of that file")
                    ex_name = takevoice().lower()
                    ex_name = ex_name.replace('close', '')
                    ex_location = 'TASKKILL /F /IM notepad.'
                    ext = ex_location+ex_name
                    try:
                        os.system(ext)
                    except:
                        speak("Tell me the specific extension of the file")
                elif 'go back' in query:
                    break
                query = takevoice().lower()

            os.system('explorer C:\\{}'.format(query.replace('open', '')))'''

        elif int(query_match)==6:
            img = screen_short.take()
            speak_now.speak("Screenshot is clicked")
        elif int(query_match)==22:
            try:
                screen_short.show(img)
            except:
                speak_now.speak("Screen short is not clicked")
        elif int(query_match)==7:
            speak_now.speak("Whats the name of the group or person")
            name = takevo.takevoice().lower()
            speak_now.speak("Whats the message for him")
            msg = takevo.takevoice().lower()
            whatsapp.whatsapp(name, msg)
            speak_now.speak("Message send successfully")
            in_process = 1

        elif int(query_match)==8:
            news_report.news_report()
            in_process = 1
        elif 'open gmail' in query:
            speak_now.speak('opening gmail....please wait sir')
            webbrowser.open("www.gmail.com")

        elif 'set an alarm' in query:
            set_time, reminder = alarm_clock.set()
            print(set_time)
            alarm_set = 1
        elif int(query_match)==9:
            speak_now.speak('opening....please wait')
            webbrowser.open("www.instagram.com")
            in_process = 1

        elif int(query_match)==10:
            speak_now.speak('opening....please wait')
            webbrowser.open("www.twitter.com")
            in_process = 1

        elif int(query_match)==23:
            speak_now.speak('playing....please wait')
            music_dir = 'C:/songs/'
            music = os.listdir(music_dir)
            random_music = random.choice(music)
            speak_now.speak('okay,here is your music! Enjoy!')
            os.startfile(music_dir + random_music)
            in_process = 1
        elif int(query_match)==16:
            if(os.system("taskkill /im vlc.exe")==0):
                speak_now.speak("Music is stop successfully....")
                in_process = 0
            else:
                speak_now.speak("Music is not playing....")

        elif int(query_match)==11:
            pyautogui.typewrite(["volumeup"])

        elif int(query_match)==12:
            pyautogui.typewrite(["volumedown"])
        elif int(query_match)==14:
            method.WmiSetBrightness(50, 0)
        elif int(query_match)==13:
            method.WmiSetBrightness(100, 0)
        elif "restart your system" in query:
            os.system("shutdown /r /t 1")
        elif "sleep your system" in query:
            os.system("shutdown /s /t 1")
        elif int(query_match)==15:
            speak_now.speak("What is your language")
            my_voice = takevo.takevoice().lower()
            speak_now.speak("which language do you want")
            translate_voice = takevo.takevoice().lower()
            speak_now.speak("please say")
            vo = takevo.takevoice().lower()
            k = translate.translate_this(my_voice,translate_voice,vo)
            speak_now.speak(k)
        elif "mute sound" in query or "unmute sound" in query:
            pyautogui.typewrite(["volumemute"])
        elif 'what do you like' in query:
            message = ['anything related information','general knowledge','depends on my mood']
            speak_now.speak(random.choice(message))
        elif 'how you born' in query:
            speak_now.speak('I was born when four bright, intellengent and creative minds students comes together at'
                  ' Apc Roy Polytecnic College to make a assistant just for you')
        elif 'how smart are you' in query:
            speak_now.speak('It might seem like i am smart, but i am just a search enthusiast')
        elif 'who is your creator' in query:
            speak_now.speak('I was created by four student : Abhishek Das , Sourab Maity, Rudra Pratap Kamillya,Saikat Roy')
        elif 'How tall are you' in query:
            speak_now.speak('If you printed out all my code and stacked it up, i think it could get pretty long')
        elif 'how much do you weight' in query:
            speak_now.speak('That depends mostly on what devices i am on. Software is prttey lightweight by it shelf')
        elif 'do you have a girlfriend' in query:
            speak_now.speak('as you know ,i am a A.I. i would love to find a special A.I. friend')
        elif 'do you have a crush' in query:
            speak_now.speak('I try to avoid crushes and crashes')
        elif 'nice to meet you' in query:
            speak_now.speak('same here')
        elif 'are you in love' in query:
            speak_now.speak('I am in love with searching things for you')
        elif 'what is ai' in query:
            speak_now.speak('artificial intelligence (AI), sometimes called machine intelligence, is intelligence'
                  ' demonstrated by machines, in contrast to the natural intelligence displayed by humans')
        elif int(query_match)==24:
            b = psutil.sensors_battery()
            print(b.percent)  # battery parsentage
            print(b.power_plugged)  # charging or not using cable
            p = "your battery is "+str(b.percent)+"percent charged"
            speak_now.speak(p)
        elif int(query_match)==25:
            selected_speak.select_speak()
        elif int(query_match)==26:
            pyautogui.hotkey('Alt', 'F4')
            in_process = 0
        #else:
            #webbrowser.open(google_url + query)



   