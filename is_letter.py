import cv2
import mediapipe as mp
import is_letter

cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands(max_num_hands=1)
draw = mp.solutions.drawing_utils


def get_finger_code(hand_landmarks):
    fingers = {
        'pyatka_y_0': hand_landmarks[0].y,
        'thumb_finger_y_3': hand_landmarks[3].y,
        'thumb_finger_y_4': hand_landmarks[4].y,
        'index_finger_y_8': hand_landmarks[8].y,
        'middle_finger_y_9': hand_landmarks[9].y,
        'middle_finger_y_12': hand_landmarks[12].y,
        'ring_finger_y_13': hand_landmarks[13].y,
        'ring_finger_y_15': hand_landmarks[15].y,
        'ring_finger_y_16': hand_landmarks[16].y,
        'pinky_finger_y_17': hand_landmarks[17].y,
        'pinky_finger_y_20': hand_landmarks[20].y,
        'thumb_finger_x_4': hand_landmarks[4].x,
        'index_finger_x_8': hand_landmarks[8].x,
    }
    return fingers


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


def is_a_gesture(hand_landmarks):
    y_threshold = 0.07  # Порог для определения примерной одной высоты
    x_threshold = 0.07  # Порог для определения примерной одной высоты
    y_positions = [hand_landmarks[i].y for i in [4, 6, 10, 14, 18]]
    x_positions = [hand_landmarks[i].x for i in [4, 6, 10, 14, 18]]
    min_y = min(y_positions)
    max_y = max(y_positions)
    min_x = min(x_positions)
    max_x = max(x_positions)
    if max_y - min_y < y_threshold and max_x - min_x > x_threshold: return True, print('a')


def is_b_gesture(hand_landmarks):
    x_threshold = 0.05
    y_threshold = 0.05

    thumb_finger_x_4 = hand_landmarks[4].x
    index_finger_x_8 = hand_landmarks[8].x
    middle_finger_x_12 = hand_landmarks[12].x
    ring_finger_x_16 = hand_landmarks[16].x
    pinky_x_20 = hand_landmarks[20].x

    thumb_finger_y_4 = hand_landmarks[4].y
    index_finger_y_8 = hand_landmarks[8].y
    middle_finger_y_12 = hand_landmarks[12].y
    ring_finger_y_16 = hand_landmarks[16].y
    pinky_y_20 = hand_landmarks[20].y

    index_finger_x_7 = hand_landmarks[7].x
    middle_finger_x_11 = hand_landmarks[11].x
    ring_finger_x_15 = hand_landmarks[15].x
    pinky_x_19 = hand_landmarks[19].x

    index_finger_y_7 = hand_landmarks[7].y
    middle_finger_y_11 = hand_landmarks[11].y
    ring_finger_y_15 = hand_landmarks[15].y
    pinky_y_19 = hand_landmarks[19].y

    ring_finger_x_13 = hand_landmarks[13].x
    ring_finger_y_13 = hand_landmarks[13].y
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


