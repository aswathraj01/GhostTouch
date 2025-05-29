import cv2
import mediapipe as mp
import pyautogui
from gestures import GestureController
from calibration_ui import GestureCalibrationUI

def main():
    try:
        # Launch UI
        print("Launching calibration UI...")
        ui = GestureCalibrationUI()
        ui.run()
        settings = ui.get_settings()
        print(f"Calibration settings: {settings}")

        # Init Gesture Handler
        gesture = GestureController(
            click_threshold=settings["click_threshold"],
            scroll_threshold=settings["scroll_threshold"],
            click_cooldown=settings["click_cooldown"]
        )

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("❌ Failed to open webcam.")
            return

        mp_hands = mp.solutions.hands.Hands(max_num_hands=1)
        mp_draw = mp.solutions.drawing_utils

        screen_w, screen_h = 1920, 1080  # Target screen resolution
        cam_w, cam_h = 1280, 720         # Webcam resolution
        smooth_factor = 5
        last_pos = [0, 0]
        prev_index_y = None

        while True:
            ret, frame = cap.read()
            if not ret:
                print("❌ Failed to grab frame.")
                break

            frame = cv2.flip(frame, 1)
            frame = cv2.resize(frame, (cam_w, cam_h))
            h, w, _ = frame.shape
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = mp_hands.process(rgb)

            if results.multi_hand_landmarks:
                hand = results.multi_hand_landmarks[0]
                mp_draw.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
                landmarks = hand.landmark

                # Coordinates
                index_tip = (int(landmarks[8].x * w), int(landmarks[8].y * h))
                middle_tip = (int(landmarks[12].x * w), int(landmarks[12].y * h))
                thumb_tip = (int(landmarks[4].x * w), int(landmarks[4].y * h))

                # Map index to screen position (smoothing)
                target_x = int(landmarks[8].x * screen_w)
                target_y = int(landmarks[8].y * screen_h)
                last_pos[0] += (target_x - last_pos[0]) // smooth_factor
                last_pos[1] += (target_y - last_pos[1]) // smooth_factor
                pyautogui.moveTo(last_pos[0], last_pos[1])

                # Gesture detection
                gesture.detect_left_click(index_tip, thumb_tip)
                gesture.detect_right_click(middle_tip, thumb_tip)

                if prev_index_y is None:
                    prev_index_y = index_tip[1]
                else:
                    prev_index_y = gesture.detect_scroll(index_tip, middle_tip, prev_index_y)

                # Visual markers
                cv2.circle(frame, index_tip, 10, (0, 255, 255), -1)
                cv2.circle(frame, thumb_tip, 10, (0, 0, 255), -1)
                cv2.circle(frame, middle_tip, 10, (255, 0, 0), -1)

            cv2.imshow("GhostTouch - Hand Tracking", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print("💥 Unexpected error:")
        print(e)

if __name__ == "__main__":
    main()
