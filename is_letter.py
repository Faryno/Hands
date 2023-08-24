import cv2
import mediapipe as mp
import math
#
# cap = cv2.VideoCapture(0)
# hands = mp.solutions.hands.Hands(max_num_hands=1)
# draw = mp.solutions.drawing_utils
def getPointsAngle(landmark1, landmark2):
    x1 = landmark1.x
    y1 = landmark1.y

    x2 = landmark2.x
    y2 = landmark2.y

    vector1X = x2 - x1
    vector1Y = y2 - y1

    vector2X = 1
    vector2Y = 0

    vector1Len = math.sqrt(vector1X ** 2 + vector1Y ** 2)
    vector2Len = math.sqrt(vector2X ** 2 + vector2Y ** 2)
    cosA = (vector1X * vector2X + vector1Y * vector2Y) / (vector1Len * vector2Len)
    rad = math.acos(cosA)

    if y1 < y2:
        deg = math.degrees(-rad) % 360
    else:
        deg = math.degrees(rad)
    return (deg - 90) % 360

def is_o_gesture(hand_landmarks):
    y_threshold = 0.1  # Порог для определения примерной одной высоты
    x_threshold = 0.1  # Порог для определения примерной одной высоты
    y_positions = [hand_landmarks[i].y for i in [4, 8, 12, 16, 20]]
    x_positions = [hand_landmarks[i].x for i in [4, 8, 12, 16, 20]]

    min_y = min(y_positions)
    max_y = max(y_positions)
    min_x = min(x_positions)
    max_x = max(x_positions)
    if abs(max_y - min_y) < y_threshold and abs(max_x - min_x) < x_threshold: return True, print('o')


def is_a(landmark):
    if ((abs(getPointsAngle(landmark[6], landmark[8]) - 185) <= 25) and
            (abs(getPointsAngle(landmark[10], landmark[12]) - 185) <= 25) and
            (abs(getPointsAngle(landmark[14], landmark[16]) - 185) <= 25) and
            (abs(getPointsAngle(landmark[18], landmark[20]) - 185) <= 25) and
            (abs(getPointsAngle(landmark[3], landmark[4]) - 340) <= 25) and
            (abs(getPointsAngle(landmark[2], landmark[3]) - 20) <= 20) and
            (abs(landmark[6].y - landmark[10].y) <= 0.05) and
            (abs(landmark[10].y - landmark[14].y) <= 0.05) and
            (abs(landmark[14].y - landmark[18].y) <= 0.05)):
        return True, print('a')
    return False


def is_b_gesture(hand_landmarks):
    x_threshold = 0.05
    y_threshold = 0.05

    index_finger_y_8 = hand_landmarks[8].y
    middle_finger_y_12 = hand_landmarks[12].y
    ring_finger_y_16 = hand_landmarks[16].y
    pinky_y_20 = hand_landmarks[20].y

    index_finger_y_7 = hand_landmarks[7].y
    middle_finger_y_11 = hand_landmarks[11].y
    ring_finger_y_15 = hand_landmarks[15].y
    pinky_y_19 = hand_landmarks[19].y

    if (
            (abs(hand_landmarks[4].x - hand_landmarks[13].x) <= x_threshold) and
            (abs(hand_landmarks[4].y - hand_landmarks[13].y) <= y_threshold) and
            (index_finger_y_7 > index_finger_y_8) and
            (middle_finger_y_11 > middle_finger_y_12) and
            (ring_finger_y_15 > ring_finger_y_16) and
            (pinky_y_19 > pinky_y_20) and
            (abs(hand_landmarks[8].y - middle_finger_y_12) <= y_threshold) and
            (abs(middle_finger_y_12 - ring_finger_y_16) <= y_threshold) and
            (abs(ring_finger_y_15 - pinky_y_20) <= y_threshold)
    ):
        return True, print('b')


def is_c_gesture(hand_landmarks):
    x_threshold = 0.07
    y_threshold = 0.07
    y_positions = [hand_landmarks[i].y for i in [8, 12, 16, 20]]
    x_positions = [hand_landmarks[i].x for i in [8, 12, 16, 20]]

    min_y = min(y_positions)
    max_y = max(y_positions)
    min_x = min(x_positions)
    max_x = max(x_positions)
    if (
            (max_y - min_y < y_threshold) and
            (max_x - min_x < x_threshold) and
            (abs(hand_landmarks[8].x - hand_landmarks[4].x) <= x_threshold)
    ):
        return True, print('c')


