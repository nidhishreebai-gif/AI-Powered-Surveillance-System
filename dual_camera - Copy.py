import cv2

cam1 = cv2.VideoCapture(0)

cam2 = cv2.VideoCapture("http://192.168.1.17:8080/videofeed")

while True:

    ret1, frame1 = cam1.read()
    ret2, frame2 = cam2.read()

    if ret1:
        cv2.imshow("Laptop Camera", frame1)

    if ret2:
         frame2 = cv2.resize(frame2,(640,480))
        cv2.imshow("Mobile Camera", frame2)

    if cv2.waitKey(1) == 27:
        break

cam1.release()
cam2.release()
cv2.destroyAllWindows()