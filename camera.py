import cv2
import numpy as np

# import success as success

cap = cv2.VideoCapture(0)
# cv2.imshow('ybyiiyb', img)
#
# cv2.waitKey(0) COLOR_BGR2GRAY

# kernal = np.ones((5,5), np.uint8)

while True:
    success, img = cap.read()
    img = cv2.resize(img, (1000, 1000))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.Canny(img, 30, 30)
    cv2.imshow("read", img)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break