def is_e_gesture(hand_landmarks):
    y_threshold = 0.05
    thumb_finger_y_4 = hand_landmarks[4].y
    thumb_finger_x_4 = hand_landmarks[4].x
    index_finger_y_8 = hand_landmarks[8].y
    middle_finger_y_12 = hand_landmarks[12].y
    ring_finger_y_16 = hand_landmarks[16].y
    pinky_y_20 = hand_landmarks[20].y
    index_finger_y_5 = hand_landmarks[5].y
    middle_finger_y_9 = hand_landmarks[9].y
    ring_finger_y_13 = hand_landmarks[13].y
    index_finger_x_5 = hand_landmarks[5].x
    pinky_y_17 = hand_landmarks[17].y

    if (
            (abs(index_finger_y_5 - index_finger_y_8 <= y_threshold)) and
            (abs(middle_finger_y_9 - middle_finger_y_12 <= y_threshold)) and
            (abs(ring_finger_y_13 - ring_finger_y_16 <= y_threshold)) and
            (abs(pinky_y_17 - pinky_y_20 <= y_threshold)) and
            (abs(ring_finger_y_13 - thumb_finger_y_4 <= y_threshold)) and
            (abs(thumb_finger_x_4 > index_finger_x_5))
    ):
        return True, print('e')


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
    # y_positions = [hand_landmarks[i].y for i in [4, 6, 10, 14]]
    # x_positions = [hand_landmarks[i].x for i in [4, 6, 10, 14]]
    # min_y = min(y_positions)
    # max_y = max(y_positions)
    # min_x = min(x_positions)
    # max_x = max(x_positions)

    if (
            (hand_landmarks[12].y > hand_landmarks[11].y)
            and
            (hand_landmarks[8].y > hand_landmarks[7].y) and
            (hand_landmarks[16].y > hand_landmarks[15].y) and
            (pinky_y_19 > pinky_y_20) and
            (abs(hand_landmarks[4].x - hand_landmarks[6].x) <= x_threshold)
    ):
        return True, print('i')


def is_l_gesture(hand_landmarks):
    y_threshold = 0.05  # Порог для определения примерной одной высоты
    x_threshold = 0.05  # Порог для определения примерной одной высоты

    thumb_finger_y_4 = hand_landmarks[4].y
    thumb_finger_x_4 = hand_landmarks[4].x
    # middle_finger_y_12 = hand_landmarks[12].y
    index_finger_x_8 = hand_landmarks[8].x
    index_finger_y_8 = hand_landmarks[8].y
    index_finger_y_7 = hand_landmarks[7].y

    if (
            (abs(thumb_finger_x_4 - index_finger_x_8) <= x_threshold)
            and
            (abs(hand_landmarks[0].x - thumb_finger_x_4) >= x_threshold) and
            (index_finger_y_8 - index_finger_y_7 <= y_threshold) and
            (abs(hand_landmarks[0].y - thumb_finger_y_4) < y_threshold)

    ):
        return True, print('l')
    return False


def is_m_gesture(hand_landmarks):
    y_threshold = 0.08  # Порог для определения примерной одной высоты
    x_threshold = 0.08  # Порог для определения примерной одной высоты
    y_positions = [hand_landmarks[i].y for i in [5, 9, 13, 8, 12, 16]]
    x_positions = [hand_landmarks[i].x for i in [5, 9, 13, 8, 12, 16]]
    ring_finger_y_13 = hand_landmarks[13].y
    ring_finger_x_13 = hand_landmarks[13].x
    thumb_finger_y_4 = hand_landmarks[4].y
    thumb_finger_x_4 = hand_landmarks[4].x
    pinky_y_20 = hand_landmarks[20].y
    min_y = min(y_positions)
    max_y = max(y_positions)
    min_x = min(x_positions)
    max_x = max(x_positions)
    if (
            (max_y - min_y < y_threshold) and
            (max_x - min_x > x_threshold) and
            (abs(thumb_finger_y_4 - ring_finger_y_13 <= y_threshold)) and
            (abs(ring_finger_x_13 - thumb_finger_x_4 <= x_threshold)) and
            (abs(pinky_y_20 > ring_finger_y_13))
    ):
        return True, print('m')


def is_n_gesture(hand_landmarks):
    y_threshold = 0.06  # Порог для определения примерной одной высоты
    x_threshold = 0.06  # Порог для определения примерной одной высоты
    y_positions = [hand_landmarks[i].y for i in [5, 8, 9, 12]]
    x_positions = [hand_landmarks[i].x for i in [5, 8, 9, 12]]
    middle_finger_y_9 = hand_landmarks[9].y
    middle_finger_x_9 = hand_landmarks[9].x
    thumb_finger_y_4 = hand_landmarks[4].y
    thumb_finger_x_4 = hand_landmarks[4].x
    pinky_y_20 = hand_landmarks[20].y
    ring_finger_y_16 = hand_landmarks[16].y
    min_y = min(y_positions)
    max_y = max(y_positions)
    min_x = min(x_positions)
    max_x = max(x_positions)
    if (
            (max_y - min_y <= y_threshold)
            and
            (max_x - min_x <= x_threshold)
            and
            (abs(thumb_finger_y_4 - middle_finger_y_9 <= y_threshold))
            and
            (abs(middle_finger_x_9 - thumb_finger_x_4 <= x_threshold)) and
            (ring_finger_y_16 > middle_finger_y_9) and
            (pinky_y_20 > middle_finger_y_9)
    ):
        return True, print('n')


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
            (middle_finger_y_12 > thumb_finger_y_4)

    ):
        return 1, print('p')


