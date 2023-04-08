import cv2 as cv

image = cv.imread("Resources/Majid.jpg")
print(image.shape) # 'shape' method gives -> ( height, width, no. of channels)

imageResize = cv.resize(image, (640, 480)) # resize to 300 width and 200 height
print((imageResize.shape))

imageCrop = image[100:700, 1300:2000]


cv.imshow("Image", image)
cv.imshow("Image Resized", imageResize)
cv.imshow("Image Cropped", imageCrop)

cv.waitKey(0)

