from pyautogui import KEYBOARD_KEYS
from event.constants import CLICK_TYPES, KEY_ACTIONS

schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "notes": {"$ref": "#/$defs/notes"},
        "children": {
            "type": "array",
            "items": {
                "anyOf": [
                    {
                        "type": "object",
                        "properties": {
                            "notes": {"$ref": "#/$defs/notes"},
                            "type": {"const": "CLICK"},
                            "click_type": {"$ref": "#/$defs/click_type"},
                            "pixel_offset": {"type": "integer"},
                            "coords": {
                                "type": "array",
                                "contains": {"type": "integer"},
                                "length": 2,
                            },
                            "execution_modulo": {"$ref": "#/$defs/execution_modulo"},
                            "iterations": {"$ref": "#/$defs/iterations"},
                        },
                        "required": ["iterations", "click_type"],
                    },
                    {
                        "type": "object",
                        "properties": {
                            "notes": {"$ref": "#/$defs/notes"},
                            "type": {"const": "DELAY"},
                            "delay_time": {"type": "integer"},
                            "time_offset": {"type": "integer"},
                            "execution_modulo": {"$ref": "#/$defs/execution_modulo"},
                            "iterations": {"$ref": "#/$defs/iterations"},
                        },
                        "required": ["iterations"],
                    },
                    {
                        "type": "object",
                        "properties": {
                            "notes": {"$ref": "#/$defs/notes"},
                            "type": {"const": "KEY"},
                            "click_type": {"enum": [k.__str__() for k in KEY_ACTIONS]},
                            "key": {"enum": KEYBOARD_KEYS},
                            "execution_modulo": {"$ref": "#/$defs/execution_modulo"},
                            "iterations": {"$ref": "#/$defs/iterations"},
                        },
                        "required": ["iterations"],
                    },
                    {
                        "type": "object",
                        "properties": {
                            "notes": {"$ref": "#/$defs/notes"},
                            "type": {"const": "IMAGE_CLICK"},
                            "click_type": {"$ref": "#/$defs/click_type"},
                            "pixel_offset": {"type": "integer"},
                            "image_path": {"type": "string"},
                            "confidence": {"type": "number"},
                            "grayscale": {"type": "boolean"},
                            "region": {
                                "type": "array",
                                "contains": {"type": "integer"},
                                "length": 4,
                            },
                            "attempts": {"type": "integer"},
                            "execution_modulo": {"$ref": "#/$defs/execution_modulo"},
                            "iterations": {"$ref": "#/$defs/iterations"},
                        },
                        "required": ["iterations"],
                    },
                    {
                        "type": "object",
                        "properties": {
                            "notes": {"$ref": "#/$defs/notes"},
                            "type": {"const": "IMAGE_FIND"},
                            "image_path": {"type": "string"},
                            "confidence": {"type": "number"},
                            "grayscale": {"type": "boolean"},
                            "region": {
                                "type": "array",
                                "contains": {"type": "integer"},
                                "length": 4,
                            },
                            "attempts": {"type": "integer"},
                            "execution_modulo": {"$ref": "#/$defs/execution_modulo"},
                            "iterations": {"$ref": "#/$defs/iterations"},
                        },
                        "required": ["iterations"],
                    },
                ],
            },
        },
        "iterations": {"$ref": "#/$defs/iterations"},
    },
    "required": ["children", "iterations"],
    "$defs": {
        "notes": {"type": "string"},
        "execution_modulo": {"type": "integer"},
        "click_type": {"enum": [t.__str__() for t in CLICK_TYPES]},
        "iterations": {
            "type": "object",
            "properties": {
                "min": {"type": "integer"},
                "max": {"type": "integer"},
                "distribution": {"type": "string", "enum": ["linear"]},
            },
            "required": ["min", "max", "distribution"],
        },
    },
}