def is_d_gesture(hand_landmarks):
    y_threshold = 0.07
    index_finger_y_8 = hand_landmarks[8].y
    index_finger_y_7 = hand_landmarks[7].y
    pyatka_y_0 = hand_landmarks[0].y
    thumb_finger_x_4 = hand_landmarks[4].x
    index_finger_x_8 = hand_landmarks[8].x
    y_positions = [hand_landmarks[i].y for i in [4, 12, 16, 20]]
    min_y = min(y_positions)
    max_y = max(y_positions)
    if (
            (max_y - min_y < y_threshold) and
            (index_finger_y_8 < max_y) and
            (abs(index_finger_y_7 - index_finger_y_8 <= y_threshold) > pyatka_y_0) and
            (thumb_finger_x_4 >= index_finger_x_8)
    ):
        return True, print('d')

def is_e(landmark):
    if ((abs(getPointsAngle(landmark[6], landmark[8]) - 185) <= 25) and
            (abs(getPointsAngle(landmark[10], landmark[12]) - 185) <= 25) and
            (abs(getPointsAngle(landmark[14], landmark[16]) - 185) <= 25) and
            (abs(getPointsAngle(landmark[18], landmark[20]) - 185) <= 25) and
            (abs(getPointsAngle(landmark[3], landmark[4]) - 330) <= 25) and
            (abs(getPointsAngle(landmark[2], landmark[3]) - 330) <= 25) and
            (abs(landmark[5].y - landmark[8].y) <= 0.05) and
            (abs(landmark[9].y - landmark[12].y) <= 0.05) and
            (abs(landmark[13].y - landmark[16].y) <= 0.05) and
            (abs(landmark[17].y - landmark[20].y) <= 0.05) and
            (abs(landmark[8].y - landmark[12].y) <= 0.05) and
            (abs(landmark[12].y - landmark[16].y) <= 0.05) and
            (abs(landmark[16].y - landmark[20].y) <= 0.05) and
            (abs(landmark[4].y - landmark[16].y) <= 0.05)
    ):
        return True, print('e')
    return False

def is_g_gesture(hand_landmarks):
    x_threshold = 0.03

    index_finger_x_8 = hand_landmarks[8].x
    middle_finger_x_12 = hand_landmarks[12].x
    x_positions = [hand_landmarks[i].x for i in [4, 10, 14, 18]]
    min_x = min(x_positions)
    max_x = max(x_positions)

    if (
            (middle_finger_x_12 < index_finger_x_8) and
            (max_x - min_x < x_threshold)
    ):
        return 1, print('g')
    return False


def is_h_gesture(hand_landmarks):
    x_threshold = 0.07

    index_finger_x_8 = hand_landmarks[8].x
    middle_finger_x_12 = hand_landmarks[12].x
    thumb_4 = hand_landmarks[4].x
    x_positions = [hand_landmarks[i].x for i in [4, 10, 14, 18]]
    min_x = min(x_positions)
    max_x = max(x_positions)

    if (
            (middle_finger_x_12 > index_finger_x_8) and
            (index_finger_x_8 > thumb_4) and
            (max_x - min_x < x_threshold)

    ):
        return True, print('h')


def is_i_gesture(hand_landmarks):
    y_threshold = 0.05  # Порог для определения примерной одной высоты
    x_threshold = 0.05  # Порог для определения примерной одной высоты
    pinky_y_20 = hand_landmarks[20].y
    pinky_y_19 = hand_landmarks[19].y

    if (
            (hand_landmarks[12].y > hand_landmarks[11].y)
            and
            (hand_landmarks[8].y > hand_landmarks[7].y) and
            (hand_landmarks[16].y > hand_landmarks[15].y) and
            (pinky_y_19 > pinky_y_20) and
            (abs(hand_landmarks[4].x - hand_landmarks[6].x) <= x_threshold)
    ):
        return True, print('i')


def is_l(landmark):
    if ((abs(getPointsAngle(landmark[5], landmark[8]) - 45) <= 15) and
            (abs(getPointsAngle(landmark[10], landmark[12]) - 220) <= 25) and
            (abs(getPointsAngle(landmark[14], landmark[16]) - 220) <= 25) and
            (abs(getPointsAngle(landmark[18], landmark[20]) - 230) <= 25) and
            (abs(getPointsAngle(landmark[2], landmark[4]) - 90) <= 15)):
        return True, print('l')
    return False

