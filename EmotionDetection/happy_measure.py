# Happy measure via face detection

import cv2.cv2 as cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')

# detect faces, processed via a gray scale image (using cascades above)
def detect(gray, frame):

    # 1.3 is scaling factor, 5 is # of nearest neighbors (can be adjusted later)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # x,y are coordinate of the upper left corner of face frame (faces stored as tuples of coordinates)
    # height and width of the frame
    for (x, y, w, h) in faces:

        # rectangle takes argument frame of upper left/right, lower left/right cords of face, RGB code for rectangle,
        # thickness of rectangle
        cv2.rectangle(frame, (x, y), ((x + w), (y + h)), (255, 0, 0), 2)

        # defines region of interest of face
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # smile detection
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

        for (sx, sy, sw, sh) in smiles:

            cv2.rectangle(roi_color, (sx, sy), ((sx + sw), (sy + sh)), (0, 0, 255), 2)

    return frame