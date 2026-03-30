# import cv2
# import os
# import numpy as np
# import pickle

# # Load the face detection model
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# def get_images_and_labels(dataset_path):
#     image_paths = []
#     original_labels = []
#     label_map = {}
#     current_label = 0

#     for person_name in os.listdir(dataset_path):
#         person_path = os.path.join(dataset_path, person_name)
#         if not os.path.isdir(person_path):
#             continue
#         label_map[current_label] = person_name

#         for image_name in os.listdir(person_path):
#             image_path = os.path.join(person_path, image_name)
#             image_paths.append(image_path)
#             original_labels.append(current_label)

#         current_label += 1

#     face_samples = []
#     detected_labels = []
#     for image_path, label in zip(image_paths, original_labels):
#         img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
#         faces = face_cascade.detectMultiScale(img)
#         for (x, y, w, h) in faces:
#             face_samples.append(img[y:y+h, x:x+w])
#             detected_labels.append(label)

#     print(f"✅ Collected {len(face_samples)} face samples and {len(detected_labels)} labels")
#     return face_samples, detected_labels, label_map

# def train_model(dataset_path, model_save_path):
#     # Load face images and their corresponding labels
#     faces, labels, label_map = get_images_and_labels(dataset_path)

#     if len(faces) == 0 or len(labels) == 0:
#         print("❌ No faces or labels found. Check your dataset structure and images.")
#         return None

#     # Create the face recognizer
#     recognizer = cv2.face.LBPHFaceRecognizer_create()

#     # Train the recognizer
#     recognizer.train(faces, np.array(labels))

#     # Save the trained model
#     recognizer.save(model_save_path)

#     print("🎉 Training complete. Model saved to:", model_save_path)
#     print("📝 Labels:", label_map)

#     return label_map

# dataset_dir = 'dataset'
# model_path = 'trainer/trainer.yml'
# label_mapping = train_model(dataset_dir, model_path)

# # Save the label map as a pickle file
# with open('trainer/labels.pickle', 'wb') as f:
#     pickle.dump(label_mapping, f)

import os
import cv2
import numpy as np
import pickle

# Load the face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def get_images_and_labels(dataset_path):
    image_paths = []
    original_labels = []
    label_map = {}
    current_label = 0

    for person_name in os.listdir(dataset_path):
        person_path = os.path.join(dataset_path, person_name)
        if not os.path.isdir(person_path):
            continue
        label_map[current_label] = person_name

        for image_name in os.listdir(person_path):
            image_path = os.path.join(person_path, image_name)
            image_paths.append(image_path)
            original_labels.append(current_label)

        current_label += 1

    face_samples = []
    detected_labels = []
    for image_path, label in zip(image_paths, original_labels):
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        faces = face_cascade.detectMultiScale(img)
        for (x, y, w, h) in faces:
            face_samples.append(img[y:y+h, x:x+w])
            detected_labels.append(label)

    print(f"✅ Collected {len(face_samples)} face samples and {len(detected_labels)} labels")
    return face_samples, detected_labels, label_map

def train_model(dataset_path, model_save_path):
    # Load face images and their corresponding labels
    faces, labels, label_map = get_images_and_labels(dataset_path)

    if len(faces) == 0 or len(labels) == 0:
        print("❌ No faces or labels found. Check your dataset structure and images.")
        return None

    # Create the face recognizer
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    # Train the recognizer
    recognizer.train(faces, np.array(labels))

    # 🔥 Ensure trainer folder exists
    trainer_folder = os.path.dirname(model_save_path)
    os.makedirs(trainer_folder, exist_ok=True)

    # Save the trained model
    recognizer.save(model_save_path)

    print("🎉 Training complete. Model saved to:", model_save_path)
    print("📝 Labels:", label_map)

    return label_map

dataset_dir = 'dataset'
model_path = 'trainer/trainer.yml'
label_mapping = train_model(dataset_dir, model_path)

# Save the label map as a pickle file
os.makedirs('trainer', exist_ok=True)  # 🔥 Ensure trainer folder exists
with open('trainer/labels.pickle', 'wb') as f:
    pickle.dump(label_mapping, f)


