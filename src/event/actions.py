import pyautogui
import time
import random
from pynput import keyboard


from .constants import (
    LEFT_CLICK,
    RIGHT_CLICK,
    KEY_PRESS,
    KEY_HOLD,
    KEY_RELEASE,
    keyboard_key_map,
)


def perform_click(x, y, offset, type):
    if offset > 0:
        x += random.randint(-offset, offset)
        y += random.randint(-offset, offset)
    perform_delay(90, 15)
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
                perform_delay(70, 50)
    return x, y


def perform_image_click(
    type, image_path, offset, confidence, grayscale, region, attempts
):
    x, y = find_image(image_path, confidence, grayscale, region, attempts)
    perform_click(x, y, offset, type)


def perform_delay(length, offset):
    if offset > 0:
        length += random.randint(0, offset)
    time.sleep(length)


def perform_numpress(num):
    num = str(num)
    asciinum = ord(num)
    pyautogui.press(asciinum)


def perform_key_action(key, action):
    ascii_key = keyboard_key_map.get(key)
    if action == KEY_PRESS:
        pyautogui.press(ascii_key)
    elif action == KEY_HOLD:
        pyautogui.keyDown(ascii_key)
    elif action == KEY_RELEASE:
        pyautogui.keyUp(ascii_key)
    else:
        pyautogui.press(ascii_key)


key_press_buffer = []


def on_press(key):
    try:
        print("alphanumeric key {0} pressed".format(key.char))
        key_press_buffer.append(ord(key.char))
    except AttributeError:
        print("special key {0} pressed".format(key))
        print(type(key.value))
        key_press_buffer.append(key.value)


def on_release(key):
    print("{0} released".format(key))
    return False


def capture_key_press():
    # bypass releasing 'enter' that got us here
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    # read actual keyboard input
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    if len(key_press_buffer):
        return key_press_buffer[0]


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