def is_r_gesture(hand_landmarks):
    y_threshold = 0.01  # Порог для определения примерной одной высоты
    x_threshold = 0.01  # Порог для определения примерной одной высоты

    middle_finger_y_11 = hand_landmarks[11].y
    middle_finger_x_11 = hand_landmarks[11].x
    thumb_finger_y_4 = hand_landmarks[4].y
    thumb_finger_x_4 = hand_landmarks[4].x
    ring_finger_y_16 = hand_landmarks[16].y
    ring_finger_x_16 = hand_landmarks[16].x
    index_finger_y_7 = hand_landmarks[7].y
    index_finger_x_7 = hand_landmarks[7].x

    if (
            (abs(middle_finger_y_11 - index_finger_y_7 <= y_threshold)) and
            (abs(middle_finger_x_11 - index_finger_x_7 <= x_threshold)) and
            (abs(thumb_finger_x_4 - ring_finger_x_16 <= x_threshold)) and
            (abs(thumb_finger_y_4 - ring_finger_y_16 <= y_threshold))
    ):
        return True, print('r')


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
    thumb_finger_x_4 = hand_landmarks[4].x
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
            (hand_landmarks[8].x < hand_landmarks[7].x)

    ):
        return 1, print('t')


def is_u_gesture(hand_landmarks):
    y_threshold = 0.05  # Порог для определения примерной одной высоты
    x_threshold = 0.06  # Порог для определения примерной одной высоты

    middle_finger_y_12 = hand_landmarks[12].y
    middle_finger_x_12 = hand_landmarks[12].x
    middle_finger_y_11 = hand_landmarks[11].y
    thumb_finger_y_4 = hand_landmarks[4].y
    thumb_finger_x_4 = hand_landmarks[4].x
    ring_finger_y_16 = hand_landmarks[16].y
    ring_finger_x_16 = hand_landmarks[16].x
    index_finger_y_8 = hand_landmarks[8].y
    index_finger_x_8 = hand_landmarks[8].x
    index_finger_y_7 = hand_landmarks[7].y

    if (
            (abs(middle_finger_y_12 - middle_finger_y_11 <= y_threshold)) and
            (abs(index_finger_y_8 - index_finger_y_7 <= y_threshold)) and
            (abs(thumb_finger_x_4 - ring_finger_x_16 <= x_threshold)) and
            (abs(thumb_finger_y_4 - ring_finger_y_16 <= y_threshold)) and
            (abs(index_finger_y_8 - middle_finger_y_12 <= y_threshold)) and
            (abs(index_finger_x_8 - middle_finger_x_12 <= x_threshold))
    ):
        return True, print('u')


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
            (abs(index_finger_y_8 - middle_finger_y_12 <= y_threshold))

    ):
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
            (abs(middle_finger_y_12 - ring_finger_y_16 <= y_threshold))
    ):
        return True, print('w')


