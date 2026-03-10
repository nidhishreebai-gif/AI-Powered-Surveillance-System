import cv2
import os
import datetime

# mobile camera
cam = cv2.VideoCapture("http://192.168.1.17:8080/videofeed")

# create alerts folder
if not os.path.exists("alerts"):
    os.makedirs("alerts")

while True:

    ret, frame = cam.read()

    if not ret:
        print("Camera not connected")
        break

    frame = cv2.resize(frame,(640,480))

    cv2.imshow("Mobile Surveillance Camera", frame)

    key = cv2.waitKey(1)

    # press S to capture image
    if key == ord('s'):

        time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"alerts/mobile_capture_{time}.jpg"

        cv2.imwrite(filename, frame)

        print("Image saved:", filename)

    # press ESC to exit
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()