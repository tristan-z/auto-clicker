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
                            "clickType": {"enum": ["LEFT_CLICK", "RIGHT_CLICK"]},
                            "pixelOffset": {"type": "integer"},
                            "xCoord": {"type": "integer"},
                            "yCoord": {"type": "integer"},
                            "executionModulo": {"$ref": "#/$defs/executionModulo"},
                            "iterations": {"$ref": "#/$defs/iterations"},
                        },
                        "required": ["iterations"],
                    },
                    {
                        "type": "object",
                        "properties": {
                            "notes": {"$ref": "#/$defs/notes"},
                            "type": {"const": "DELAY"},
                            "delayTime": {"type": "integer"},
                            "timeOffset": {"type": "integer"},
                            "executionModulo": {"$ref": "#/$defs/executionModulo"},
                            "iterations": {"$ref": "#/$defs/iterations"},
                        },
                        "required": ["iterations"],
                    },
                    {
                        "type": "object",
                        "properties": {
                            "notes": {"$ref": "#/$defs/notes"},
                            "type": {"const": "KEY"},
                            "clickType": {
                                "enum": ["KEY_PRESS", "KEY_HOLD", "KEY_RELEASE"]
                            },
                            "key": {"enum": KEYBOARD_KEYS},
                            "executionModulo": {"$ref": "#/$defs/executionModulo"},
                            "iterations": {"$ref": "#/$defs/iterations"},
                        },
                        "required": ["iterations"],
                    },
                    {
                        "type": "object",
                        "properties": {
                            "notes": {"$ref": "#/$defs/notes"},
                            "type": {"const": "IMAGE_CLICK"},
                            "clickType": {"enum": ["LEFT_CLICK", "RIGHT_CLICK"]},
                            "pixelOffset": {"type": "integer"},
                            "imagePath": {"type": "string"},
                            "confidence": {"type": "number"},
                            "grayscale": {"type": "boolean"},
                            "region": {
                                "type": "array",
                                "contains": {"type": "integer"},
                                "length": 4,
                            },
                            "attempts": {"type": "integer"},
                            "executionModulo": {"$ref": "#/$defs/executionModulo"},
                            "iterations": {"$ref": "#/$defs/iterations"},
                        },
                        "required": ["iterations"],
                    },
                    {
                        "type": "object",
                        "properties": {
                            "notes": {"$ref": "#/$defs/notes"},
                            "type": {"const": "IMAGE_FIND"},
                            "imagePath": {"type": "string"},
                            "confidence": {"type": "number"},
                            "grayscale": {"type": "boolean"},
                            "region": {
                                "type": "array",
                                "contains": {"type": "integer"},
                                "length": 4,
                            },
                            "attempts": {"type": "integer"},
                            "executionModulo": {"$ref": "#/$defs/executionModulo"},
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
        "executionModulo": {"type": "integer"},
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
