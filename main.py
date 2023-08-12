import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands(max_num_hands=1)
draw = mp.solutions.drawing_utils


# def is_o_gesture(hand_landmarks):
#     y_threshold = 0.07  # Порог для определения примерной одной высоты
#     x_threshold = 0.07  # Порог для определения примерной одной высоты
#     y_positions = [hand_landmarks[i].y for i in [4, 8, 12, 16, 20]]
#     x_positions = [hand_landmarks[i].x for i in [4, 8, 12, 16, 20]]
#     min_y = min(y_positions)
#     max_y = max(y_positions)
#     min_x = min(x_positions)
#     max_x = max(x_positions)
#     if max_y - min_y < y_threshold
#        and max_x - min_x < x_threshold: return True


# def is_a_gesture(hand_landmarks):
#     y_threshold = 0.07  # Порог для определения примерной одной высоты
#     x_threshold = 0.07  # Порог для определения примерной одной высоты
#     y_positions = [hand_landmarks[i].y for i in [4, 6, 10, 14, 18]]
#     x_positions = [hand_landmarks[i].x for i in [4, 6, 10, 14, 18]]
#     min_y = min(y_positions)
#     max_y = max(y_positions)
#     min_x = min(x_positions)
#     max_x = max(x_positions)
#     if max_y - min_y < y_threshold and max_x - min_x > x_threshold: return True

# def is_b_gesture(hand_landmarks):
#     x_threshold = 0.01
#     y_threshold = 0.05
#
#     thumb_x_4 = hand_landmarks[4].x
#     index_finger_x_8 = hand_landmarks[8].x
#     middle_finger_x_12 = hand_landmarks[12].x
#     ring_finger_x_16 = hand_landmarks[16].x
#     pinky_x_20 = hand_landmarks[20].x
#
#     thumb_y_4 = hand_landmarks[4].y
#     index_finger_y_8 = hand_landmarks[8].y
#     middle_finger_y_12 = hand_landmarks[12].y
#     ring_finger_y_16 = hand_landmarks[16].y
#     pinky_y_20 = hand_landmarks[20].y
#
#     index_finger_x_7 = hand_landmarks[7].x
#     middle_finger_x_11 = hand_landmarks[11].x
#     ring_finger_x_15 = hand_landmarks[15].x
#     pinky_x_19 = hand_landmarks[19].x
#
#     index_finger_y_7 = hand_landmarks[7].y
#     middle_finger_y_11 = hand_landmarks[11].y
#     ring_finger_y_15 = hand_landmarks[15].y
#     pinky_y_19 = hand_landmarks[19].y
#
#     ring_finger_x_13 = hand_landmarks[13].x
#     ring_finger_y_13 = hand_landmarks[13].y
#     print(index_finger_y_8, index_finger_y_7)
#     if (
#         (abs(thumb_y_4 - ring_finger_y_13) < (y_threshold)) and
#         (index_finger_y_7 > index_finger_y_8) and
#         (middle_finger_y_11 > middle_finger_y_12) and
#         (ring_finger_y_15 > ring_finger_y_16) and
#         (pinky_y_19 > pinky_y_20) and
#         (abs(thumb_x_4 - ring_finger_x_13) < x_threshold) and
#         abs(index_finger_x_8 - index_finger_x_7) <= x_threshold and
#         abs(middle_finger_x_12 - middle_finger_x_11) <= x_threshold and
#         abs(ring_finger_x_16 - ring_finger_x_15) <= x_threshold and
#         abs(pinky_x_20 - pinky_x_19) <= x_threshold
#     ):
#         return True
#
#     return False

# def is_c_gesture(hand_landmarks):
#     x_threshold = 0.01
#     y_threshold = 0.05
#
#     thumb_y_4 = hand_landmarks[4].y
#     index_finger_y_8 = hand_landmarks[8].y
#     middle_finger_y_12 = hand_landmarks[12].y
#     ring_finger_y_16 = hand_landmarks[16].y
#     ring_finger_y_15 = hand_landmarks[15].y
#     pinky_y_20 = hand_landmarks[20].y
#     pyatka_y_0 = hand_landmarks[0].y
#
#     if (
#         (abs(thumb_y_4 - pyatka_y_0 <= y_threshold)) and
#         (abs(index_finger_y_8 - middle_finger_y_12 <= y_threshold)) and
#         (abs(middle_finger_y_12 - ring_finger_y_16 <= y_threshold)) and
#         (abs(ring_finger_y_15 - pinky_y_20 <= y_threshold)) and
#         (abs(index_finger_y_8 - ring_finger_y_16 <= y_threshold)) and
#         (index_finger_y_8 < pinky_y_20)
#
#     ):
#         return True
#
#     return False

