import json
from jsonschema import validate, ValidationError
from event import actions, constants
from pynput import keyboard
import sys
import random
import schema_config


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
    """if should_cancel_script_execution():
    return False"""
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


def on_key_press(key):
    try:
        print("alphanumeric key {0} pressed".format(key.char))
    except AttributeError:
        print("special key {0} pressed".format(key))


def on_key_release(key):
    print("{0} released".format(key))
    if key == keyboard.Key.tab:
        # Stop listener
        return False


def run_script(script):
    if "iterations" not in script:
        return False
    else:
        print('\nOpen Desired Screen and Press "TAB" to Begin\n')
        with keyboard.Listener(
            on_press=on_key_press, on_release=on_key_release
        ) as listener:
            listener.join()
        print("\nRunning Script\n")
        success = execute_script(script)
        if not success:
            return False
        print("\nScript Completed\n")
        return True


def save_script(filename, script):
    try:
        # convert storage lists to json
        _script = json.dumps(script)
        orig_stdout = sys.stdout
        # write jsons to file
        fout = open(filename, "w")
        sys.stdout = fout
        print(script)
        sys.stdout = orig_stdout
        fout.close()
        print("\nScript Saved Successfully\n")
    except:
        print("\nScript Failed To Save\n")


def load_script(filename):
    try:
        f = open(filename, "r")
        script = json.load(f)
        f.close()
        validate(instance=script, schema=schema_config.schema)
        print("\nScript Loaded Successfully\n")
        return script
    except ValidationError as e:
        raise Exception("\nInvalid JSON format:\n{}\n".format(str(e)))
    except Exception as e:
        raise Exception("\nScript Failed To Load:\n{}\n".format(str(e)))
