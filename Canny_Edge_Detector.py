import cv2 as cv
import numpy as np

image = cv.imread("Resources/majid2.jpg")
imageGray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
imageBlur = cv.GaussianBlur(imageGray, (9,9), 0)    # Kernel is defined to be 5x5
                                                    # SigmaX is 0
# Canny Edge Detector
imageCanny = cv.Canny(image, 100, 100)

# Increasing the thickness to join any unconnected line
kernel = np.ones((5,5), np.uint8)
imageDilation = cv.dilate(imageCanny, kernel, iterations=1)

# Decreasing the thickness to join any unconnected line
imageEroded = cv.erode(imageDilation, kernel, iterations=1)

cv.imshow("Gray Image", imageGray)
cv.imshow("Blured Image", imageBlur)
cv.imshow("Canny Image", imageCanny)
cv.imshow("Dilation Image", imageDilation)
cv.imshow("Eroded Image", imageEroded)
cv.waitKey(0)