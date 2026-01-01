import cv2
import mediapipe as mp
import numpy as np
import winsound

# ---------- EAR FUNCTION ----------
def eye_aspect_ratio(landmarks, eye_indices, w, h):
    pts = []
    for idx in eye_indices:
        lm = landmarks[idx]
        pts.append(np.array([int(lm.x * w), int(lm.y * h)]))

    p1, p2, p3, p4, p5, p6 = pts
    A = np.linalg.norm(p2 - p6)
    B = np.linalg.norm(p3 - p5)
    C = np.linalg.norm(p1 - p4)

    return (A + B) / (2.0 * C)

# ---------- MEDIAPIPE SETUP ----------
mp_face_mesh = mp.solutions.face_mesh
mp_face_detection = mp.solutions.face_detection

face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

face_detection = mp_face_detection.FaceDetection(
    model_selection=0,
    min_detection_confidence=0.6
)

# Eye landmark indices
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# ---------- DROWSINESS PARAMETERS ----------
EAR_THRESHOLD = 0.25
CLOSED_FRAMES_LIMIT = 30

frame_counter = 0

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # ---------- FACE DETECTION (STEP 2) ----------
    face_results = face_detection.process(rgb)
    if face_results.detections:
        for det in face_results.detections:
            bbox = det.location_data.relative_bounding_box
            x = int(bbox.xmin * w)
            y = int(bbox.ymin * h)
            bw = int(bbox.width * w)
            bh = int(bbox.height * h)

            cv2.rectangle(frame, (x, y), (x + bw, y + bh),
                          (255, 0, 0), 2)

    # ---------- FACE MESH (STEP 3 + STEP 4) ----------
    results = face_mesh.process(rgb)
    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark

        left_ear = eye_aspect_ratio(landmarks, LEFT_EYE, w, h)
        right_ear = eye_aspect_ratio(landmarks, RIGHT_EYE, w, h)
        ear = (left_ear + right_ear) / 2.0

        # ---------- DRAW EYE EDGES (STEP 3) ----------
        for idx in LEFT_EYE + RIGHT_EYE:
            lm = landmarks[idx]
            x = int(lm.x * w)
            y = int(lm.y * h)
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        # ---------- TIME LOGIC ----------
        if ear < EAR_THRESHOLD:
            frame_counter += 1
        else:
            frame_counter = 0

        # ---------- ALERT ----------
        if frame_counter >= CLOSED_FRAMES_LIMIT:
            cv2.putText(frame, "DROWSINESS ALERT!", (30, 90),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

            print("BEEP CALLED")
            winsound.Beep(2500, 1000)  # unchanged

        # ---------- EAR DISPLAY ----------
        cv2.putText(frame, f"EAR: {ear:.2f}", (30, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Driver Drowsiness Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
