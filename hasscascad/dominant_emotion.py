
import cv2
from deepface import DeepFace
face_value=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)
while video. isOpened():
    frame=video.read()
    gray_img=cv2.cvtcolor(frame,cv2.COLOR_BGR2GRAY)
    face=face_value.detectMultiScale(gray_img,scaleFactor=1.1,minNeighbors=5)
    for x,y,w,h in face:
        img=cv2.rectangle(frame,(x,y),(x+w, y+h),(0,0,255),1)
        try:
            analyze=DeepFace.analyze(frame,actions=['emotion'])
            print(analyze['dominant_emotion'])
        except:
            print("noface")
    cv2.imshow('video',frame)
    key =cv2.waitkey(1)
    if key ==ord('o'):
        break
    video.release()        