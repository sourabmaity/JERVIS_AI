#whatsapp message send
#using all_name = [raja,pigus,tom]
from selenium import webdriver
import time
import speak_now
#print("wkvkwv")
#from selenium.webdriver.common.keys import Keys
def whatsapp(name, msg):
    driver = webdriver.Chrome('C:/Users/sourab/Desktop/jervis/chromedriver.exe')
    driver.get('https://web.whatsapp.com/')
    speak_now.speak("Please check that QR code is scanned")
    input("")
    #user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))  # for loop before it name in all_name
    user = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/input')
    user.send_keys(name)
    time.sleep(1)
    select = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div/div')
    select.click()
    msg_box = driver.find_element_by_class_name('_13mgZ')
    # for r in range(0,100):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
    time.sleep(1)
    return

