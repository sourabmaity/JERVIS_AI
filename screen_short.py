import pyautogui
import cv2
import os

def take():
    img = pyautogui.screenshot()
    img.save("C:/Users/sourab/Desktop/jervis/screenshot.png")
    return img

def show(img):
    img.show()
