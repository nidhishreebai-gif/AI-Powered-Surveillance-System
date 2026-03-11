# AI Powered Surveillance System

## Overview

The **AI Powered Surveillance System** is a smart security application that uses computer vision and artificial intelligence to monitor a camera feed in real time. The system detects human faces, recognizes known individuals, and identifies unknown persons (intruders). When an unknown person appears, the system generates alerts through voice notifications, saves the intruder image, and records the exact date and time of detection.

This project demonstrates how artificial intelligence can be used to improve security systems by automating monitoring and alert mechanisms.

---

## Objective

The objective of this project is to build an intelligent surveillance system that can automatically detect and recognize people through a camera. When an unknown person appears, the system alerts the user with voice notification and records the event with timestamp information.

---

## Key Features

* Real-time face detection using a camera
* Face recognition for known individuals
* Detection of unknown persons (intruders)
* Voice alert for known and unknown persons
* Intruder image capture and storage
* Real-time date and time display on the screen
* Email notification when an intruder is detected
* Simple and lightweight AI model suitable for real-time applications

---

## Technologies Used

### Programming Language

* Python

### Libraries

* OpenCV – Computer vision and face detection
* NumPy – Numerical operations
* pyttsx3 – Voice alerts
* smtplib – Email notification
* datetime – Real-time date and time display
* Pillow – Image processing

---

## System Workflow

1. The camera continuously captures video frames.
2. Each frame is converted into grayscale for face detection.
3. The system detects faces using a Haar Cascade classifier.
4. The detected face is compared with trained face data.
5. If the face matches the trained model, the person is identified as a known user.
6. If the face does not match, the system labels it as an unknown person.
7. When an unknown person is detected:

   * A voice alert is triggered.
   * The intruder image is saved in the alerts folder.
   * The system records the current date and time.
   * An email notification is sent.

---

## Project Structure

```
AI-Surveillance-System
│
├── app.py
├── capture_faces.py
├── train_model.py
├── dataset
│   └── captured face images
├── alerts
│   └── saved intruder images
├── trainer.yml
└── README.md
```

---

## How to Run the Project

### Step 1: Install Required Libraries

```
pip install opencv-python
pip install numpy
pip install pyttsx3
pip install pillow
```

### Step 2: Capture Face Images

Run the face capture script to collect images of the authorized person.

```
python capture_faces.py
```

This will store face images inside the dataset folder.

### Step 3: Train the Model

Train the recognition model using the captured images.

```
python train_model.py
```

This will generate the `trainer.yml` file.

### Step 4: Run the Surveillance System

Start the AI surveillance system.

```
python app.py
```

The system will open the camera and start detecting faces.

---

## Output

* Known person → Green bounding box with name and voice confirmation.
* Unknown person → Red bounding box with "Unknown".
* Voice alert: "Unknown person detected".
* Intruder image stored in the alerts folder.
* Real-time date and time displayed on the camera screen.

---

## Applications

* Smart home security
* Office security systems
* College campus monitoring
* Restricted area monitoring
* Automated surveillance systems

---

## Future Improvements

* Mobile notification system
* Cloud storage for alerts
* Multiple face recognition
* Mobile camera integration
* Web dashboard for monitoring

---

## Conclusion

This project demonstrates the practical use of artificial intelligence and computer vision in surveillance systems. By automating face detection and recognition with alert mechanisms, the system improves security monitoring and reduces the need for constant human supervision.


