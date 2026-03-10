import cv2
import os
import numpy as np
from PIL import Image

dataset_path = "dataset"

recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []

label_map = {}
current_label = 0

for person in os.listdir(dataset_path):

    label_map[current_label] = person

    person_path = os.path.join(dataset_path, person)

    for image in os.listdir(person_path):

        img_path = os.path.join(person_path, image)

        gray = np.array(Image.open(img_path).convert("L"), "uint8")

        faces.append(gray)

        labels.append(current_label)

    current_label += 1

recognizer.train(faces, np.array(labels))

recognizer.save("face_model.yml")

print("Training complete")