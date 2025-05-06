import face_recognition
import cv2
import pickle
import os
from datetime import datetime
import csv

with open("encodings.pickle", "rb") as f:
    data = pickle.load(f)

video_capture = cv2.VideoCapture(0)

if not os.path.exists("attendance.csv"):
    with open("attendance.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Date", "Time"])

print("[INFO] Starting face recognition...")

logged_names = set()

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb_frame)
    encodings = face_recognition.face_encodings(rgb_frame, boxes)

    names = []

    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"], encoding)
        name = "Unknown"

        if True in matches:
            matched_idxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            for i in matched_idxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1

            name = max(counts, key=counts.get)

        names.append(name)

        if name not in logged_names:
            logged_names.add(name)

            now = datetime.now()
            date_str = now.strftime("%Y-%m-%d")
            time_str = now.strftime("%H:%M:%S")

            with open("attendance.csv", "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([name, date_str, time_str])

            print(f"[LOG] {name} logged at {date_str} {time_str}")

    for (top, right, bottom, left), name in zip(boxes, names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.75, (0, 255, 0), 2)

    cv2.imshow("Face Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
