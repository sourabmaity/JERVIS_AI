'''from threading import *
import speak_now
#import jervis
import takevo
import time
def new():
    #speak_now.speakf("jchgc")
    for x in range(10):
        speak_now.speakf("jchgc")
        print("scnbacj")
        time.sleep(1)
def hi():

    for x in range(10):
        takevo.takevoice()
        time.sleep(1)
t1=Thread(target=new)
t2=Thread(target=hi)
t1.start()
t2.start()
print("hbjb")'''
import os
os.add_dll_directory(r'C:\Program Files (x86)\VideoLAN\VLC')
import vlc
player=""
def play():
    global player
    c = vlc.MediaPlayer("C:/songs/WhatsApp Audio 2020-02-13 at 12.15.48 PM (1).mpeg")
    c.play()
def pause():
    global player
    player.pause()
def stop():
    global player
    player.stop


play()