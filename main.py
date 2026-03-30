# #Face Recognition with Arduino Integration

# import cv2
# import numpy as np
# import serial
# import time
# import pickle

# # Setup serial communication with Arduino
# arduino = serial.Serial('COM11', 9600)  
# time.sleep(2)  # Wait for Arduino to initialize

# # Load the face detection model and trained recognizer
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.read('trainer/trainer.yml')

# # Load labels (id to name mapping)
# with open('trainer/labels.pickle', 'rb') as f:
#     labels = pickle.load(f)

# # Start video capture
# cap = cv2.VideoCapture(0)

# # Function to send face status to Arduino
# def send_to_arduino(face_status):
#     if face_status == 'known':
#         arduino.write(b'1')
#     elif face_status == 'unknown':
#         arduino.write(b'2')
#     else:
#         arduino.write(b'0')

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#     face_status_sent = 'none'  # default value

#     for (x, y, w, h) in faces:
#         roi_gray = gray[y:y+h, x:x+w]
#         id_, conf = recognizer.predict(roi_gray)

#         if conf < 60:
#             name = labels.get(id_, "Unknown")
#             face_status_sent = 'known'
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#             cv2.putText(frame, name, (x, y-10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#         else:
#             face_status_sent = 'unknown'
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
#             cv2.putText(frame, "Unknown", (x, y-10),
#                         cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#         break  # Only process the first detected face
   
#     send_to_arduino(face_status_sent)

#     cv2.imshow('Face Recognition', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
# arduino.close()

# Face Recognition without Arduino

import cv2
import numpy as np
import pickle

# Load the face detection model and trained recognizer
face_cascade = cv2.CascadeClassifier('face_recognition/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('face_recognition/trainer/trainer.yml')

# Load labels (id to name mapping)
with open('face_recognition/trainer/labels.pickle', 'rb') as f:
    labels = pickle.load(f)

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        id_, conf = recognizer.predict(roi_gray)

        if conf < 60:
            name = labels.get(id_, "Unknown")
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, name, (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.putText(frame, "Unknown", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        break  # Only process the first detected face

    cv2.imshow('Face Recognition', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