def is_x_gesture(hand_landmarks):
    y_threshold = 0.05  # Порог для определения примерной одной высоты

    index_finger_y_8 = hand_landmarks[8].y
    index_finger_y_6 = hand_landmarks[6].y
    index_finger_y_5 = hand_landmarks[5].y
    middle_finger_y_12 = hand_landmarks[12].y
    ring_finger_y_16 = hand_landmarks[16].y
    pinky_y_20 = hand_landmarks[20].y

    if (
            (abs(index_finger_y_6 - index_finger_y_8 < y_threshold)) and
            (index_finger_y_8 < index_finger_y_5) and
            (index_finger_y_8 < middle_finger_y_12) and
            (index_finger_y_8 < ring_finger_y_16) and
            (index_finger_y_8 < pinky_y_20)
    ):
        return True, print('x')


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
            (abs(hand_landmarks[20].x - hand_landmarks[6].x) > x_threshold)
    ):
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

    if (
            abs(index_finger_x_8 - thumb_finger_x_4) <= x_threshold and
            abs(thumb_finger_y_4 - index_finger_y_8) <= y_threshold and
            abs(pinky_y_20 - ring_finger_y_15) <= y_threshold and
            abs(ring_finger_y_15 - middle_finger_y_11) <= y_threshold and
            abs(hand_landmarks[20].x - hand_landmarks[16].x) >= 0.08 and
            abs(hand_landmarks[16].x - hand_landmarks[12].x) >= 0.08

    ):
        return 1, print("f")

def is_k_gesture(hand_landmarks):
    y_threshold = 0.05
    x_threshold = 0.05

    index_finger_y_8 = hand_landmarks[8].y
    index_finger_y_7 = hand_landmarks[7].y
    middle_finger_y_12 = hand_landmarks[12].y
    middle_finger_y_10 = hand_landmarks[10].y
    middle_finger_x_10 = hand_landmarks[10].x
    thumb_finger_y_4 = hand_landmarks[4].y
    thumb_finger_x_4 = hand_landmarks[4].x
    index_finger_x_8 = hand_landmarks[8].x
    index_finger_x_5 = hand_landmarks[5].x
    middle_finger_y_9 = hand_landmarks[9].y
    ring_finger_y_15 = hand_landmarks[15].y
    ring_finger_y_16 = hand_landmarks[16].y
    pinky_finger_y_19 = hand_landmarks[19].y
    pinky_finger_y_20 = hand_landmarks[20].y

    # fingers = get_finger_code(hand_landmarks)
    # fingers['thumb_finger_y_3']

    if (
            (index_finger_y_8 < index_finger_y_7) and
            (abs(thumb_finger_x_4 - middle_finger_x_10) <= x_threshold) and
            (abs(thumb_finger_y_4 - middle_finger_y_10) <= y_threshold) and
            (abs(index_finger_x_8 - index_finger_x_5) <= x_threshold) and
            (abs(middle_finger_y_9 - middle_finger_y_12) <= y_threshold) and
            (ring_finger_y_16 > ring_finger_y_15) and
            (pinky_finger_y_20 > pinky_finger_y_19)

    ):
        return True, print('k')


def is_q_gesture(hand_landmarks):
    y_threshold = 0.05
    y_max_threshold = 0.1
    x_min_threshold = 0.1
    fingers = get_finger_code(hand_landmarks)
    if (
            abs(fingers['index_finger_y_8'] - fingers['thumb_finger_y_4']) <= y_threshold
            and
            abs(fingers['index_finger_x_8'] - fingers['thumb_finger_x_4']) >= x_min_threshold
            and
            abs(fingers['middle_finger_y_12'] - fingers['middle_finger_y_9']) <= y_max_threshold
            and
            abs(fingers['ring_finger_y_16'] - fingers['ring_finger_y_13']) <= y_max_threshold
            and
            abs(fingers['pinky_finger_y_20'] - fingers['pinky_finger_y_17']) <= y_max_threshold
    ):
        return True, print('q')

# while True:
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
#     success, image = cap.read()
#     image = cv2.flip(image, 1)
#     results = hands.process(image)
#     if results.multi_hand_landmarks:
#         for handLms in results.multi_hand_landmarks:
#             if is_b_gesture(handLms.landmark):
#                 draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)
#
#     cv2.imshow("Hand Gesture Recognition", image)

cap.release()
cv2.destroyAllWindows()
