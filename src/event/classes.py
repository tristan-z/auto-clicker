from enum import StrEnum
from utils.logger import log

EVENT_TYPES = StrEnum(
    "EVENT_TYPES",
    ["CLICK", "COLOR_CLICK", "IMAGE_CLICK", "DELAY", "NUM", "KEY", "TEXT"],
)


class Event:
    def __init__(self, type, notes):
        self.type = type
        self.notes = notes

    def print_notes(self):
        if self.notes:
            log.info(self.notes)

    def get_type(self) -> str:
        return self.type.__str__().upper()


class ClickEvent(Event):
    def __init__(self, event_type, click_type, pixel_offset, notes=None):
        super().__init__(event_type, notes)

        self.click_type = click_type
        self.pixel_offset = pixel_offset


class Click(ClickEvent):
    def __init__(self, click_type, pixel_offset, x_coord, y_coord, notes=None):
        super().__init__(EVENT_TYPES.CLICK, click_type, pixel_offset, notes)

        self.x_coord = x_coord
        self.y_coord = y_coord


class ClickColor(ClickEvent):
    def __init__(
        self,
        color,
        click_type,
        pixel_offset,
        x_coord_bounds,
        y_coord_bounds,
        notes=None,
    ):
        super().__init__(EVENT_TYPES.COLOR_CLICK, click_type, pixel_offset, notes)

        self.color = color
        self.x_coord_bounds = x_coord_bounds
        self.y_coord_bounds = y_coord_bounds


class ClickImage(ClickEvent):
    def __init__(
        self,
        click_type,
        image_location,
        pixel_offset,
        confidence,
        grayscale,
        notes=None,
    ):
        super().__init__(EVENT_TYPES.IMAGE_CLICK, click_type, pixel_offset, notes)

        self.image_location = image_location
        self.confidence = confidence
        self.grayscale = grayscale


class Delay(Event):
    def __init__(self, delay_time, time_offset, notes=None):
        super().__init__(EVENT_TYPES.DELAY, notes)

        self.delay_time = delay_time  # time in ms
        self.time_offset = time_offset  # range of time in ms offset


class Num(Event):
    def __init__(self, value, notes=None):
        super().__init__(EVENT_TYPES.NUM, notes)

        self.value = value


class Key(Event):
    def __init__(self, key, action, notes=None):
        super().__init__(EVENT_TYPES.KEY, notes)

        self.key = str(key)
        self.action = action


class Text(Event):
    def __init__(self, value, notes=None):
        super().__init__(EVENT_TYPES.TEXT, notes)

        self.value = value
