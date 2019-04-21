# url : https://developer.ibm.com/tutorials/document-scanner/
# url : https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes
# url : https://medium.com/@MicroPyramid/extract-text-with-ocr-for-all-image-types-in-python-using-pytesseract-ec3c53e5fc3a

# pdf to png converter
#import cv2

#img = cv2.imread("output_image.png", 0)
#ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_OTSU)
#print("Threshold selected : ", ret)
#cv2.imwrite("output_image1.png", thresh)

from PIL import Image
import PIL.Image

from pytesseract import image_to_string
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract'
TESSDATA_PREFIX = 'C:/Program Files/Tesseract-OCR'
output = pytesseract.image_to_string(PIL.Image.open('test1.PNG').convert("RGB"), lang='eng')
print(output)
f = open("outfile.txt", "w")
f.write(output)
f.write("\n")
f.close()

