from pyautogui import KEYBOARD_KEYS

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
                            "click_type": {"enum": ["LEFT_CLICK", "RIGHT_CLICK"]},
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
                            "click_type": {
                                "enum": ["KEY_PRESS", "KEY_HOLD", "KEY_RELEASE"]
                            },
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
                            "click_type": {"enum": ["LEFT_CLICK", "RIGHT_CLICK"]},
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
