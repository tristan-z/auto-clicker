import pyautogui
import time
import random


from .constants import (
    LEFT_CLICK,
    RIGHT_CLICK,
    KEY_PRESS,
    KEY_HOLD,
    KEY_RELEASE,
)


def perform_click(x, y, offset, type):
    if offset > 0:
        x += random.randint(-offset, offset)
        y += random.randint(-offset, offset)
    perform_delay_ms(90, 15)
    if type == LEFT_CLICK:
        pyautogui.click(x, y)
    elif type == RIGHT_CLICK:
        pyautogui.click(x, y, button="right")


def find_image(image_path, confidence=0.6, grayscale=False, region=None, attempts=1):
    if region:
        region = tuple(region)
    x = y = 0
    for attempt in range(attempts):
        try:
            x, y = pyautogui.locateCenterOnScreen(
                image_path, confidence=confidence, grayscale=grayscale, region=region
            )
            break
        except:
            if attempt + 1 >= attempts:
                raise Exception("Image not found within configured attempts.")
            else:
                perform_delay_ms(70, 50)
    return x, y


def perform_image_click(
    type, image_path, offset, confidence, grayscale, region, attempts
):
    x, y = find_image(image_path, confidence, grayscale, region, attempts)
    perform_click(x, y, offset, type)


def perform_delay_ms(length, offset):
    if offset > 0:
        length += random.randint(0, offset)
    time.sleep(length / 1000)


def perform_numpress(num):
    num = str(num)
    asciinum = ord(num)
    pyautogui.press(asciinum)


def perform_key_action(key, action):
    if action == KEY_PRESS:
        pyautogui.press(key)
    elif action == KEY_HOLD:
        pyautogui.keyDown(key)
    elif action == KEY_RELEASE:
        pyautogui.keyUp(key)
    else:
        pyautogui.press(key)


def capture_mouse_coords():
    print("Move mouse to desired location. Press Ctrl-C to capture coords.")
    try:
        while True:
            x, y = pyautogui.position()
            position_str = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
            print(position_str, end="")
            print("\b" * len(position_str), end="", flush=True)
    except KeyboardInterrupt:
        print("\n")
    return x, y
