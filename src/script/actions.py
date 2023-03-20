import json
from jsonschema import validate, ValidationError
from event import actions, constants
from pynput import keyboard
import sys
import schema_config
from utils.logger import log
from .exceptions import ScriptFileError
from .utils import calculate_value


def handle_event(event):
    notes = event.get("notes")
    if notes:
        print(notes)
    event_type = event["type"]
    if event_type == constants.CLICK_TYPE:
        actions.perform_click(
            event["xCoord"], event["yCoord"], event["pixelOffset"], event["clickType"]
        )
    elif event_type == constants.DELAY_TYPE:
        actions.perform_delay_ms(event["delayTime"], event["timeOffset"])
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
        log.debug("alphanumeric key {0} pressed".format(key.char))
    except AttributeError:
        log.debug("special key {0} pressed".format(key))


def on_key_release(key):
    log.debug("{0} released".format(key))
    if key == keyboard.Key.tab:
        # Stop listener
        return False


def run_script(script):
    if "iterations" not in script:
        return False
    else:
        log.info('Open Desired Screen and Press "TAB" to Begin\n')
        with keyboard.Listener(
            on_press=on_key_press, on_release=on_key_release
        ) as listener:
            listener.join()

        log.info("\nStarting Script\n")
        success = execute_script(script)
        if not success:
            return False
        log.info("Script Completed\n")
        return True


def save_script(filename, script):
    try:
        # convert storage lists to json
        _script = json.dumps(script)
        orig_stdout = sys.stdout
        # write jsons to file
        fout = open(filename, "w")
        sys.stdout = fout
        log.debug(_script)
        sys.stdout = orig_stdout
        fout.close()
        log.info("Script Saved Successfully\n")
    except Exception as e:
        raise ScriptFileError("Script Failed To Save:\n{}\n".format(str(e)))


def load_script(filename):
    try:
        f = open(filename, "r")
        script = json.load(f)
        f.close()
        validate(instance=script, schema=schema_config.schema)
        log.info("Script Loaded Successfully\n")
        return script
    except ValidationError as e:
        raise ScriptFileError("Invalid Script format:\n{}\n".format(str(e)))
    except Exception as e:
        raise ScriptFileError("Script Failed To Load:\n{}\n".format(str(e)))