def is_m(landmark):
    if ((abs(getPointsAngle(landmark[6], landmark[8]) - 185) <= 25) and
            (abs(getPointsAngle(landmark[10], landmark[12]) - 185) <= 25) and
            (abs(getPointsAngle(landmark[14], landmark[16]) - 185) <= 25) and
            (abs(getPointsAngle(landmark[18], landmark[20]) - 185) <= 25) and
            (abs(getPointsAngle(landmark[3], landmark[4]) - 330) <= 25) and
            (abs(getPointsAngle(landmark[2], landmark[3]) - 330) <= 25) and
            (abs(landmark[5].y - landmark[8].y) <= 0.07) and
            (abs(landmark[9].y - landmark[12].y) <= 0.07) and
            (abs(landmark[13].y - landmark[16].y) <= 0.07) and
            (abs(landmark[4].y - landmark[16].y) <= 0.07) and
            (abs(landmark[8].y - landmark[12].y) <= 0.05) and
            (abs(landmark[12].y - landmark[16].y) <= 0.05) and
            (abs(landmark[20].y - landmark[4].y) >= 0.07)):
        return True, print('m')
    return False

def is_n(landmark):
    if ((abs(getPointsAngle(landmark[6], landmark[8]) - 185) <= 25) and
            (abs(getPointsAngle(landmark[10], landmark[12]) - 185) <= 25) and
            (abs(getPointsAngle(landmark[14], landmark[16]) - 185) <= 25) and
            (abs(getPointsAngle(landmark[18], landmark[20]) - 185) <= 25) and
            (abs(getPointsAngle(landmark[3], landmark[4]) - 335) <= 25) and
            (abs(getPointsAngle(landmark[2], landmark[3]) - 350) <= 25) and
            (abs(landmark[5].y - landmark[8].y) <= 0.07) and
            (abs(landmark[9].y - landmark[12].y) <= 0.07) and
            (abs(landmark[8].y - landmark[12].y) <= 0.05) and
            (abs(landmark[4].y - landmark[12].y) <= 0.07) and
            (abs(landmark[16].y - landmark[4].y) >= 0.07) and
            (abs(landmark[20].y - landmark[4].y) >= 0.07)):
        return True, print('n')
    return False


def is_p_gesture(hand_landmarks):
    y_threshold = 0.08  # Порог для определения примерной одной высоты
    x_threshold = 0.06  # Порог для определения примерной одной высоты

    middle_finger_y_12 = hand_landmarks[12].y
    middle_finger_y_11 = hand_landmarks[11].y
    thumb_finger_y_4 = hand_landmarks[4].y
    middle_finger_y_10 = hand_landmarks[10].y
    middle_finger_x_10 = hand_landmarks[10].x
    thumb_finger_x_4 = hand_landmarks[4].x
    index_finger_y_8 = hand_landmarks[8].y
    pyatka_y_0 = hand_landmarks[0].y

    if (
            (abs(pyatka_y_0 - index_finger_y_8 <= y_threshold))
            and
            (middle_finger_y_12 - middle_finger_y_11 <= y_threshold) and
            (abs(thumb_finger_x_4 - middle_finger_x_10 <= x_threshold)) and
            (abs(thumb_finger_y_4 - middle_finger_y_10 <= y_threshold)) and
            (middle_finger_y_12 > thumb_finger_y_4)):
        return True, print('p')


def is_r(landmark):
    if ((abs(getPointsAngle(landmark[3], landmark[4]) - 335) <= 25) and
        (abs(getPointsAngle(landmark[14], landmark[16]) - 170) <= 25) and
            ((0 <= getPointsAngle(landmark[9], landmark[12]) and getPointsAngle(landmark[9], landmark[12]) <= 15) or (325 <= getPointsAngle(landmark[9], landmark[12]) and getPointsAngle(landmark[9], landmark[12]) <= 360)) and
        (abs(getPointsAngle(landmark[5], landmark[8]) - 350) <= 25) and
            (abs(getPointsAngle(landmark[14], landmark[16]) - 165) <= 15) and
            (landmark[8].x > landmark[12].x)):return True, print('r')
    return False

def is_s_gesture(hand_landmarks):
    y_threshold = 0.04  # Порог для определения примерной одной высоты
    x_threshold = 0.04 # Порог для определения примерной одной высоты

    y_positions = [hand_landmarks[i].y for i in [8, 12, 16, 20]]
    x_positions = [hand_landmarks[i].x for i in [8, 12, 16, 20]]
    thumb_finger_y_4 = hand_landmarks[4].y
    thumb_finger_x_4 = hand_landmarks[4].x
    middle_finger_y_10 = hand_landmarks[10].y
    middle_finger_x_10 = hand_landmarks[10].x
    min_y = min(y_positions)
    max_y = max(y_positions)
    min_x = min(x_positions)
    max_x = max(x_positions)
    if (
            (max_y - min_y < y_threshold) and
            (max_x - min_x > x_threshold) and
            (abs(middle_finger_x_10 - thumb_finger_x_4 <= x_threshold)) and
            (abs(middle_finger_y_10 - thumb_finger_y_4 <= y_threshold))
    ):
        return True, print('s')


