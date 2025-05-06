<h1>📸 Face Recognition & Attendance System</h1>

<p>A real-time face recognition-based attendance system built using Python, OpenCV, and the face_recognition library. This project captures faces through a webcam and automatically marks attendance in a CSV file.</p>

<h3>💻 Tech Stack</h3>

Python, 
OpenCV, 
face_recognition, 
CSV (for attendance logging), 
Visual Studio Code (IDE)

<h3>⚙️ How It Works</h3>

- Capture images inside dataset/person_name/ folders.

- Run train_model.py to generate face encodings.

- Run recognize_faces.py to start real-time webcam recognition.

- Attendance is saved automatically in attendance.csv with:
👤 Name, 
📅 Date, 
⏰ Time

<h3>🚀 Get Started</h3>

- **📥Install Dependencies:** 
pip install opencv-python face_recognition

- **🧠Train the Model:**
python train_model.py

- **📷Run Real-Time Recognition:**
python recognize_faces.py
