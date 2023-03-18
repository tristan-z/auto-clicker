import pyautogui
import win32api
import win32con
import random
import msvcrt
from pynput import keyboard


from .constants import LEFT_CLICK, RIGHT_CLICK, KEY_PRESS, KEY_HOLD, KEY_RELEASE, keyboard_key_map


def perform_click(x, y, offset, type):
    if offset > 0:
        x += random.randint(-offset, offset)
        y += random.randint(-offset, offset)
    win32api.SetCursorPos((x, y))
    perform_delay(90, 15)
    if type == LEFT_CLICK:
        #pyautogui.click(x, y)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    elif type == RIGHT_CLICK:
        #pyautogui.click(x, y, button='right')
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, x, y, 0, 0)


def find_image(image_path, confidence=0.6, grayscale=False, region=None, attempts=1):
    if region:
        region = tuple(region)
    x = y = 0
    for attempt in range(attempts):
        try:
            x, y = pyautogui.locateCenterOnScreen(
                image_path, confidence=confidence, grayscale=grayscale, region=region)
            break
        except:
            if attempt + 1 >= attempts:
                raise Exception('Image not found within configured attempts.')
            else:
                perform_delay(70, 50)
    return x, y


def perform_image_click(type, image_path, offset, confidence, grayscale, region, attempts):
    x, y = find_image(image_path, confidence, grayscale, region, attempts)
    perform_click(x, y, offset, type)


def perform_delay(length, offset):
    if offset > 0:
        length += random.randint(0, offset)
    win32api.Sleep(length)


def perform_numpress(num):
    num = str(num)
    asciinum = ord(num)
    win32api.keybd_event(asciinum, 0, )


def key_hold(key):
    win32api.keybd_event(key, 0, 1, 0)


def key_release(key):
    win32api.keybd_event(
        key, 0, win32con.KEYEVENTF_EXTENDEDKEY | win32con.KEYEVENTF_KEYUP, 0)


def key_press(key):
    key_hold(key)
    perform_delay(80, 80)


def perform_key_action(key, action):
    ascii_key = keyboard_key_map.get(key)
    if action == KEY_PRESS:
        key_press(ascii_key)
    elif action == KEY_HOLD:
        key_hold(ascii_key)
    elif action == KEY_RELEASE:
        key_release(ascii_key)
    else:
        win32api.keybd_event(ascii_key, 0, 0, 0)
        win32api.keybd_event(ascii_key, 0, win32con.KEYEVENTF_KEYUP, 0)


key_press_buffer = []


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        key_press_buffer.append(ord(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        print(type(key.value))
        key_press_buffer.append(key.value)


def on_release(key):
    print('{0} released'.format(
        key))
    return False


def capture_key_press():
    # bypass releasing 'enter' that got us here
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    # read actual keyboard input
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    print('tristan kpb', key_press_buffer)
    if len(key_press_buffer):
        return key_press_buffer[0]


def capture_mouse_coords():
    print("Move mouse to desired location and\npress any key to capture coords")
    while True:
        x, y = pyautogui.position()
        win32api.Sleep(500)
        print("x: %d, y: %d" % (x, y))
        # check for keyboard interrupt
        if msvcrt.kbhit() and ord(msvcrt.getch()) != None:
            break
    print("x: %d, y: %d" % (x, y))
    return x, y
