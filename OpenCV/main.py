import numpy as np
import cv2

# Image

image = cv2.imread('images/image.jpg')

image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))
image = cv2.GaussianBlur(image, (9, 9), 0)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image = cv2.Canny(image, 100, 100)

kernel = np.ones((5, 5), np.uint8)
image = cv2.dilate(image, kernel, iterations=1)

image = cv2.erode(image, kernel, iterations=1)

cv2.imshow('Photo', image)
cv2.waitKey(0)


#Video

# capture = cv2.VideoCapture('video/video.mp4')

# Connect web camera and set width and height
capture = cv2.VideoCapture(0)
capture.set(3, 400)
capture.set(4, 300)

while True:
    success, frame = capture.read()
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) and 0xff == ord('q'):
        break

