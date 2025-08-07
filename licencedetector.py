import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"


#reading the image from the directory
img = cv2.imread("car2.jpg")
cv2.imshow("Original",img)

#converting into grayscale 
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayImage",gray_img)

#extracting the corner using canny edge extraction
canny_img = cv2.Canny(gray_img,170,200)
cv2.imshow("Canny image",canny_img)


#Finding all the contors in the image 
contours,new = cv2.findContours(canny_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#reversing the contours so that we can find only the contour with maximum contour to find the number plate
contours = sorted(contours,key=cv2.contourArea,reverse=True)[:30]

#initializing the variables
contour_with_licence_plate = None
license_plate = None
(x,y,w,h) = (None,None,None,None)


contour_img = img.copy()
cv2.drawContours(contour_img,contours,-1,(0,255,0),1)
cv2.imshow("Contour image",contour_img)


#finding the contour with polygon shape i.e enclosed shape
for c in contours:
    perimeter = cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,0.01*perimeter,True)
    print("approx : %d" %(len(approx)))
    if len(approx) == 4 :
        contour_with_licence_plate = approx
        (x,y,w,h) = cv2.boundingRect(c)
        license_plate = gray_img[y:y+h,x:x+w]
        cv2.imshow("Number Plate cropped",license_plate)
        
        break
    
thresh,license_plate = cv2.threshold(license_plate,127,255,cv2.THRESH_BINARY)

#removing the noise from the plate
license_plate = cv2.bilateralFilter(license_plate,11,17,17)

text = pytesseract.image_to_string(license_plate)
cv2.rectangle(img,(x,y),(x+w,y+h),(122,122,0),2)
cv2.putText(img,text,(x-100,y-20),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
cv2.imshow("FInal Image",img)

print(text)
       

cv2.waitKey(0)
