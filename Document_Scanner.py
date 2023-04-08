import cv2 as cv
import numpy as np

#############################

widthImage = 640
heightImage = 480 

#############################

faceCascade = cv.CascadeClassifier("Resources/Friends.xml")

# image = cv.imread('Resources/majid.jpg')

cameraCapture = cv.VideoCapture(1)
cameraCapture.set(3,widthImage) # Width
cameraCapture.set(4,heightImage) # Height

def preProcessing(image):
    imageGray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    imageBlur = cv.GaussianBlur(imageGray, (5,5), 0)
    imageCanny = cv.Canny(imageBlur, 50, 50)
    # cv.imshow("c", imageGray)
    # cv.imshow("blur", imageBlur)
    cv.imshow("canny", imageCanny)
    # improving edges
    kernel = np.ones((5,5), np.uint8)
    imageDilation = cv.dilate(imageCanny, kernel, iterations=3)
    imageThres = cv.erode(imageDilation, kernel, iterations=1)
    # cv.imshow("dia", imageDilation)
    cv.imshow("thres", imageThres)

    
    return imageThres


def getContours(image):
    biggestContour = np.array([])
    maxArea = 0
    contours, hierarchy = cv.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        print(area)
        if area>5000:
            # cv.drawContours(imageContour, cnt, -1, (255,0,0), 3)
            perimeter = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02*perimeter, True)
            if area>maxArea and len(approx)==4: 
                biggestContour = approx # 4 points of the biggest rectangle
                maxArea = area 
    cv.drawContours(imageContour, biggestContour, -1, (255,0,0), 20)
    return biggestContour
            # objectCorner = len(approx)
            # x, y, w, h = cv.boundingRect(approx)

def reorderPoints(myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsReordered = np.zeros((4,1,2), np.int32)
    add = myPoints.sum(1)
    myPointsReordered[0] = myPoints[np.argmin(add)]
    myPointsReordered[3] = myPoints[np.argmax(add)]

    diff = np.diff(myPoints, axis=1)
    myPointsReordered[1] = myPoints[np.argmin(diff)]
    myPointsReordered[2] = myPoints[np.argmax(diff)]
    print(myPointsReordered)
    return myPointsReordered


def getWarp(image, biggestContour):
    biggestContour = reorderPoints(biggestContour)
    pts1 = np.float32(biggestContour)
    pts2 = np.float32([[0,0],[widthImage,0], [0,heightImage], [widthImage, heightImage]])
    matrix = cv.getPerspectiveTransform(pts1,pts2)
    imageOutput = cv.warpPerspective(image, matrix, (widthImage, heightImage))
    
    imageCropped = imageOutput[20:imageOutput.shape[0]-20, 20:imageOutput.shape[1]-20]
    return imageCropped


success, frame = cameraCapture.read()
while success:
    success, image = cameraCapture.read()
    image = cv.resize(image, (widthImage, heightImage))
    imageContour = image.copy()
    imageThreshold = preProcessing(image=image)
    biggestContour = getContours(imageThreshold)
    try:
        warpedImage = getWarp(image, biggestContour)
    except:
        pass
    cv.imshow("Contour", imageContour)
    cv.imshow("Result", warpedImage)
    cv.waitKey(1)

