import numpy
import cv2
import cv2.aruco as aruco
def extractaruco():
    img = cv2.imread("C:/Users/Maity Gini Palace/Desktop/shape123.jpg")
    img2 = img[0:425, 0:425, :]
    cv2.imshow('io',img2)
    gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

    ret, th = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    cv2.imshow('crop1',th)
    cv2.waitKey(0)

    _,contours, hierarchy = cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0]
    epsilon = 0.1*cv2.arcLength(contours,True)
    approx = cv2.approxPolyDP(contours,epsilon,True)
    image_crop = gray[approx[0,0,1]:approx[2,0,1],approx[0,0,0]:approx[2,0,0]]
    cv2.imshow('pading1',image_crop)
    cv2.waitKey(0)

    #cv2.imshow('crop',image_crop)
    #im = extractaruco(image_crop)
    cr = cv2.resize(image_crop,(700,700))
    cv2.imshow('12',cr)
    cv2.waitKey(0)
    cr1 = cr.shape[0]
    print(cr1)
    #im = cv2.resize(image_crop,(MAX_SIZE,MAX_SIZE))
    width =int(cr1/ 7)
    print(width)
    #area = (width,width,width,width)
    im = cr[width:width*6,width:width*6]
    cv2.imshow('pading',im)
    cv2.waitKey(0)
    ret_val = 0
    for y in range(5):
        _val1 = int(im[(y*width)+(width/2),width+width/2])
        _val2 = int(im[(y*width)+(width/2),3*width+width/2])
        if _val1 == 255:
            _val1=1
        if _val2 == 255:
            _val2 = 1
        ret_val = ret_val*2+_val1
        ret_val = ret_val*2+_val2
    print(ret_val)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    extractaruco()