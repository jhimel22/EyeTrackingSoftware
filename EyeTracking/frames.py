# Python file for sending frames

import cv2.cv2 as cv2
import os
from datetime import datetime
from pathlib import Path
import webbrowser


path = Path("/Users/jackiehimel/Documents/EyeTrackingSoftware/")

# opens a local file in web browser
#webbrowser.open(path.absolute().as_uri())
Path.cwd()

# to later open the frame files: with path.open(mode='r') as fid:
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')

def frames():

    # opens the inbuilt camera of laptop to capture video
    video = cv2.VideoCapture(0)
    i = 0

    while True:
    # while video.isOpened():

        ret, frame = video.read()

        # converting to gray scheme
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # put date and time on each frame
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(frame, str(datetime.now()), (20,40), font, 2, (255,255,255), 2, cv2.LINE_AA)


        # prevents infinite looping if video stream ends
        if not ret:
            break

        # saves frame by frame into disk using imwrite method
        cv2.imwrite('Frame' + str(i) + '.jpg', frame)
        i += 1

        # draw rectangle around the face
        for (x, y, w, h) in faces:

            # puts rectangle around the face
            cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)


    video.release()
    cv2.destroyAllWindows()