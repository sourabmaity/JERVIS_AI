import cv2
import numpy as np
import math
import cv2.aruco as aruco
max_size = 406
def extractaruco(img,image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('120',gray)
    cv2.waitKey(0)
    x4, y4, w1, h1 = cv2.boundingRect(gray)
    print(w1)
    print(h1)
    '''ret, th = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    _,contours, hierarchy = cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow('567',th)
    cv2.waitKey(0)
    contours = contours[0]
    epsilon = 0.1 * cv2.arcLength(contours, True)
    approx = cv2.approxPolyDP(contours, epsilon, True)
    image_crop = gray[approx[0, 0, 1]:approx[2, 0, 1], approx[0, 0, 0]:approx[2, 0, 0]]
    cv2.imshow('crop', image_crop)
    cv2.waitKey(0)'''
    gray = image
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)
    parameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    #gray = aruco.drawDetectedMarkers(gray, corners)
    x = int(corners[0][0][0][0])
    y = int(corners[0][0][0][1])
    x1 = int(corners[0][0][1][0])
    y1 = int(corners[0][0][1][1])
    x2 = int(corners[0][0][2][0])
    y2 = int(corners[0][0][2][1])
    x3 = int(corners[0][0][3][0])
    y3 = int(corners[0][0][3][1])
    w = x1-x
    h = y2-y1
    cv2.putText(gray,"%i"%ids,(int(x+w/2+5),int(y+h/2+5)), cv2.FONT_HERSHEY_SIMPLEX,0.4,(140, 140, 140),thickness=1)
    cv2.line(gray,(int(x+w/2),int(y)),(int(x+w/2),int(y+h/2)),(127, 127, 127),thickness=1)
    cv2.circle(gray,(int(x+w/2),int(y+h/2)),2,(140, 140, 140),thickness=4)
   #aruco.drawAxis(gray,0.1)
    #gray2 = cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)
    x5 = int(x+w/2)
    y5 = int(y+h/2)
    a = int(math.sqrt(int(math.pow(w1-x4, 2)+int(math.pow(h1-h1, 2)))))
    b = int(math.sqrt(int(math.pow(w1-x5, 2)+int(math.pow(h1-y5, 2)))))
    c =int(math.sqrt(int(math.pow(x5-x4, 2)+int(math.pow(y5-h1, 2)))))
    angle = math.acos(int((math.pow(c,2)+math.pow(b,2)-math.pow(a,2))/(2*b*c)))
    angle1 = int(angle*180/math.pi)
    cv2.putText(gray,"%i"%angle1,(int(x+w/2-27),int(y+20)), cv2.FONT_HERSHEY_SIMPLEX,0.4,(140, 140, 140),thickness=1)
    print(angle1)
    print(a)
    print(b)
    print(c)
    print(angle)
    print(ids)
    cv2.imshow('789',gray)
    cv2.waitKey(0)
    #gray = cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)
    #x, y, w, h = cv2.boundingRect(image_crop)
    #x1,y1,w1,h1 = cv2.boundingRect(gray)
    #gray = image
    #cv2.putText(gray,"%i"%ids,(int(x1+w1/2),int(y1+h1/2)), cv2.FONT_HERSHEY_SIMPLEX,0.4,(140, 140, 140),thickness=1)
    #gray2 = cv2.line(gray,(int(x1+w1/2),int((h1-h)/2)),(int(x1+w1/2),int(y1+h1/2)),(127, 127, 127),thickness=1)
    #gray2 = cv2.circle(gray2,(207,210),2,(140, 140, 140),thickness=4)
    rotM = np.zeros(shape=(3, 3))
    cv2.Rodrigues(corners[0][0],rotM,jacobian=0)
    ypr = cv2.RQDecomp3x3(rotM)
    #cv2.imshow('frame', gray)
    #cv2.imshow('3546',gray2)
    cv2.waitKey(0)
    print(ypr)
    print(ids)
    print(corners[0][0])
    cv2.waitKey(0)
    return image_crop
def findarucoid(inp_img,image):
    im = extractaruco(inp_img,image)
    #im = cv2.resize(im, (max_size,max_size))
    #width = int(max_size/7)
    #im = im[width:width*6,width:width*6]
    cv2.imshow('padding', im)
    cv2.waitKey(0)
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_100)
    parameters = aruco.DetectorParameters_create()
    corners,ids,rejectedimagepoint= aruco.detectMarkers(im,aruco_dict,parameters=parameters)
    print(ids)
    print(corners)
    '''ret_val = 0
    for y in range(6):
        _val1 = int(im[int((y * width)+(width / 2)), int(width+width / 2)])
        _val2 = int(im[int((y * width) + (width / 2)), int(3 * width + width / 2)])
        if _val1 == 255:
            _val1 = 1
        if _val2 == 255:
            _val2 = 1
        ret_val = ret_val * 2 + _val1
        ret_val = ret_val * 2 + _val2
    return ret_val'''
image = cv2.imread("C:/Users/APC/Desktop/shape1234.jpg")
img2 = image[0:420, 0:420, :]

cv2.imshow('000',img2)
cv2.waitKey(0)
id = findarucoid(img2,image)

cv2.waitKey(0)
cv2.destroyAllWindows()
print('marker id is',id)