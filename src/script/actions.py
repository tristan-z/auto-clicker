import json
from jsonschema import validate, ValidationError
from event import constants
from pynput import keyboard
import sys
import schema_config
from utils.logger import log
from .exceptions import ScriptFileError, ScriptExecutionError
from .utils import calculate_value
from event import events


def handle_event(event_config):
    event = None

    event_type = event_config["type"]
    match event_type:
        case constants.CLICK_TYPE:
            event = events.Click(**event_config)
        case constants.DELAY_TYPE:
            event = events.Delay(**event_config)
        case constants.NUM_TYPE:
            event = events.Num(**event_config)
        case constants.KEY_TYPE:
            event = events.Key(**event_config)
        case constants.IMAGE_CLICK_TYPE:
            event = events.ClickImage(**event_config)
        case constants.IMAGE_FIND_TYPE:
            event = events.FindImage(**event_config)

    if event == None:
        raise ScriptExecutionError("Failed to execute event")
    event.print_notes()
    event.execute()


def execute_script(script_segment, parent_iteration=0):
    execution_modulo = script_segment.get("executionModulo")
    bypass_execution = execution_modulo and ((parent_iteration + 1) % execution_modulo)
    if not bypass_execution:
        itrs = calculate_value(script_segment["iterations"])
        for itr in range(itrs):
            if "children" in script_segment:
                for child in script_segment["children"]:
                    execute_script(child, itr)
            else:
                handle_event(script_segment)
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
        raise ScriptFileError("Could not find iterations config in script.")
    else:
        log.info('Press "TAB" to Begin.  Press Ctrl+C to exit.\n')
        with keyboard.Listener(
            on_press=on_key_press, on_release=on_key_release
        ) as listener:
            listener.join()

        log.info("Starting Script. Press Ctrl+C to stop.\n")
        try:
            execute_script(script)
        except KeyboardInterrupt:
            log.info("Script Stopped.")
        else:
            log.info("Script Completed\n")


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
