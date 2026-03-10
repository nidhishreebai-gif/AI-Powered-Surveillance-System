import cv2
import os
import datetime

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("face_model.yml")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

if not os.path.exists("alerts"):
    os.makedirs("alerts")

labels = {
    0: "Nidhishree"
}

camera = cv2.VideoCapture("http://192.168.1.17:8080/video")

while True:

    ret, frame = camera.read()

    if not ret:
        print("Camera not connected")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:

        id, conf = recognizer.predict(gray[y:y+h, x:x+w])

        if conf < 60:
            name = labels.get(id,"Known")
            color = (0,255,0)

        else:
            name = "Intruder"
            color = (0,0,255)

            time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"alerts/intruder_{time}.jpg"
            cv2.imwrite(filename, frame)

        cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)

        cv2.putText(frame,name,(x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,color,2)

    cv2.imshow("AI Surveillance System", frame)

    if cv2.waitKey(1)==27:
        break

camera.release()
cv2.destroyAllWindows()