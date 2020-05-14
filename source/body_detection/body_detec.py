import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('/home/kms/anaconda3/envs/flaskapp/pictures/img_1.jpg',cv2.IMREAD_COLOR)

print(type(img))
face_cascade = cv2.CascadeClassifier("/home/kms/anaconda3/envs/flaskapp/source/body_detection/find_face.xml")
body_cascade = cv2.CascadeClassifier('/home/kms/anaconda3/envs/flaskapp/source/body_detection/find_body.xml')
print(type(img))
print(body_cascade)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY )
print(type(gray))
bodies = body_cascade.detectMultiScale(gray, 1.1 , 5)
faces = face_cascade.detectMultiScale(gray, 1.03, 5)
print(faces)
for (x,y,w,h) in bodies:
    cv2.rectangle(img, (x,y), (x+w, y+h), (12,150,100),1)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),1)



plt.figure(figsize=(12,12))
plt.imshow(img, cmap='gray')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

