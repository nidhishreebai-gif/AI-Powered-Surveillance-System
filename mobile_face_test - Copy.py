import cv2

# mobile camera stream
cam = cv2.VideoCapture("http://192.168.1.17:8080/videofeed")

# face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

while True:

    ret, frame = cam.read()

    if not ret:
        print("Camera not connected")
        break

    # resize frame for faster detection
    frame = cv2.resize(frame,(640,480))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4
    )

    for (x,y,w,h) in faces:

        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.putText(frame,"Face Detected",(x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,(0,255,0),2)

    cv2.imshow("Mobile Camera Face Detection", frame)

    if cv2.waitKey(1)==27:
        break

cam.release()
cv2.destroyAllWindows()