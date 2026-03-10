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

camera = cv2.VideoCapture(0)

known_counter = 0
unknown_counter = 0
display_name = ""
color = (0,255,0)

while True:

    ret, frame = camera.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:

        id, conf = recognizer.predict(gray[y:y+h, x:x+w])

        if conf < 80:
            known_counter += 1
            unknown_counter = 0
        else:
            unknown_counter += 1
            known_counter = 0

        # decide after few frames
        if known_counter > 5:
            display_name = labels.get(id,"Known")
            color = (0,255,0)

        elif unknown_counter > 5:
            display_name = "Intruder"
            color = (0,0,255)

            time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"alerts/intruder_{time}.jpg"
            cv2.imwrite(filename, frame)

        cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)

        cv2.putText(frame,display_name,(x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,0.9,color,2)

    cv2.imshow("AI Surveillance System", frame)

    if cv2.waitKey(1)==27:
        break

camera.release()
cv2.destroyAllWindows()