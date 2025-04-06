import cv2
import mediapipe as mp
import requests

mp_face_detection = mp.solutions.face_detection
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
ESP8266_IP = "http://192.168.1.21/"

with mp_face_detection.FaceDetection(min_detection_confidence=0.7) as face_detection, \
     mp_face_mesh.FaceMesh(max_num_faces=1, min_detection_confidence=0.7) as face_mesh:
    
    face_detected = False
    
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results_detection = face_detection.process(image_rgb)
        results_mesh = face_mesh.process(image_rgb)

        if results_detection.detections:
            if not face_detected:
                print("Face detected!")
            face_detected = True
            for detection in results_detection.detections:
                bboxC = detection.location_data.relative_bounding_box
                h, w, _ = image.shape
                bbox = int(bboxC.xmin * w), int(bboxC.ymin * h), \
                       int(bboxC.width * w), int(bboxC.height * h)
                cv2.rectangle(image, bbox, (255, 0, 0), 2)

            # ส่งคำสั่งเปิด Relay
            try:
                requests.get(f"{ESP8266_IP}/turnOn")
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")

        else:
            if face_detected:
                print("Face lost!")
                try:
                    requests.get(f"{ESP8266_IP}/turnOff")
                except requests.exceptions.RequestException as e:
                    print(f"Request failed: {e}")
            face_detected = False

        if results_mesh.multi_face_landmarks:
            for face_landmarks in results_mesh.multi_face_landmarks:
                ih, iw, _ = image.shape
                points = [33, 0, 263, 362]
                for point in points:
                    landmark = face_landmarks.landmark[point]
                    x = int(landmark.x * iw)
                    y = int(landmark.y * ih)
                    if 0 <= x < iw and 0 <= y < ih:
                        cv2.circle(image, (x, y), 4, (0, 0, 255), -1)

        cv2.imshow('Face Detection and Mesh', image)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
