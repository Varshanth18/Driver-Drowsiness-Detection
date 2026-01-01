# 🚗 Driver Drowsiness Detection System

A real-time **Driver Drowsiness Detection System** developed using **Python, OpenCV, and MediaPipe**.  
The system monitors a driver’s eye movements through a webcam and triggers an alert when prolonged eye closure (drowsiness) is detected.

This project is designed as an **academic / mini-project** and demonstrates the use of computer vision techniques for real-time safety applications.

---

## 📌 Features

- Real-time webcam video capture
- Face detection using MediaPipe
- Eye landmark (eye edge) detection
- Eye Aspect Ratio (EAR) calculation
- Drowsiness detection based on eye closure duration
- Visual alert message on screen
- Sound alert using system beep (Windows)
- Simple, real-time, and lightweight implementation
- Works with a standard laptop or USB webcam

---

## 🧠 System Overview

The system continuously analyzes the driver’s eye state using computer vision.

### High-Level Flow:
1. Capture video frames from the webcam
2. Detect the driver’s face
3. Detect eye landmarks within the face
4. Compute Eye Aspect Ratio (EAR)
5. Monitor EAR over time
6. Trigger alert if drowsiness is detected

---

## 🔄 Main Process Flow

1. **Video Capture**  
   OpenCV captures frames from the webcam in real time.

2. **Face Detection**  
   MediaPipe Face Detection is used to locate the driver’s face in each frame.

3. **Eye Landmark Detection**  
   MediaPipe Face Mesh provides precise eye landmark points (upper and lower eyelids).

4. **EAR Calculation**  
   Eye Aspect Ratio (EAR) is calculated using distances between eye landmarks.

5. **Drowsiness Detection Logic**  
   - If EAR drops below a threshold
   - And remains low for a fixed number of frames  
   → Driver is considered drowsy.

6. **Alert Mechanism**  
   - A warning message is displayed on the screen
   - A beep sound is triggered continuously while drowsiness persists

---

## 📐 Eye Aspect Ratio (EAR)

The **Eye Aspect Ratio (EAR)** is a geometric measure used to determine whether the eyes are open or closed.

### Formula:
EAR = (Vertical Distance 1 + Vertical Distance 2) / (2 × Horizontal Distance)


### Interpretation:
- **High EAR** → Eyes are open
- **Low EAR** → Eyes are closed

A continuously low EAR over multiple frames indicates drowsiness rather than a normal blink.

---

## 🤔 Why MediaPipe?

MediaPipe is used in this project because:

- It provides **highly accurate facial and eye landmarks**
- Works in **real time**
- Does not require training a machine learning model
- Lightweight and efficient for CPU-based systems
- Easy integration with OpenCV

MediaPipe Face Mesh returns normalized landmark points, which are ideal for geometric calculations like EAR.

---

## 🛠️ Technologies Used

- **Python 3**
- **OpenCV** – video capture and visualization
- **MediaPipe** – face and eye landmark detection
- **NumPy** – numerical and distance calculations
- **winsound** – sound alert on Windows

---

