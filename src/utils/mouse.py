import pyautogui
from utils.logger import log


def capture_mouse_coords():
    log.info("Move mouse to desired location. Press Ctrl-C to capture coords.")
    try:
        while True:
            x, y = pyautogui.position()
            position_str = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
            print(position_str, end="")
            print("\b" * len(position_str), end="", flush=True)
    except KeyboardInterrupt:
        print("\n")
    return x, y
