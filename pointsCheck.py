import cv2
import mediapipe as mp
import gestures

class Validator:
	@staticmethod
	def isInt(str):
		try:
			int(str)
		except ValueError:
			return False
		
		return True
	
	@staticmethod
	def isNaturalInt(str):
		if Validator.isInt(str) and int(str) > 0:
			return True
		
		return False

cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands(max_num_hands=1)
draw = mp.solutions.drawing_utils

windowName = "Points Check"

point1 = 0
point2 = 0
while True:
	success, image = cap.read()
	image = cv2.flip(image, 1)
	results = hands.process(image)

	if results.multi_hand_landmarks:
		for handLms in results.multi_hand_landmarks:
			if point1 != point2:
				print(gestures.getPointsAngle(handLms.landmark[point1], handLms.landmark[point2]))

			draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)

	cv2.imshow(windowName, image)


	keyCode = cv2.waitKey(1)
	if keyCode == 13:
		while True:
			print('Введите 1-ую точку: ', end = '')
			point1 = input()
			print()

			if Validator.isNaturalInt(point1):
				point1 = int(point1)
				break

		while True:
			print('Введите 2-ую точку: ', end = '')
			point2 = input()
			print()

			if Validator.isNaturalInt(point2):
				point2 = int(point2)
				break

	if cv2.getWindowProperty(windowName, cv2.WND_PROP_VISIBLE) < 1 or keyCode == 113 or keyCode == 233 or keyCode == 81 or keyCode == 201:
		break

cap.release()
cv2.destroyAllWindows()