# def is_d_gesture(hand_landmarks):
#     y_threshold = 0.07
#     index_finger_y_8 = hand_landmarks[8].y
#     index_finger_y_7 = hand_landmarks[7].y
#     pyatka_y_0 = hand_landmarks[0].y
#     thumb_x_4 = hand_landmarks[4].x
#     index_finger_x_8 = hand_landmarks[8].x
#     y_positions = [hand_landmarks[i].y for i in [4, 12, 16, 20]]
#     min_y = min(y_positions)
#     max_y = max(y_positions)
#     if(
#
#         (max_y - min_y < y_threshold) and
#         (index_finger_y_8 < max_y) and
#         (abs(index_finger_y_7 - index_finger_y_8 <= y_threshold) > pyatka_y_0) and
#         (thumb_x_4 >= index_finger_x_8)
#     ):
#         return True
#
#     return False

# def is_e_gesture(hand_landmarks):
#     y_threshold = 0.05
#
#     thumb_y_4 = hand_landmarks[4].y
#     thumb_x_4 = hand_landmarks[4].x
#     index_finger_y_8 = hand_landmarks[8].y
#     middle_finger_y_12 = hand_landmarks[12].y
#     ring_finger_y_16 = hand_landmarks[16].y
#     pinky_y_20 = hand_landmarks[20].y
#     index_finger_y_5 = hand_landmarks[5].y
#     middle_finger_y_9 = hand_landmarks[9].y
#     ring_finger_y_13 = hand_landmarks[13].y
#     index_finger_x_5 = hand_landmarks[5].x
#     pinky_y_17 = hand_landmarks[17].y
#
#     if (
#         (abs(index_finger_y_5 - index_finger_y_8 <= y_threshold))and
#         (abs(middle_finger_y_9 - middle_finger_y_12 <= y_threshold)) and
#         (abs(ring_finger_y_13 - ring_finger_y_16 <= y_threshold)) and
#         (abs(pinky_y_17 - pinky_y_20 <= y_threshold)) and
#         (abs(ring_finger_y_13 - thumb_y_4 <= y_threshold)) and
#         (abs(thumb_x_4 > index_finger_x_5))
#     ):
#         return True
#
#     return False

# def is_g_gesture(hand_landmarks):
#     x_threshold = 0.03
#
#     index_finger_x_8 = hand_landmarks[8].x
#     middle_finger_x_12 = hand_landmarks[12].x
#     x_positions = [hand_landmarks[i].x for i in [4, 10, 14, 18]]
#     min_x = min(x_positions)
#     max_x = max(x_positions)
#
#     if (
#         (middle_finger_x_12 < index_finger_x_8) and
#         (max_x - min_x < x_threshold)
#     ):
#         return 1
#     return False

# def is_h_gesture(hand_landmarks):
#     x_threshold = 0.07
#
#     index_finger_x_8 = hand_landmarks[8].x
#     middle_finger_x_12 = hand_landmarks[12].x
#     thumb_4 = hand_landmarks[4].x
#     x_positions = [hand_landmarks[i].x for i in [4, 10, 14, 18]]
#     min_x = min(x_positions)
#     max_x = max(x_positions)
#
#     if (
#         (middle_finger_x_12 > index_finger_x_8) and
#         (index_finger_x_8 > thumb_4) and
#         (max_x - min_x < x_threshold)
#
#     ):
#         return True
#     return False

