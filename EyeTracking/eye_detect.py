# Eye detection

import cv2.cv2 as cv2
import sys

cascadePath = sys.argv[1]

eyeCascade = cv2.CascadeClassifier(cascadePath)

video_cap = cv2.VideoCapture(0)

while True:
    ret, frame = video_cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    eyes = eyeCascade.detectMultiScale(gray, 1.3, 5)

    # draw rectangle around the face
    for (x,y,w,h) in eyes:

        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)
