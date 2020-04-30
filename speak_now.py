import pyttsx3
engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
#print(voice)
engine.setProperty('voice',voice[0].id)
#print(voice[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()




