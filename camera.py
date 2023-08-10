import cv2
import numpy as np

# import success as success

cap = cv2.VideoCapture(0)
# cv2.imshow('ybyiiyb', img)
#
# cv2.waitKey(0) COLOR_BGR2GRAY

# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)   конвертация слоев в дугие библиотеки

kernal = np.ones((5,5), np.uint8)



while True:
    success, img = cap.read()
    img = cv2.resize(img, (1000, 1000))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    img = cv2.Canny(img, 90, 90)
    new = np.zeros(img.shape, dtype='uint8')
    con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(new, con, -1, (100, 100, 100), 1)

    cv2.imshow("read", new)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print(con)

        break