# def is_i_gesture(hand_landmarks):
#     y_threshold = 0.05  # Порог для определения примерной одной высоты
#     x_threshold = 0.05  # Порог для определения примерной одной высоты
#     pinky_y_20 = hand_landmarks[20].y
#     pinky_y_19 = hand_landmarks[19].y
#     y_positions = [hand_landmarks[i].y for i in [4, 6, 10, 14]]
#     x_positions = [hand_landmarks[i].x for i in [4, 6, 10, 14]]
#     min_y = min(y_positions)
#     max_y = max(y_positions)
#     min_x = min(x_positions)
#     max_x = max(x_positions)
#
#
#
#     if ((max_y - min_y < y_threshold) and
#         (max_x - min_x > x_threshold) and
#         (pinky_y_19 - pinky_y_20 <= y_threshold)
#
#
#     ):
#         return True
#     return False

# def is_l_gesture(hand_landmarks):
#     y_threshold = 0.05  # Порог для определения примерной одной высоты
#     x_threshold = 0.05  # Порог для определения примерной одной высоты
#
#     thumb_y_4 = hand_landmarks[4].y
#     thumb_x_4 = hand_landmarks[4].x
#     middle_finger_y_12 = hand_landmarks[12].y
#     # ring_finger_y_14 = hand_landmarks[14].y
#     index_finger_x_8 = hand_landmarks[8].x
#     index_finger_y_8 = hand_landmarks[8].y
#     index_finger_y_7 = hand_landmarks[7].y
#     index_finger_y_5 = hand_landmarks[5].y
#
#     if (
#         (abs(index_finger_x_8 - thumb_x_4 <= x_threshold)) and
#         (abs(middle_finger_y_12 - thumb_y_4 <= y_threshold)) and
#         (abs(index_finger_y_8 - index_finger_y_7 <= y_threshold)) and
#         (abs(index_finger_y_5 - middle_finger_y_12 < y_threshold))
#
#     ):
#         return True
#     return False

# def is_m_gesture(hand_landmarks):
#     y_threshold = 0.08  # Порог для определения примерной одной высоты
#     x_threshold = 0.08  # Порог для определения примерной одной высоты
#     y_positions = [hand_landmarks[i].y for i in [5, 9, 13, 8, 12, 16]]
#     x_positions = [hand_landmarks[i].x for i in [5, 9, 13, 8, 12, 16]]
#     ring_finger_y_13 = hand_landmarks[13].y
#     ring_finger_x_13 = hand_landmarks[13].x
#     thumb_y_4 = hand_landmarks[4].y
#     thumb_x_4 = hand_landmarks[4].x
#     pinky_y_20 = hand_landmarks[20].y
#     min_y = min(y_positions)
#     max_y = max(y_positions)
#     min_x = min(x_positions)
#     max_x = max(x_positions)
#     if (
#         (max_y - min_y < y_threshold) and
#         (max_x - min_x > x_threshold) and
#         (abs(thumb_y_4 - ring_finger_y_13 <= y_threshold)) and
#         (abs(ring_finger_x_13 - thumb_x_4 <= x_threshold)) and
#         (abs(pinky_y_20 > ring_finger_y_13 ))
#     ):
#         return True

def is_n_gesture(hand_landmarks):
    y_threshold = 0.08  # Порог для определения примерной одной высоты

    x_threshold = 0.08  # Порог для определения примерной одной высоты
    y_positions = [hand_landmarks[i].y for i in [5, 8, 9, 12]]
    x_positions = [hand_landmarks[i].x for i in [5, 8, 9, 12]]
    middle_finger_y_13 = hand_landmarks[13].y
    middle_finger_x_13 = hand_landmarks[13].x
    thumb_y_4 = hand_landmarks[4].y
    thumb_x_4 = hand_landmarks[4].x
    pinky_y_20 = hand_landmarks[20].y
    min_y = min(y_positions)
    max_y = max(y_positions)
    min_x = min(x_positions)
    max_x = max(x_positions)
    if (
        (max_y - min_y <= y_threshold)
            and
        (max_x - min_x >= x_threshold)
            and
        (abs(thumb_y_4 - middle_finger_y_13 <= y_threshold)) and
        (abs(middle_finger_x_13 - thumb_x_4 <= x_threshold))
    ):
        return True


while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    success, image = cap.read()
    image = cv2.flip(image, 1)
    results = hands.process(image)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            if is_n_gesture(handLms.landmark):
                draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)

    cv2.imshow("Hand Gesture Recognition", image)

cap.release()
cv2.destroyAllWindows()