def is_t_gesture(hand_landmarks):
    y_threshold = 0.05  # Порог для определения примерной одной высоты
    x_threshold = 0.06  # Порог для определения примерной одной высоты

    index_finger_x_8 = hand_landmarks[8].x
    thumb_finger_x_3 = hand_landmarks[3].x
    index_finger_y_6 = hand_landmarks[6].y
    index_finger_x_6 = hand_landmarks[6].x
    middle_finger_x_12 = hand_landmarks[12].x
    ring_finger_x_16 = hand_landmarks[16].x
    pinky_x_20 = hand_landmarks[20].x
    if (
            (abs(index_finger_y_6 - hand_landmarks[8].y) <= y_threshold) and
            (abs(index_finger_x_6 - thumb_finger_x_3) <= x_threshold) and
            (abs(index_finger_y_6 - hand_landmarks[3].y) <= x_threshold) and
            (index_finger_x_8 < middle_finger_x_12) and
            (index_finger_x_8 < ring_finger_x_16) and
            (index_finger_x_8 < pinky_x_20) and
            (hand_landmarks[8].x < hand_landmarks[7].x)):
        return 1, print('t')


def is_u(landmark):
    if ((abs(getPointsAngle(landmark[3], landmark[4]) - 335) <= 25) and
            (abs(getPointsAngle(landmark[14], landmark[16]) - 170) <= 25) and
            ((0 <= getPointsAngle(landmark[5], landmark[8]) and getPointsAngle(landmark[5], landmark[8]) <= 15) or (325 <= getPointsAngle(landmark[5], landmark[8]) and getPointsAngle(landmark[5], landmark[8]) <= 360)) and
            ((0 <= getPointsAngle(landmark[9], landmark[12]) and getPointsAngle(landmark[9], landmark[12]) <= 15) or (325 <= getPointsAngle(landmark[9], landmark[12]) and getPointsAngle(landmark[9],landmark[12]) <= 360)) and
            (abs(getPointsAngle(landmark[14], landmark[16]) - 165) <= 15) and
            (abs(landmark[7].y - landmark[10].y) >= 0.04) and
            (abs(landmark[8].x - landmark[12].x) <= 0.05)):
        return True, print('u')
    return False


def is_v_gesture(hand_landmarks):
    y_threshold = 0.05  # Порог для определения примерной одной высоты
    x_threshold = 0.06  # Порог для определения примерной одной высоты

    middle_finger_y_12 = hand_landmarks[12].y
    middle_finger_y_11 = hand_landmarks[11].y
    index_finger_y_8 = hand_landmarks[8].y
    index_finger_y_7 = hand_landmarks[7].y
    thumb_finger_y_4 = hand_landmarks[4].y
    thumb_finger_x_4 = hand_landmarks[4].x
    ring_finger_y_16 = hand_landmarks[16].y
    ring_finger_x_16 = hand_landmarks[16].x

    if (
            (abs(thumb_finger_x_4 - ring_finger_x_16 <= x_threshold)) and
            (abs(thumb_finger_y_4 - ring_finger_y_16 <= y_threshold)) and
            (abs(middle_finger_y_12 - middle_finger_y_11 <= y_threshold)) and
            (abs(index_finger_y_8 - index_finger_y_7 <= y_threshold)) and
            (abs(middle_finger_y_12 - index_finger_y_8 <= y_threshold)) and
            (abs(index_finger_y_8 - middle_finger_y_12 <= y_threshold))):
        return 1, print('v')

def is_w_gesture(hand_landmarks):
    y_threshold = 0.05  # Порог для определения примерной одной высоты
    x_threshold = 0.06  # Порог для определения примерной одной высоты

    middle_finger_y_12 = hand_landmarks[12].y
    middle_finger_y_11 = hand_landmarks[11].y
    index_finger_y_8 = hand_landmarks[8].y
    index_finger_y_7 = hand_landmarks[7].y
    ring_finger_y_16 = hand_landmarks[16].y
    ring_finger_y_15 = hand_landmarks[15].y
    thumb_finger_y_4 = hand_landmarks[4].y
    thumb_finger_x_4 = hand_landmarks[4].x
    pinky_x_20 = hand_landmarks[20].x
    pinky_y_20 = hand_landmarks[20].y

    if (
            (abs(pinky_x_20 - thumb_finger_x_4 <= x_threshold)) and
            (abs(pinky_y_20 - thumb_finger_y_4 <= y_threshold)) and
            (middle_finger_y_12 < middle_finger_y_11) and
            (index_finger_y_8 < index_finger_y_7) and
            (ring_finger_y_16 < ring_finger_y_15) and
            (abs(index_finger_y_8 - middle_finger_y_12 <= y_threshold)) and
            (abs(middle_finger_y_12 - ring_finger_y_16 <= y_threshold))):
        return True, print('w')

