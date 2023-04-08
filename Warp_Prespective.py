from turtle import width
import cv2 as cv 
import numpy as np

image = cv.imread("Resources/cards.jpg")

width, height = 250,350
pts1 = np.float32(([111,219],[287,188],[154,482],[352,440]))
pts2 = np.float32(([0,0],[width,0], [0,height], [width, height]))
matrix = cv.getPerspectiveTransform(pts1,pts2)
imgOutput = cv.warpPerspective(image, matrix, (width, height))



cv.imshow("cards.jpg", image)
cv.imshow("Output", imgOutput)

cv.waitKey(0)