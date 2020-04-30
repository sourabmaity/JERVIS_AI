import numpy as np
import cv2

angle1 = 360
angle2 = 0
angle3 = 150
angle4 = 250
angle5 = 90
startAngle1 = 0
startAngle2 = 0
startAngle3 = 90
startAngle4 = 180
startAngle5 = 270
endAngle1 = 180
endAngle2 = 180
endAngle3 = 360
endAngle4 = 360
endAngle5 = 360
color=(0,0,255)
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while 1:
    ret, img = cap.read()
    img2 = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            #cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            #print(ex,ey,ex+int(ew/2),ey+int(eh/2))
            if(ew>40):
                radius1 = int(ew/2+15)
                radius2 = int(ew/2+10)
                radius3 = int(ew/2+5)
                radius4 = int(ew/2)
                radius5 = int(ew/2-5)
                axes1 = (radius1, radius1)
                axes2 = (radius2, radius2)
                axes3 = (radius3, radius3)
                axes4 = (radius4, radius4)
                axes5 = (radius5, radius5)
                center=(ex+int(ew/2),ey+int(eh/2))
                cv2.ellipse(roi_color, center, axes1, angle1, startAngle1, endAngle1, color)
                cv2.ellipse(roi_color, center, axes2, angle2, startAngle2, endAngle2, color)
                cv2.ellipse(roi_color, center, axes3, angle3, startAngle3, endAngle3, color)
                cv2.ellipse(roi_color, center, axes4, angle4, startAngle4, endAngle4, color)
                cv2.ellipse(roi_color, center, axes5, angle5, startAngle5, endAngle5, color)
                angle2 = angle2+12
                angle1 = angle1-12
                angle3 = angle3-16
                angle4 = angle4+18
                angle5 = angle5-20
                if (angle5 <= 0):
                    angle5 = 360
                if(angle4 == 360):
                    angle4 = 0
                if(angle3<=0):
                    angle3 = 360
                if(angle1 == 0):
                    angle1 = 360
                    angle2 = 0
    cv2.imshow("d", img)
    k = cv2.waitKey(30) & 0xff
    if k == 113:
        break


cap.release()
cv2.destroyAllWindows()


