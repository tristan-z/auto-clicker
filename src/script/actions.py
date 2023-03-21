import json
from jsonschema import validate, ValidationError
from event.constants import EVENT_TYPES
from pynput import keyboard
import sys
import schema_config
from utils.logger import log, log_if_exists
from .exceptions import ScriptFileError, ScriptExecutionError
from .utils import calculate_itr_count, bypass_iteration
from event import events


def handle_event(event_config):
    event = None

    event_type = EVENT_TYPES[event_config["type"]]
    match event_type:
        case EVENT_TYPES.CLICK:
            event = events.Click(**event_config)
        case EVENT_TYPES.DELAY:
            event = events.Delay(**event_config)
        case EVENT_TYPES.NUM:
            event = events.Num(**event_config)
        case EVENT_TYPES.KEY:
            event = events.Key(**event_config)
        case EVENT_TYPES.IMAGE_CLICK:
            event = events.ClickImage(**event_config)
        case EVENT_TYPES.IMAGE_FIND:
            event = events.FindImage(**event_config)

    if event == None:
        raise ScriptExecutionError("Failed to execute event")

    event.execute()


def execute_script(script_segment, parent_iter=0):
    if not bypass_iteration(script_segment.get("execution_modulo"), parent_iter + 1):
        log_if_exists(script_segment.get("notes"))
        itrs = calculate_itr_count(script_segment["iterations"])
        for itr in range(itrs):
            if "children" in script_segment:
                for child in script_segment["children"]:
                    execute_script(child, itr)
            else:
                handle_event(script_segment)


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
            log.info("Script Completed.")


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
