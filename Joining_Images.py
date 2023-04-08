import cv2 as cv 
import numpy as np

image = cv.imread("Resources/obama.jpg")

horizontal = np.hstack((image, image))
vertical = np.vstack((image, image))

cv.imshow("h", horizontal)
cv.imshow("v", vertical)

cv.waitKey(0)