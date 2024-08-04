import cv2
import numpy as np
import dlib
from imutils import face_utils
import pygame
import tkinter as tk
from PIL import Image, ImageTk

# Initialize Pygame mixer and load alarm sound
pygame.mixer.init()
alarm_sound = pygame.mixer.Sound("mixkit-classic-alarm-995 (1).wav")

# Initialize face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Initialize variables
sleep = 0
drowsy = 0
active = 0
status = ""
color = (0, 0, 0)

# Function to compute Euclidean distance between two points
def compute(ptA, ptB):
    dist = np.linalg.norm(ptA - ptB)
    return dist

# Function to detect blinks based on facial landmarks
def blinked(a, b, c, d, e, f):
    up = compute(b, d) + compute(c, e)
    down = compute(a, f)
    ratio = up / (2.0 * down)

    if ratio > 0.25:
        return 2
    elif ratio > 0.21 and ratio <= 0.25:
        return 1
    else:
        return 0

# Function to recommend a beverage based on drowsiness level
def recommend_beverage(drowsiness_level):
    beverages = {
        'Moderate': 'Coffee with low caffeine content',
        'Severe': 'Espresso shot'
    }
    return beverages.get(drowsiness_level, 'Unknown')

# Function to update status and recommendation
def update_status():
    global sleep, drowsy, active, status, color

    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        landmarks = predictor(gray, face)
        landmarks = face_utils.shape_to_np(landmarks)

        left_blink = blinked(landmarks[36], landmarks[37], landmarks[38], landmarks[41], landmarks[40], landmarks[39])
        right_blink = blinked(landmarks[42], landmarks[43], landmarks[44], landmarks[47], landmarks[46], landmarks[45])

        if left_blink == 0 or right_blink == 0:
            sleep += 1
            drowsy = 0
            active = 0
            if sleep > 11:
                status = "SLEEPING !!!"
                color = (255, 0, 0)
                alarm_sound.play()
                recommendation_label.config(text=recommend_beverage('Severe'))
        elif left_blink == 1 or right_blink == 1:
            sleep = 0
            active = 0
            drowsy += 1
            if drowsy > 6:
                status = "Drowsy !"
                color = (0, 0, 255)
                recommendation_label.config(text=recommend_beverage('Moderate'))
        else:
            drowsy = 0
            sleep = 0
            active += 1
            if active > 11:
                status = "Active :)"
                color = (0, 255, 0)

        status_label.config(text=status, fg=f'#{color[0]:02x}{color[1]:02x}{color[2]:02x}')
        update_image(frame)

    root.after(10, update_status)

# Function to update video frame
def update_image(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (800, 600))
    img = Image.fromarray(frame)
    img = ImageTk.PhotoImage(image=img)
    video_label.imgtk = img
    video_label.config(image=img)

# Main function
def main():
    global cap, status_label, recommendation_label, video_label, root

    root = tk.Tk()
    root.title("Drowsiness Detection App")

    cap = cv2.VideoCapture(0)

    status_label = tk.Label(root, text="", font=("Helvetica", 24))
    status_label.pack()

    recommendation_label = tk.Label(root, text="", font=("Helvetica", 16))
    recommendation_label.pack()

    video_label = tk.Label(root)
    video_label.pack()

    update_status()

    root.mainloop()

if __name__ == "__main__":
    main()
