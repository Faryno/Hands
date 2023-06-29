import cv2
import numpy as np

photo = np.zeros((500, 500, 3), dtype='uint8')

# photo[200:500, 200:280] = 64, 235, 52

# cv2.rectangle(photo, (0, 0), (400, 200), (64, 235, 52), thickness=cv2.FILLED)

cv2.line(photo, (0, 0), (photo.shape[1] // 2, photo.shape[0] // 2), (64, 235, 52), thickness=3)

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 250, (64, 235, 52), thickness=cv2.FILLED)

cv2.putText(photo, 'bvvctctuyivlhvftjjvgcgfugjhjfyu', (0, 100), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0))

cv2.imshow("Photo",photo)
cv2.waitKey(0)