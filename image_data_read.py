import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'
img = cv2.imread("C:/Users/sourab/Desktop/jervis/admission-form-1-725x1024.jpg")
text = pytesseract.image_to_data(img)
print(text)