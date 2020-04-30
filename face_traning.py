import cv2
import os
import numpy as np
face__haar_cascade = cv2.CascadeClassifier("C:/Users/sourab/Desktop/jervis/haarcascade_frontalface_default.xml")
def faceDetection(test_img):
    gimage=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
    #cv2.imshow("jjv",gimage)

    face = face__haar_cascade.detectMultiScale(gimage,scaleFactor=1.3, minNeighbors=5)
    return face,gimage

def traning_data(directory):
    faces=[]
    faceID=[]
    for path,subdirnames,filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."):
                print("Skipping system file")#Skipping files that startwith .
                continue

            id=os.path.basename(path)#fetching subdirectory names
            img_path=os.path.join(path,filename)#fetching image path
            print("img_path:",img_path)
            print("id:",id)
            test_img=cv2.imread(img_path,cv2.IMREAD_UNCHANGED)#loading each image one by one
            test_img = cv2.resize(test_img, (600, 600), interpolation=cv2.INTER_AREA)
            if test_img is None:
                print("Image not loaded properly")
                continue
            faces_rect,gray_img=faceDetection(test_img)#Calling faceDetection function to return faces detected in particular image
            if len(faces_rect)!=1:
                os.remove(img_path)
                continue #Since we are assuming only single person images are being fed to classifier
            (x,y,w,h)=faces_rect[0]
            roi_gray=gray_img[y:y+w,x:x+h]#cropping region of interest i.e. face area from grayscale image
            #cv2.imshow("cbf",roi_gray)
            #cv2.waitKey(0)
            faces.append(roi_gray)
            faceID.append(int(id))
    return faces,faceID
def train_classifier(faces,faceID):
    face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces,np.array(faceID))
    return face_recognizer


def draw_rect(test_img,face):
    (x,y,w,h)=face
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=5)


def put_text(test_img,text,x,y):
    cv2.putText(test_img,text,(x,y),cv2.FONT_HERSHEY_DUPLEX,2,(255,0,0),4)
facess,faceid=traning_data("C:/Users/sourab/Desktop/jervis/image_me/")##
face_re=train_classifier(facess,faceid)
face_re.save("traning_data.yml")
name={0:"Sourab",
      1:"Rudra",
      2:"Abhishek"}
cv2.waitKey(0)#Waits indefinitely until a key is pressed
cv2.destroyAllWindows()

