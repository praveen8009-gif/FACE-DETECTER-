import cv2
import os 
from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc
from datetime import datetime
from random import randrange as r

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
current_time = now.strftime(" %I - %M - %S")

cap = cv2.VideoCapture(0)

video = VideoWriter(current_date+current_time+'.avi', VideoWriter_fourcc(*'MP42'), 10.0, (640,480) )

faceCascade =cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
       

while(True):
     
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2GRAY )

	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor =1.3,
		minNeighbors =5,
		minSize =(30,30),
	)
	if len(faces) > 0:
		for (x,y,w,h) in faces:
			cv2.rectangle(frame, (x,y), (x+w, y+h), (r(0,256),r(0,256),r(0,256)),4)
			
		print("face found !!")
	else:
		print("Not human face!!")
	cv2.imshow('frame', frame)

	video.write(frame)

	if cv2.waitKey(30) & 0xFF == ord('q'):
    		break	
	
	
cap.release()
cv2.destroyAllWindows()
video.release()