import cv2

from face_gesture_detector import FaceGestureDetector
from gesture_controller import GestureController


def main():

    detector = FaceGestureDetector()

    controller = GestureController()

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():

        print("Could not access webcam")

        return

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # Mirror view
        frame = cv2.flip(frame, 1)

        result = detector.detect(frame)

        if result:

            controller.process(result)

            mouth_open = result["mouth_open"]

            mouth_width = result["mouth_width"]

            # =================================================
            # Gesture Display
            # =================================================

            if mouth_open > 0.08:

                gesture = "MOUTH OPEN -> PAUSE"

            elif (
                mouth_width > 0.38
                and mouth_open < 0.07
            ):

                gesture = "SMILE -> NEXT"

            elif (
                mouth_width < 0.28
                and mouth_open < 0.05
            ):

                gesture = "POUT -> PREVIOUS"

            else:

                gesture = "NEUTRAL"

            # =================================================
            # Debug Values
            # =================================================

            cv2.putText(
                frame,
                f"Mouth Open: {mouth_open:.3f}",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"Mouth Width: {mouth_width:.3f}",
                (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                gesture,
                (20, 130),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.9,
                (0, 0, 255),
                3
            )

        cv2.imshow(
            "Instagram Gesture Control",
            frame
        )

        key = cv2.waitKey(1)

        if key & 0xFF == ord('q'):
            break

    cap.release()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()