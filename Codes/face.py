import cv2

img = cv2.imread("./3.jpg")
img = cv2.resize(img,(  int(img.shape[1]/1) ,   int(img.shape[1]/1)   ))

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.05 ,minNeighbors = 20)

for x,y,w,h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

resized = cv2.resize(img,(  int(img.shape[1]/4) ,   int(img.shape[1]/4)   ))
cv2.imshow("lalala",resized)

