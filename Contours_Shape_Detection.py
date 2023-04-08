from turtle import Turtle
import cv2 as cv 
import numpy as np


def getContours(image):
    contours, hierarchy = cv.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        print(area)
        if area>500:
            cv.drawContours(imageContour, cnt, -1, (255,0,0), 3)
            perimeter = cv.arcLength(cnt, True)
            print(perimeter)
            approx = cv.approxPolyDP(cnt, 0.02*perimeter, True)
            print(len(approx))
            objectCorner = len(approx)
            x, y, w, h = cv.boundingRect(approx)
            
            if objectCorner == 3: objectType = "Tri"
            elif objectCorner == 4: 
                    aspectRatio = w/float(h)
                    if aspectRatio>0.95 and aspectRatio<1.05: objectType = "Square"
                    else: objectType= "Rectangle"
            elif objectCorner>4: objectType= "Circle"
            else: objectType= "None"

            cv.rectangle(imageContour, (x,y),(x+w, y+h), (0, 255, 0), 2)
            cv.putText(imageContour, objectType, 
                                (x+(w//2)-10, y+(h//2)-10), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,155,155), 2)             

image = cv.imread("Resources/shapes.png")
imageContour = image.copy()
imageGray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
imageBlur = cv.GaussianBlur(imageGray, (7,7), 1)
imageCanny = cv.Canny(imageBlur, 50, 50)
getContours(imageCanny)

cv.imshow("original", image)
cv.imshow("gray", imageGray)
cv.imshow("blur", imageBlur)
cv.imshow("canny", imageCanny)
cv.imshow("contour", imageContour)



cv.waitKey(0)