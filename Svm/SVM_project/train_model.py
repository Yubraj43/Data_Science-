import face_recognition
import os
import numpy as np
import pickle
from sklearn import svm


dataset_path = "dataset"
encodings = []
labels = []

# Loop through each person in the dataset
for person_name in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person_name)
    
    # Loop through each image of the person
    for image_name in os.listdir(person_path):
        image_path = os.path.join(person_path, image_name)
        
        # Load the image and get face encodings
        image = face_recognition.load_image_file(image_path)
        face_encodings = face_recognition.face_encodings(image)
        
        if len(face_encodings) > 0:
            encodings.append(face_encodings[0])
            labels.append(person_name)

# Train the SVM model
if not encodings:
    raise ValueError("No face encodings found. Check the dataset folder and image files.")

model = svm.SVC(kernel='linear', probability=True)
model.fit(encodings, labels)
# Save the trained model
with open("svm_model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Model trained and saved successfully.")

