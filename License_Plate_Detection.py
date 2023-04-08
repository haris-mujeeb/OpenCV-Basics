import cv2 as cv

numberPlateCascade = cv.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")

# image = cv.imread('Resources/majid.jpg')

cameraCapture = cv.VideoCapture(1)
cameraCapture.set(3,640) # Width
cameraCapture.set(4,480) # Height

success, frame = cameraCapture.read()
while success:
    success, image = cameraCapture.read()
    imageGray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    plate = numberPlateCascade.detectMultiScale(imageGray, 1.1, 4)
    for (x,y,w,h) in plate:
        cv.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)
    cv.imshow("Result", image)
    cv.waitKey(1)