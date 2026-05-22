import pyautogui
import time


class GestureController:

    def __init__(self):

        # =====================================================
        # Cooldown
        # =====================================================

        self.cooldown = 1.5

        self.last_action_time = 0

        # =====================================================
        # Gesture states
        # =====================================================

        self.smile_active = False

        self.pout_active = False

        self.mouth_open_active = False

    def can_trigger(self):

        return time.time() - self.last_action_time > self.cooldown

    def process(self, data):

        current_time = time.time()

        mouth_open = data["mouth_open"]

        mouth_width = data["mouth_width"]

        # =====================================================
        # Gesture Conditions
        # =====================================================

        is_mouth_open = mouth_open > 0.08

        is_smile = (
            mouth_width > 0.42
            and mouth_open < 0.07
        )

        is_pout = (
            mouth_width < 0.35
            and mouth_open < 0.05
        )

        # =====================================================
        # PRIORITY 1:
        # MOUTH OPEN -> PAUSE/PLAY
        # =====================================================

        if is_mouth_open:

            if not self.mouth_open_active and self.can_trigger():

                screen_width, screen_height = pyautogui.size()

                pyautogui.click(
                    x=screen_width // 2,
                    y=screen_height // 2
                )

                print("PAUSE / PLAY")

                self.last_action_time = current_time

                self.mouth_open_active = True

            return

        else:
            self.mouth_open_active = False

        # =====================================================
        # PRIORITY 2:
        # SMILE -> NEXT REEL
        # =====================================================

        if is_smile:

            if not self.smile_active and self.can_trigger():

                pyautogui.press('down')

                print("NEXT REEL")

                self.last_action_time = current_time

                self.smile_active = True

            return

        else:
            self.smile_active = False

        # =====================================================
        # PRIORITY 3:
        # POUT -> PREVIOUS REEL
        # =====================================================

        if is_pout:

            if not self.pout_active and self.can_trigger():

                pyautogui.press('up')

                print("PREVIOUS REEL")

                self.last_action_time = current_time

                self.pout_active = True

            return

        else:
            self.pout_active = False