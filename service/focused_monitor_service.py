import cv2
import pyautogui
import numpy as np
import time
import os
from monitor.viewer import Viewer

class FocusedMonitor:
    def __init__(self, icons_path=["assets/x_icon.png", "assets/pinterest_icon.png"], threshold=0.8):
        self.viewer = Viewer()
        self.template_paths = icons_path
        self.threshold = threshold
        self.templates = []

        for i_path in self.template_paths:
            if not os.path.exists(i_path):
                raise FileNotFoundError(f"Image not found {i_path}")

            template = cv2.imread(i_path, cv2.IMREAD_UNCHANGED)
            if template is None:
                raise ValueError(f"Unable to load image - {i_path}")

            template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
            w, h = template_gray.shape[::-1]
            self.templates.append((template_gray, w, h))

    def check_icon_on_screen(self) -> bool:
        screenshot = pyautogui.screenshot()
        screen_convert_np = np.array(screenshot)
        screen_gray_temp = cv2.cvtColor(screen_convert_np, cv2.COLOR_RGB2GRAY)

        for template_gray, w, h in self.templates:
            result = cv2.matchTemplate(screen_gray_temp, template_gray, cv2.TM_CCOEFF_NORMED)
            loc = np.where(result >= self.threshold)
            if len(loc[0]) > 0:
                return True

        return False

    def monitor(self) -> None:
        try:
            while True:
                if self.check_icon_on_screen():
                    print("Out of focus \r")
                    if not self.viewer.which_state():
                        self.viewer.show_focused_mensage()
                else:
                    print("Focused \r")
                    if self.viewer.which_state():
                        self.viewer.destroy_viewer()

                time.sleep(1)
        except KeyboardInterrupt:
            self.viewer.destroy_viewer()
            