import cv2
import os
import numpy as np
max = 0
face__haar_cascade = cv2.CascadeClassifier("C:/Users/sourab/Desktop/jervis/haarcascade_frontalface_default.xml")#change the direction as per your computer
cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)
f = os.listdir("C:/Users/sourab/Desktop/jervis/image_me/0")#give the name of the folder where you store your picture
for i in f:
    k = i.find(".")
    i = i[0:k]
    if(int(i)>int(max)):
        max = i

while True:
    ret, img = cap.read()
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #gray_img = cv2.resize(gray_img, (600, 600), interpolation=cv2.INTER_AREA)
    '''face = face__haar_cascade.detectMultiScale(gray_img,scaleFactor=1.3, minNeighbors=5)
    img1=img.copy()
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),thickness=5)'''
    cv2.rectangle(img,(100,100),(50,50),(0,0,255),3)
    img2=img.copy()
    img2=img2[55:95,55:95]
    k=img2
    for i in k:
        for l in i:
            print(l[0])
    cv2.imshow("faces", img)
    cv2.imshow("pic", img2)

    '''k = cv2.waitKey(30) & 0xff
    if k == 113:
        break
    if k == 97:
        cv2.imwrite("C:/Users/sourab/Desktop/jervis/image_me/0/{}.png".format(int(max)+1),img1);#donot change /{}.png change only location of your required folder
        max = int(max)+1'''
    break

cap.release()
cv2.destroyAllWindows()










