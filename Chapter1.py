import cv2
print("Package Imported")

image = cv2.imread("resources/haris.jpg")   # the name is not case sensitve
cv2.imshow("Output",image)
cv2.waitKey(1000)   # in milli-seconds, while zero means infinte delay


# Playing Video
videoCapture = cv2.VideoCapture("resources/majid.mp4") # Creating a video capture object

success, img = videoCapture.read()
scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

while success:
    img = cv2.flip(img, 0)
    cv2.resize(img ,dim ,interpolation = cv2.INTER_AREA)
    cv2.imshow("Video", img)
    # press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    success, img = videoCapture.read()

# Saving/Writing a new video fule
videoCapture = cv2.VideoCapture("resources/majid.mp4")
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc('I','4','2','0')
videoWriter = cv2.VideoWriter('MyOutputVideo.avi',fourcc ,fps ,size)

success, img = videoCapture.read()
# while loop to go through each frame one by one
while success:
    videoWriter.write(img)
    success, frame = videoCapture.read()


