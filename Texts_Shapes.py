import cv2 as cv
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)
print(image.shape)
image[:] = 155, 100, 100

cv.line(image, (0,0), (image.shape[1],image.shape[0]), (0,255,0), 3)
cv.rectangle(image, (0,0), (250,350), (0,0,255, 2), cv.FILLED)
cv.circle(image, (400,50), 30, (255,255,0), 5)
cv.putText(image, "OPENCV ", (200, 400), cv.FONT_HERSHEY_COMPLEX,1, (0,150,0), 3)


cv.imshow("image", image)

cv.waitKey(0)