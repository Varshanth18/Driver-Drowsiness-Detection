# 🚗 Driver Drowsiness Detection System

A real-time **Driver Drowsiness Detection System** developed using **Python, OpenCV, and MediaPipe**.  
The system monitors a driver’s eye movements through a webcam and triggers an alert when prolonged eye closure (drowsiness) is detected.

This project is designed as an **academic / mini-project** and demonstrates the use of computer vision for real-time safety applications.

---

## 📌 Features

- Real-time webcam video capture
- Face detection using MediaPipe
- Eye landmark (eye edge) detection
- Eye Aspect Ratio (EAR) calculation
- Drowsiness detection based on eye closure duration
- Visual alert message on screen
- Sound alert using system beep (Windows)
- Simple and easy-to-understand logic

---

## 🧠 System Overview

The system works by continuously monitoring the driver’s eyes:

1. Captures real-time video from the webcam.
2. Detects the driver’s face.
3. Extracts eye landmarks from the detected face.
4. Calculates the Eye Aspect Ratio (EAR).
5. If EAR remains below a threshold for a fixed duration:
   - The driver is considered drowsy.
   - A warning message is displayed.
   - An alarm sound is triggered.

---

## 📐 Eye Aspect Ratio (EAR)

The Eye Aspect Ratio (EAR) is used to determine whether the eyes are open or closed.

