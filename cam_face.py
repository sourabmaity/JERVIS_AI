import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier("C:/Users/sourab/Desktop/jervis/haarcascade_frontalface_default.xml")
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
name={0:"Sourab",
      1:"Rudra",
      2:"Abhishek"}
face_recognizer.read("C:/Users/sourab/Desktop/jervis/traning_data.yml")
matched_time = 0
match_id = 0
def face_matching():
    global matched_time
    global match_id
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # gray_img = cv2.resize(gray_img, (600, 600), interpolation=cv2.INTER_AREA)
        face = face_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), thickness=5)
        for fac in face:
            (x, y, w, h) = fac
            roi_gray = gray_img[y:y + h, x:x + h]
            label, confidence = face_recognizer.predict(roi_gray)  # predicting the label of given image
            print("confidence:", confidence)
            print("label:", label)
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), thickness=5)
            predicted_name = name[int(label)]
            if (confidence > 50):  # If confidence more than 37 then don't print predicted face text on screen
                continue
            if(match_id==label):
                matched_time = matched_time+1
                if matched_time==5:
                    cap.release()
                    cv2.destroyAllWindows()
                    return
            else:
                matched_time = 0
            cv2.putText(img, predicted_name, (x, y), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 4)
        cv2.imshow("faces", img)
        k = cv2.waitKey(1) & 0xff
        if k == 113:
            break

    cap.release()
    cv2.destroyAllWindows()

face_matching()