import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access the webcam")
else:
    print("Webcam is working!")

cap.release()