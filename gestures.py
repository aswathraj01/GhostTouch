import math
import time
import pyautogui

class GestureController:
    def __init__(self, click_threshold=40, scroll_threshold=20, click_cooldown=0.8):
        self.click_threshold = click_threshold
        self.scroll_threshold = scroll_threshold
        self.click_cooldown = click_cooldown

        self.last_left_click = 0
        self.last_right_click = 0
        self.drag_active = False

    def distance(self, point1, point2):
        return math.hypot(point1[0] - point2[0], point1[1] - point2[1])

    def detect_left_click(self, index_tip, thumb_tip):
        dist = self.distance(index_tip, thumb_tip)
        if dist < self.click_threshold:
            now = time.time()
            if now - self.last_left_click > self.click_cooldown:
                pyautogui.click(button="left")
                self.last_left_click = now
                return True
        return False

    def detect_right_click(self, middle_tip, thumb_tip):
        dist = self.distance(middle_tip, thumb_tip)
        if dist < self.click_threshold:
            now = time.time()
            if now - self.last_right_click > self.click_cooldown:
                pyautogui.click(button="right")
                self.last_right_click = now
                return True
        return False

    def detect_scroll(self, index_tip, middle_tip, prev_index_y):
        # Use middle finger as reference if needed, currently unused
        dy = index_tip[1] - prev_index_y
        if abs(dy) > self.scroll_threshold:
            direction = -1 if dy < 0 else 1
            pyautogui.scroll(30 * direction)
        return index_tip[1]

    def detect_drag(self, ring_tip, thumb_tip):
        dist = self.distance(ring_tip, thumb_tip)
        if dist < self.click_threshold:
            if not self.drag_active:
                pyautogui.mouseDown()
                self.drag_active = True
        else:
            if self.drag_active:
                pyautogui.mouseUp()
                self.drag_active = False

    def detect_thumbs_up_both_hands(self, hands):
        """
        hands: list of hand landmarks (one for each hand)
        Return True if both hands show thumbs-up.
        """
        if len(hands) != 2:
            return False

        thumbs_up = []
        for hand in hands:
            thumb_tip = hand.landmark[4]
            index_mcp = hand.landmark[5]
            wrist = hand.landmark[0]

            if thumb_tip.y < index_mcp.y and thumb_tip.y < wrist.y:
                thumbs_up.append(True)
            else:
                thumbs_up.append(False)

        return all(thumbs_up)
