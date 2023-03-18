import json
from ..event import actions, constants
import win32api
import sys
import random

script_events = {}


# assumes min < max always
def calculate_value(value_obj):
    _min = value_obj["min"]
    _max = value_obj["max"]
    distribution = value_obj["distribution"]
    if _min == _max:
        return _min
    if distribution == "linear":
        return random.randint(_min, _max)


def handle_event(event):
    if should_cancel_script_execution():
        return False
    notes = event.get("notes")
    if False and notes:
        print(notes)
    event_type = event["type"]
    if event_type == constants.CLICK_TYPE:
        actions.perform_click(
            event["xCoord"], event["yCoord"], event["pixelOffset"], event["clickType"]
        )
    elif event_type == constants.DELAY_TYPE:
        actions.perform_delay(event["delayTime"], event["timeOffset"])
    elif event_type == constants.NUM_TYPE:
        actions.perform_numpress(event["value"])
    elif event_type == constants.KEY_TYPE:
        actions.perform_key_action(event["key"], event["action"])
    elif event_type == constants.TEXT_TYPE:
        print("Text: %s" % (event["pText"]))
    elif event_type == constants.IMAGE_CLICK_TYPE:
        actions.perform_image_click(
            event["clickType"],
            event["imagePath"],
            event["pixelOffset"],
            event.get("confidence"),
            event.get("grayscale"),
            event.get("region"),
            event.get("attempts"),
        )
    elif event_type == constants.IMAGE_FIND_TYPE:
        actions.find_image(
            event["imagePath"],
            event.get("confidence"),
            event.get("grayscale"),
            event.get("region"),
            event.get("attempts"),
        )
    return True


def execute_script(script_segment, parent_iteration=0):
    execution_modulo = script_segment.get("executionModulo")
    bypass_execution = execution_modulo and ((parent_iteration + 1) % execution_modulo)
    if not bypass_execution:
        itrs = calculate_value(script_segment["iterations"])
        for itr in range(itrs):
            if "children" in script_segment:
                for child in script_segment["children"]:
                    success = execute_script(child, itr)
                    if not success:
                        return False
            else:
                success = handle_event(script_segment)
                if not success:
                    return False
    return True


def run_script():
    if "iterations" not in script_events:
        return False
    else:
        print('\nOpen Desired Screen and Press "TAB" to Begin\n')
        while 1:
            if start_script_option():
                break
            actions.perform_delay(70, 0)
        print("\nRunning Script\n")
        success = execute_script(script_events)
        if not success:
            return False
        print("\nScript Completed\n")
        return True


def save_script(filename):
    try:
        # convert storage lists to json
        print("scriptEvents", script_events)
        script = json.dumps(script_events)
        orig_stdout = sys.stdout
        # write jsons to file
        fout = open(filename, "w")
        sys.stdout = fout
        print(script)
        sys.stdout = orig_stdout
        fout.close()
        print("Script Saved Successfully\n")
    except:
        print("\nScript Failed To Save\n")


def load_script(filename):
    global script_events
    try:
        script = open(filename, "r")
        script_events = json.load(script)
        script.close()
        print("\nScript Loaded Successfully\n")
    except:
        print("\nScript Failed To Load\n")


def should_cancel_script_execution():
    stopKey = constants.keyboard_key_map.get("F12")
    if win32api.GetKeyState(stopKey) & (1 << 7):
        return True
    return False


def start_script_option():
    # tab to start
    startKey = 9
    if win32api.GetKeyState(startKey) & (1 << 7):
        return True
    return False
