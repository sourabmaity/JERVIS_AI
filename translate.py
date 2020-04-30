'''from selenium import webdriver
import time
import pyautogui
def translate_this(my_voice,translate_voice,vo):

    driver = webdriver.Chrome("C:/Users/sourab/Desktop/jervis/chromedriver.exe")
    driver.get("https://translate.google.co.in/")
    k = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]")
    k.click()
    k = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[1]/div[1]/div[3]/input")
    / html / body / div[2] / div[2] / div[3] / div / div[2] / div[1] / div[1] / div[3] / input
    k.send_keys(my_voice)   # change it asper the language you say
    pyautogui.typewrite(["enter"])
    p = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[3]")
    p.click()
    p=driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[2]/div[1]/div[3]/input")
    p.send_keys(translate_voice)  # change the language you want
    pyautogui.typewrite(["enter"])
    c=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/textarea")
    c.click()
    pyautogui.typewrite(vo) # what you want to say
    pyautogui.typewrite(["enter"])
    time.sleep(1)
    c=driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[3]/div[1]")
    return (c.text)


translate_this("english","bangla","who are you")'''
from gtts import gTTS
#from google_speech import Speech
language_dict = {
    "afrikaans":"af",
    "albanian":"sq",
}
print(language_dict['cot'])
'''from googletrans import Translator
translator = Translator()
k = translator.translate("who are you", dest='bengali')
p = gTTS(k.text,lang='bn-IN')
p.save("translate.mp3")'''