def is_x(landmark):
        if ((abs(getPointsAngle(landmark[2], landmark[3]) - 30) <= 15) and
                (abs(getPointsAngle(landmark[3], landmark[4]) - 30) <= 15) and
                (abs(getPointsAngle(landmark[10], landmark[12]) - 200) <= 15) and
                (abs(getPointsAngle(landmark[14], landmark[16]) - 220) <= 15) and
                (abs(getPointsAngle(landmark[18], landmark[20]) - 215) <= 15)):
            return True, print('x')
        return False

def is_y_gesture(hand_landmarks):
    y_threshold = 0.05
    x_threshold = 0.1
    pinky_y_19 = hand_landmarks[19].y
    thumb_finger_y_4 = hand_landmarks[4].y
    index_finger_y_6 = hand_landmarks[6].y
    index_finger_y_8 = hand_landmarks[8].y
    middle_finger_y_12 = hand_landmarks[12].y
    ring_finger_y_16 = hand_landmarks[16].y

    if (
            (abs(index_finger_y_8 - middle_finger_y_12 <= y_threshold)) and
            (abs(middle_finger_y_12 - ring_finger_y_16 <= y_threshold)) and
            (abs(ring_finger_y_16 - index_finger_y_8 <= y_threshold)) and
            (abs(thumb_finger_y_4 - index_finger_y_6 <= y_threshold)) and
            (index_finger_y_8 > index_finger_y_6) and
            (middle_finger_y_12 > index_finger_y_6) and
            (ring_finger_y_16 > index_finger_y_6) and
            (abs(pinky_y_19 - index_finger_y_6) <= y_threshold) and
            (abs(hand_landmarks[4].x - hand_landmarks[6].x) > x_threshold) and
            (abs(hand_landmarks[20].x - hand_landmarks[6].x) > x_threshold)):
        return True, print('y')

def is_f_gesture(hand_landmarks):
    y_threshold = 0.08
    x_threshold = 0.05

    thumb_finger_y_4 = hand_landmarks[4].y
    thumb_finger_x_4 = hand_landmarks[4].x
    index_finger_y_8 = hand_landmarks[8].y
    index_finger_x_8 = hand_landmarks[8].x
    middle_finger_y_11 = hand_landmarks[11].y
    ring_finger_y_15 = hand_landmarks[15].y
    pinky_y_20 = hand_landmarks[20].y

    if (abs(index_finger_x_8 - thumb_finger_x_4) <= x_threshold and
            abs(thumb_finger_y_4 - index_finger_y_8) <= y_threshold and
            abs(pinky_y_20 - ring_finger_y_15) <= y_threshold and
            abs(ring_finger_y_15 - middle_finger_y_11) <= y_threshold and
            abs(hand_landmarks[20].x - hand_landmarks[16].x) >= 0.08 and
            abs(hand_landmarks[16].x - hand_landmarks[12].x) >= 0.08):
        return 1, print("f")

def is_k(landmark):
    if (((0 <= getPointsAngle(landmark[5], landmark[8]) and getPointsAngle(landmark[5], landmark[8]) <= 10) or (350 <= getPointsAngle(landmark[5], landmark[8]) and getPointsAngle(landmark[5], landmark[8]) <= 360)) and #####################
            ((0 <= getPointsAngle(landmark[2], landmark[4]) and getPointsAngle(landmark[2], landmark[4]) <= 5) or (345 <= getPointsAngle(landmark[2], landmark[4]) and getPointsAngle(landmark[2], landmark[4]) <= 360)) and
            (abs(getPointsAngle(landmark[10], landmark[12]) - 115) <= 25) ):
        return True, print('k')
    return False

def is_q(landmark):
    if ((abs(getPointsAngle(landmark[5], landmark[8]) - 190) <= 10) and
            (abs(getPointsAngle(landmark[2], landmark[4]) - 188) <= 10)):
        return True, print('q')
    return False

