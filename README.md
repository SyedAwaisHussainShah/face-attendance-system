**📸 Face Recognition Attendance System**

A real-time face recognition-based attendance system built using Python, OpenCV, and the face_recognition library. This project captures faces through a webcam and automatically marks attendance in a CSV file.

**💻 Tech Stack**

Python, 
OpenCV, 
face_recognition, 
CSV (for attendance logging), 
Visual Studio Code (IDE)

**⚙️ How It Works**

- Capture images inside dataset/person_name/ folders.

- Run train_model.py to generate face encodings.

- Run recognize_faces.py to start real-time webcam recognition.

- Attendance is saved automatically in attendance.csv with:
👤 Name, 
📅 Date, 
⏰ Time

**🚀 Get Started**

**📥 Step 1: Install Dependencies:** 
pip install opencv-python face_recognition

**🧠 Step 2: Train the Model:**
python train_model.py

**📷 Step 3: Run Real-Time Recognition:**
python recognize_faces.py
