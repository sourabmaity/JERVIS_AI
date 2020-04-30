'''from selenium import webdriver
import time
import pyautogui
gmail_id = "maitysourab@gmail.com"
gmail_pw = "9874116071"
driver = webdriver.Chrome("C:/Users/sourab/Desktop/jervis/chromedriver.exe")
driver.get("https://duo.google.com")
s = driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/div[1]/a")
s.click()
s = driver.find_element_by_xpath('//*[@id="identifierId"]')
s.send_keys(gmail_id)
s = driver.find_element_by_xpath('//*[@id="identifierNext"]')
s.click()
while(1):
    try:
        s = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        s.send_keys(gmail_pw)
        break
    except:
        continue
s = driver.find_element_by_xpath('//*[@id="passwordNext"]')
s.click()'''
'''import pyautogui
from selenium import webdriver
k=pyautogui.middleClick(1013,1052)
#driver = webdriver.Chrome("C:/Users/sourab/Desktop/jervis/chromedriver.exe")
s = webdriver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[3]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[1]/input')
s.send_keys("abhishek das")'''
'''import geocoder
g = geocoder.ip('me')
print(g.latlng)'''
'''import requests
import json

send_url = "http://api.ipstack.com/check?access_key=abc2a7e460d4affeb7f9788f5361769f"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
city = geo_json['city']
print(city)
print(latitude)
print(longitude)
print(geo_json)'''
import fb
token = "EAAG2PCCsBz4BAL9ZCUQramIyDTurXMnB4TROwRN8jLxTRB9VM2IJu8dM2PfUcZAAA7BYMgxuUeHWFxHF7n4elYHVTL5YY6XYsH5A3KgFSzO02B" \
        "4qQASt20MQwlFOjW7pciYbxNSqXYeQxXBJcAx9WLMg593JTdAo4F2hXXxtSNB6TJn3NuQoYXjsJnYJ9yGJjy9IwupScUYJjl9KdP"
facebook = fb.graph.api(token)
facebook.publish(cat="feed", id="me", message="my facebook status")
