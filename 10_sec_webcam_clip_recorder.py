import cv2
print("Package Imported")

# Capturing frames from a webcam
cameraCapture = cv2.VideoCapture(1)
cameraCapture.set(3,640) # Width
cameraCapture.set(4,480) # Height

fps_assumed = 30 # an assumption
fps = cameraCapture.get(cv2.CAP_PROP_FPS)
size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
           int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = cv2.VideoWriter_fourcc('I','4','2','0')
videoWriter = cv2.VideoWriter('MyWebcamVideo.avi', fourcc, fps, size)

# Capturing and Previewing 10 second webcam clip
success, frame = cameraCapture.read()
numFramesRemaining = 10 * fps - 1
while success and numFramesRemaining > 0:
    success, frame = cameraCapture.read()
    cv2.imshow("Webcam", frame)
    videoWriter.write(frame)
    numFramesRemaining -= 1
    if cv2.waitKey(5) == 27: # Delay is intentional, otherwise refresh rate is too high to view anything
        break


