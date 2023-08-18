import cv2
import mediapipe as mp
import is_letter

cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands(max_num_hands=1)
draw = mp.solutions.drawing_utils


def is_pinky_up(hand_landmarks):
    return hand_landmarks[20].y <= hand_landmarks[19].y


def is_ring_up(hand_landmarks):
    return hand_landmarks[16].y + 0.05 < hand_landmarks[15].y


def is_middle_up(hand_landmarks):
    return hand_landmarks[12].y + 0.05 < hand_landmarks[11].y


def is_index_up(hand_landmarks):
    return hand_landmarks[8].y + 0.05 < hand_landmarks[7].y


def is_thumb_up(hand_landmarks):
    return hand_landmarks[4].y + 0.05 < hand_landmarks[3].y


def is_index_finger_horithontal(hand_landmarks):
    return hand_landmarks[8].y - hand_landmarks[5].y <= 0.05


def is_index_finger_down(hand_landmarks):
    return hand_landmarks[8].x - hand_landmarks[5].x <= 0.06 and hand_landmarks[8].y - hand_landmarks[5].y <= 0.06


def is_index_thumb_fingers_down(hand_landmarks):
    return hand_landmarks[8].y >= hand_landmarks[7].y and hand_landmarks[4].y >= hand_landmarks[3].y

def is_index_finger_turn_left(hand_landmarks):
    return hand_landmarks[8].x < hand_landmarks[7].x

def is_middle_finger_down(hand_landmarks):
    return hand_landmarks[12].y > hand_landmarks[9].y

def is_middle_finger_pinky(hand_landmarks):
    return abs(hand_landmarks[12].x - hand_landmarks[20].x) <= 0.05

def is_pinky_ring_finger(hand_landmarks):
    return abs(hand_landmarks[20].y - hand_landmarks[15].y) <= 0.05

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    success, image = cap.read()
    image = cv2.flip(image, 1)
    results = hands.process(image)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            if is_pinky_up(handLms.landmark):
                if is_middle_finger_down(handLms.landmark):
                    if abs(handLms.landmark[4].x - handLms.landmark[6].x) <= 0.05:
                        if is_letter.is_i_gesture(handLms.landmark):
                            draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)
                    else:
                        if is_letter.is_y_gesture(handLms.landmark):
                            draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)

                elif is_middle_finger_pinky(handLms.landmark): # C O

                        if is_letter.is_o_gesture(handLms.landmark):
                            draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)
                        elif is_letter.is_c_gesture(handLms.landmark):
                            draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)


                elif is_pinky_ring_finger(handLms.landmark): # B F
                    if abs(handLms.landmark[4].x - handLms.landmark[8].x) <= 0.05:
                        if is_letter.is_f_gesture(handLms.landmark):
                                draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)
                        elif is_letter.is_b_gesture(handLms.landmark):
                            draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)

            elif is_ring_up(handLms.landmark):  # отсекаем только W
                if is_letter.is_w_gesture(handLms.landmark):
                    draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)


            elif is_middle_up(handLms.landmark):  # отсекли R,U,V
                if abs(handLms.landmark[8].x - handLms.landmark[12].x) >= 0.1:
                    if is_letter.is_v_gesture(handLms.landmark):
                        draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)
                elif abs(handLms.landmark[8].x - handLms.landmark[12].x) <= 0.025:
                    if is_letter.is_u_gesture(handLms.landmark):
                        draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)
                else:
                    if is_letter.is_r_gesture(handLms.landmark):
                        draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)

            elif is_index_up(handLms.landmark):  # отсекли D,K,L
                if ((abs(handLms.landmark[16].x - handLms.landmark[4].x) <= 0.05) and
                        (abs(handLms.landmark[16].y - handLms.landmark[4].y) <= 0.05)):
                    if is_letter.is_d_gesture(handLms.landmark):
                        draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)
                elif ((abs(handLms.landmark[4].x - handLms.landmark[10].x) <= 0.05) and
                  (abs(handLms.landmark[4].y - handLms.landmark[10].y) <= 0.05)):
                    if is_letter.is_k_gesture(handLms.landmark):
                        draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)
                else:
                    if is_letter.is_l_gesture(handLms.landmark):
                        draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)


            elif is_thumb_up(handLms.landmark):  # A,T,S
                if handLms.landmark[4].x < handLms.landmark[6].x:
                    if is_letter.is_a_gesture(handLms.landmark):
                        draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)
                elif (abs(handLms.landmark[4].y - handLms.landmark[10].y <= 0.05) and
                      (abs(handLms.landmark[4].x - handLms.landmark[10].x <= 0.06))):
                    if is_letter.is_s_gesture(handLms.landmark):
                        draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)


            elif is_index_finger_horithontal(handLms.landmark):  # Отсев G,H,P
                if handLms.landmark[12].y > handLms.landmark[11].y:
                    if is_letter.is_p_gesture(handLms.landmark):
                        draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)
                elif handLms.landmark[12].x > handLms.landmark[8].x:
                    if is_letter.is_h_gesture(handLms.landmark):
                        draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)
                else:
                    if is_letter.is_g_gesture(handLms.landmark):
                        draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)


            elif is_index_finger_down(handLms.landmark):  # отсев E,M,N
                if ((handLms.landmark[20].x - handLms.landmark[17].x <= 0.05) and
                        (handLms.landmark[20].y - handLms.landmark[17].y <= 0.05)):
                    if is_letter.is_e_gesture(handLms.landmark):
                        draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)
                elif ((handLms.landmark[16].x - handLms.landmark[13].x <= 0.05) and
                      (handLms.landmark[16].y - handLms.landmark[13].y <= 0.05)):
                    if is_letter.is_m_gesture(handLms.landmark):
                        draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)
                else:
                    if is_letter.is_n_gesture(handLms.landmark):
                        draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)


            elif is_index_thumb_fingers_down(handLms.landmark): # Q
                if is_letter.is_q_gesture(handLms.landmark):
                    draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)

            elif is_index_finger_turn_left(handLms.landmark):
                if is_letter.is_t_gesture(handLms.landmark):
                    draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)

            else:
                if is_letter.is_x_gesture(handLms.landmark): #X
                    draw.draw_landmarks(image, handLms, mp.solutions.hands.HAND_CONNECTIONS)


    cv2.imshow("Hand Gesture Recognition", image)

cap.release()
cv2.destroyAllWindows()