import cv2
import os

# Try mobile camera first
mobile_url = "http://192.168.1.17:8080/video"

print("Checking mobile camera...")

cam = cv2.VideoCapture(mobile_url)

if not cam.isOpened():
    print("Mobile camera not available. Switching to laptop camera...")
    cam = cv2.VideoCapture(0)
else:
    print("Using mobile camera")

# Face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

while True:

    ret, frame = cam.read()

    if not ret:
        print("Camera not working")
        break

    frame = cv2.resize(frame,(640,480))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.putText(frame,"Face Detected",(x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,(0,255,0),2)

    cv2.imshow("AI Surveillance Camera", frame)

    if cv2.waitKey(1)==27:
        break

cam.release()
cv2.destroyAllWindows()