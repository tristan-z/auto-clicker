import sys
import json
from pyautogui import KEYBOARD_KEYS
from event.constants import CLICK_TYPES, KEY_ACTIONS
from utils.logger import log

schema = {
    "$id": "auto-clicker-input.schema.json",
    "title": "Auto Clicker Input",
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "notes": {"$ref": "#/$defs/notes"},
        "children": {
            "title": "Events",
            "type": "array",
            "items": {
                "anyOf": [
                    {
                        "title": "Click",
                        "type": "object",
                        "properties": {
                            "notes": {"$ref": "#/$defs/notes"},
                            "type": {"const": "CLICK"},
                            "click_type": {"$ref": "#/$defs/click_type"},
                            "pixel_offset": {"type": "integer"},
                            "coords": {
                                "title": "coords",
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
                        "title": "Delay",
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
                        "title": "Key",
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
                        "title": "Image Click",
                        "type": "object",
                        "properties": {
                            "notes": {"$ref": "#/$defs/notes"},
                            "type": {"const": "IMAGE_CLICK"},
                            "click_type": {"$ref": "#/$defs/click_type"},
                            "pixel_offset": {"type": "integer"},
                            "image_path": {"type": "string"},
                            "confidence": {"type": "number"},
                            "grayscale": {"type": "boolean"},
                            "region": {"$ref": "#/$defs/region"},
                            "attempts": {"type": "integer"},
                            "execution_modulo": {"$ref": "#/$defs/execution_modulo"},
                            "iterations": {"$ref": "#/$defs/iterations"},
                        },
                        "required": ["iterations"],
                    },
                    {
                        "title": "Image Find",
                        "type": "object",
                        "properties": {
                            "notes": {"$ref": "#/$defs/notes"},
                            "type": {"const": "IMAGE_FIND"},
                            "image_path": {"type": "string"},
                            "confidence": {"type": "number"},
                            "grayscale": {"type": "boolean"},
                            "region": {"$ref": "#/$defs/region"},
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
        "click_type": {"type": "string", "enum": [t.__str__() for t in CLICK_TYPES]},
        "iterations": {
            "title": "iterations",
            "type": "object",
            "properties": {
                "min": {"type": "integer"},
                "max": {"type": "integer"},
                "distribution": {"type": "string", "enum": ["linear"]},
            },
            "required": ["min", "max", "distribution"],
        },
        "region": {
            "title": "region",
            "type": "array",
            "contains": {"type": "integer"},
            "length": 4,
        },
    },
}

OUTPUT_FILE = "../scripts/docs/auto-clicker-input.schema.json"


def generate_schema_json(output_file):
    with open(output_file, "w") as fp:
        json.dump(schema, fp)


if __name__ == "__main__":
    output_file = OUTPUT_FILE
    if len(sys.argv) == 2:
        output_path = sys.argv[1]
    try:
        generate_schema_json(output_file)
    except Exception:
        log.error("Failed to generate schema json file.")
