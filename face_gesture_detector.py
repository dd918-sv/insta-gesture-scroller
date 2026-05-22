import cv2
import mediapipe as mp
import numpy as np


class FaceGestureDetector:

    def __init__(self):

        self.mp_face_mesh = mp.solutions.face_mesh

        self.face_mesh = self.mp_face_mesh.FaceMesh(
            refine_landmarks=True,
            max_num_faces=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def get_landmark(self, landmarks, idx, w, h):

        point = landmarks[idx]

        return np.array([
            int(point.x * w),
            int(point.y * h)
        ])

    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = self.face_mesh.process(rgb)

        if not results.multi_face_landmarks:
            return None

        landmarks = results.multi_face_landmarks[0].landmark

        h, w, _ = frame.shape

        # =====================================================
        # Mouth landmarks
        # =====================================================

        upper_lip = self.get_landmark(landmarks, 13, w, h)
        lower_lip = self.get_landmark(landmarks, 14, w, h)

        left_corner = self.get_landmark(landmarks, 61, w, h)
        right_corner = self.get_landmark(landmarks, 291, w, h)

        # =====================================================
        # Face width landmarks
        # =====================================================

        left_face = self.get_landmark(landmarks, 234, w, h)
        right_face = self.get_landmark(landmarks, 454, w, h)

        # =====================================================
        # Measurements
        # =====================================================

        mouth_height = np.linalg.norm(upper_lip - lower_lip)

        mouth_width = np.linalg.norm(left_corner - right_corner)

        face_width = np.linalg.norm(left_face - right_face)

        # =====================================================
        # Normalized values
        # =====================================================

        normalized_mouth_open = mouth_height / face_width

        normalized_mouth_width = mouth_width / face_width

        return {
            "mouth_open": normalized_mouth_open,
            "mouth_width": normalized_mouth_width
        }