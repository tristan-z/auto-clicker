from enum import StrEnum

EVENT_TYPES = StrEnum(
    "EVENT_TYPES",
    [
        "CLICK",
        "COLOR_CLICK",
        "IMAGE_CLICK",
        "IMAGE_FIND",
        "DELAY",
        "NUM",
        "KEY",
        "TEXT",
    ],
)

KEY_ACTIONS = StrEnum("KEY_ACTIONS", ["press", "release", "hold"])

CLICK_TYPES = StrEnum("CLICK_TYPES", ["left", "right"])
