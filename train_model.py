import face_recognition
import os
import pickle
import cv2

dataset_dir = "dataset"
encodings_file = "encodings.pickle"

known_encodings = []
known_names = []

# Loop over each person in the dataset folder
for person_name in os.listdir(dataset_dir):
    person_folder = os.path.join(dataset_dir, person_name)
    
    if not os.path.isdir(person_folder):
        continue

    print(f"[INFO] Processing {person_name}...")

    # Loop over each image file for that person
    for image_name in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_name)
        image = cv2.imread(image_path)
        if image is None:
            continue

        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Detect face locations and encodings
        boxes = face_recognition.face_locations(rgb, model='hog')
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(person_name)

# Save encodings to a pickle file
print(f"[INFO] Saving {len(known_encodings)} encodings to {encodings_file}...")
with open(encodings_file, "wb") as f:
    pickle.dump({"encodings": known_encodings, "names": known_names}, f)

print("[INFO] Training complete.")
