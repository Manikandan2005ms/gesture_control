import cv2
import mediapipe as mp
import pyautogui
import subprocess
import keyboard
import time
from datetime import datetime

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1)

# Webcam
cap = cv2.VideoCapture(0)

# Tracking variables
prev_action = None
action_time = 0
gesture_cooldown = 1.5
scroll_threshold = 40
last_y = None

# Screenshot function
def take_screenshot():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    pyautogui.screenshot(f"screenshot_{timestamp}.png")

# Launch apps
def launch_app(app_name):
    if app_name == "notepad":
        subprocess.Popen(["notepad.exe"])
    elif app_name == "calculator":
        subprocess.Popen("calc.exe")

# Detect gesture
def gesture_to_action(landmarks):
    fingers = []

    # Thumb
    if landmarks[4].x < landmarks[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    for tip in [8, 12, 16, 20]:
        if landmarks[tip].y < landmarks[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    # Gesture mapping
    if fingers == [0, 0, 0, 0, 0]:
        return "screenshot"
    elif fingers == [0, 1, 0, 0, 0]:
        return "select"
    elif fingers == [0, 1, 1, 0, 0]:
        return "copy"
    elif fingers == [0, 1, 1, 1, 0]:
        return "cut"
    elif fingers == [1, 1, 0, 0, 1]:
        return "paste"
    elif fingers == [0, 1, 0, 0, 0] and landmarks[8].x > 0.8:
        return "open_calc"
    elif fingers == [0, 1, 0, 0, 0] and landmarks[8].x < 0.2:
        return "open_notepad"
    return "none"

# Main loop
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    h, w, _ = img.shape
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    action = "none"

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark
            y_pos = landmarks[8].y * h

            # Detect scroll (open palm movement)
            fingers = []
            for tip in [4, 8, 12, 16, 20]:
                if landmarks[tip].y < landmarks[tip - 2].y:
                    fingers.append(1)
                else:
                    fingers.append(0)

            if fingers == [1, 1, 1, 1, 1]:
                if last_y is not None:
                    diff = y_pos - last_y
                    if diff > scroll_threshold:
                        pyautogui.scroll(-30)
                        action = "scroll_down"
                    elif diff < -scroll_threshold:
                        pyautogui.scroll(30)
                        action = "scroll_up"
                last_y = y_pos

            # Gesture actions
            gesture = gesture_to_action(landmarks)
            if gesture == prev_action:
                if time.time() - action_time > gesture_cooldown:
                    if gesture == "copy":
                        keyboard.press_and_release('ctrl+c')
                    elif gesture == "cut":
                        keyboard.press_and_release('ctrl+x')
                    elif gesture == "paste":
                        keyboard.press_and_release('ctrl+v')
                    elif gesture == "select":
                        pyautogui.click()
                    elif gesture == "screenshot":
                        take_screenshot()
                    elif gesture == "open_notepad":
                        launch_app("notepad")
                    elif gesture == "open_calc":
                        launch_app("calculator")
                    action_time = time.time()
            else:
                prev_action = gesture
                action_time = time.time()

            # Feedback on screen
            display_text = gesture if gesture != "none" else action
            cv2.putText(img, f"Gesture: {display_text}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    else:
        prev_action = None
        last_y = None

    cv2.imshow("AI Gesture Control", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
