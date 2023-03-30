import pyautogui
import random
import time
from abc import ABC, abstractclassmethod
from utils.logger import log, log_if_exists
from .exceptions import FindImageError
from .constants import EVENT_TYPES, KEY_ACTIONS, CLICK_TYPES


"""
Event Base Classes
"""


class Event(ABC):
    def __init__(self, event_type, notes=None, **kwargs):
        self.type = event_type
        self.notes = notes

    def print_notes(self):
        log_if_exists(self.notes)

    def get_type_str(self) -> str:
        return self.type.__str__()

    @abstractclassmethod
    def execute(self):
        pass


class ImageEvent(Event):
    def __init__(
        self,
        event_type,
        image_path,
        confidence=0.6,
        grayscale=False,
        region=None,
        attempts=1,
        notes=None,
        **kwargs,
    ):
        super().__init__(event_type, notes)

        self.image_path = image_path
        self.confidence = confidence
        self.grayscale = grayscale
        self.region = region
        self.attempts = attempts

    @staticmethod
    def find_image(
        image_path, confidence=0.6, grayscale=False, region=None, attempts=1
    ):
        if region:
            region = tuple(region)
        x, y = 0, 0
        for attempt in range(attempts):
            try:
                x, y = pyautogui.locateCenterOnScreen(
                    image=image_path,
                    confidence=confidence,
                    grayscale=grayscale,
                    region=region,
                )
                break
            except (pyautogui.ImageNotFoundException, Exception):
                if attempt + 1 >= attempts:
                    raise FindImageError("Image not found within configured attempts.")
                else:
                    log.debug("Image not found, retrying search.")
                    Delay.perform_delay_ms(70, 50)
        return x, y


class ClickEvent(Event):
    def __init__(self, event_type, click_type, pixel_offset, notes=None, **kwargs):
        super().__init__(event_type, notes)

        self.click_type = click_type
        self.pixel_offset = pixel_offset

    @staticmethod
    def perform_click(coords, click_type, pixel_offset=0):
        x, y = coords
        if pixel_offset > 0:
            x += random.randint(-pixel_offset, pixel_offset)
            y += random.randint(-pixel_offset, pixel_offset)
        button = CLICK_TYPES[click_type].__str__()
        pyautogui.click(x, y, button=button)


"""
Event Classes
"""


class Click(ClickEvent):
    def __init__(self, click_type, pixel_offset, coords, notes=None, **kwargs):
        super().__init__(EVENT_TYPES.CLICK, click_type, pixel_offset, notes)

        self.coords = coords

    def execute(self):
        super().perform_click(self.coords, self.click_type, self.pixel_offset)


class ClickImage(ImageEvent):
    def __init__(
        self,
        click_type,
        pixel_offset,
        image_path,
        **kwargs,
    ):
        super().__init__(EVENT_TYPES.IMAGE_FIND, image_path, **kwargs)
        self.click_type = click_type
        self.pixel_offset = pixel_offset

    @staticmethod
    def perform_image_click(
        click_type, image_path, offset, confidence, grayscale, region, attempts
    ):
        x, y = ImageEvent.find_image(
            image_path, confidence, grayscale, region, attempts
        )
        log.debug("Center of image found: ({},{})".format(str(x), str(y)))
        # TODO: investigate if the x,y "//2" logic works on all sceen res
        ClickEvent.perform_click([x // 2, y // 2], click_type, offset)

    def execute(self):
        self.perform_image_click(
            self.click_type,
            self.image_path,
            self.pixel_offset,
            self.confidence,
            self.grayscale,
            self.region,
            self.attempts,
        )


class FindImage(ImageEvent):
    def __init__(
        self,
        image_path,
        confidence,
        grayscale,
        region,
        attempts,
        notes,
        **kwargs,
    ):
        super().__init__(
            EVENT_TYPES.IMAGE_FIND,
            image_path,
            confidence,
            grayscale,
            region,
            attempts,
            notes,
        )

    def execute(self):
        super().find_image(
            self.image_path, self.confidence, self.grayscale, self.region, self.attempts
        )


class Delay(Event):
    def __init__(self, delay_time, time_offset, notes=None, **kwargs):
        super().__init__(EVENT_TYPES.DELAY, notes)

        self.delay_time = delay_time  # time in ms
        self.time_offset = time_offset  # range of time in ms offset

    @staticmethod
    def perform_delay_ms(length, offset):
        if offset > 0:
            length += random.randint(0, offset)
        time.sleep(length / 1000)

    def execute(self):
        self.perform_delay_ms(self.delay_time, self.time_offset)


class Num(Event):
    def __init__(self, value, notes=None, **kwargs):
        super().__init__(EVENT_TYPES.NUM, notes)

        self.value = value

    @staticmethod
    def perform_numpress(num):
        num = str(num)
        asciinum = ord(num)
        pyautogui.press(asciinum)

    def execute(self):
        self.perform_numpress(self.value)


class Key(Event):
    def __init__(self, key, action, notes=None, **kwargs):
        super().__init__(EVENT_TYPES.KEY, notes)

        self.key = str(key)
        self.action = action

    @staticmethod
    def perform_key_action(key, action):
        match KEY_ACTIONS[action]:
            case KEY_ACTIONS.press:
                pyautogui.press(key)
            case KEY_ACTIONS.hold:
                pyautogui.keyDown(key)
            case KEY_ACTIONS.release:
                pyautogui.keyUp(key)
            case _:
                pyautogui.press(key)

    def execute(self):
        self.perform_key_action(self.key, self.action)
