import cv2
import mediapipe as mp
import pygame
import numpy as np

# Initialize MediaPipe Hand Tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Initialize Pygame for sound
pygame.init()
strings = [pygame.mixer.Sound(f'sounds/string_{i}.wav') for i in range(6)]  # Load guitar string sounds

# Open Webcam
cap = cv2.VideoCapture(0)

# Define guitar string positions (y-coordinates)
HEIGHT = 480
WIDTH = 640
string_positions = [HEIGHT // 7 * i for i in range(1, 7)]

print("Virtual Guitar Started - Open Hand to Play...")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame")
        break
    
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get landmark positions
            landmarks = [(lm.x * WIDTH, lm.y * HEIGHT) for lm in hand_landmarks.landmark]
            
            # Detect if the hand is in a fist (check if fingertips are below base joints)
            fingers_folded = all(landmarks[i][1] > landmarks[i - 2][1] for i in [8, 12, 16, 20])  # Index, Middle, Ring, Pinky

            if fingers_folded:
                cv2.putText(frame, "Fist Detected (Muted)", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                # Get Thumb Tip Coordinates (Landmark 4)
                thumb_tip_x, thumb_tip_y = int(landmarks[4][0]), int(landmarks[4][1])
                
                # Draw Thumb Tip
                cv2.circle(frame, (thumb_tip_x, thumb_tip_y), 10, (0, 0, 255), -1)  # Red dot on thumb tip

                # Check if thumb tip is near a string
                for i, y in enumerate(string_positions):
                    if abs(thumb_tip_y - y) < 10:  # Play sound if near string
                        strings[i].play()
                        cv2.line(frame, (0, y), (WIDTH, y), (0, 255, 0), 2)  # Highlight active string
                    else:
                        cv2.line(frame, (0, y), (WIDTH, y), (255, 255, 255), 1)

    cv2.imshow("Virtual Guitar (Fist = Mute, Open = Play)", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting Virtual Guitar...")
        break

cap.release()
cv2.destroyAllWindows()