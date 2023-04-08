import cv2 as cv

faceCascade = cv.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

image = cv.imread('Resources/friends.jpg')
imageGray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imageGray, 1.1, 4)
for (x,y,w,h) in faces:
    cv.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)

image = cv.resize(image, (640, 640)) # resize to 300 width and 200 height

cv.imshow("Result", image)
cv.waitKey(0)


# cameraCapture = cv.VideoCapture(1)
# cameraCapture.set(3,640) # Width
# cameraCapture.set(4,480) # Height

# success, frame = cameraCapture.read()
# while success:
#     success, image = cameraCapture.read()
#     imageGray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#     faces = faceCascade.detectMultiScale(imageGray, 1.1, 4)
#     for (x,y,w,h) in faces:
#         cv.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 2)
#     cv.imshow("Result", image)
#     cv.waitKey(1)