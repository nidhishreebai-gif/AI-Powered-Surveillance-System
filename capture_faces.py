import cv2
import os

name = input("Enter person name: ")

path = "dataset/" + name

if not os.path.exists(path):
    os.makedirs(path)

# camera (mobile or laptop)
cam = cv2.VideoCapture(0)
# if using mobile camera use this instead
# cam = cv2.VideoCapture("http://192.168.1.17:8080/video")

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

count = 0

while True:

    ret, frame = cam.read()

    if not ret:
        print("Camera not working")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:

        count += 1

        face = gray[y:y+h, x:x+w]

        file_name = path + "/" + str(count) + ".jpg"

        cv2.imwrite(file_name, face)

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        print("Captured image",count)

    cv2.imshow("Capturing Faces",frame)

    # stop after 30 images
    if count >= 30:
        break

    # press ESC to stop
    if cv2.waitKey(1)==27:
        break

cam.release()
cv2.destroyAllWindows()

print("Face capture complete")