import random
import sys

from script.actions import load_script, run_script
from utils.mouse import capture_mouse_coords
from utils.logger import log


def run_auto_clicker(file_path):
    script = load_script(file_path)
    while 1:
        try:
            run_script(script)
        except KeyboardInterrupt:
            log.info("Exiting.")
            break
        except Exception as e:
            log.error("Error encountered when running script. {}".format(str(e)))


if __name__ == "__main__":
    random.seed()
    if len(sys.argv) == 1:
        capture_mouse_coords()
    else:
        try:
            file_path = sys.argv[1]
            run_auto_clicker(file_path)
        except Exception as e:
            log.error("Error Occurred", e)
            k = input("press close to exit")
            raise
