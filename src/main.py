import random
import sys

from script.actions import load_script, run_script
from event.actions import capture_mouse_coords


def run_auto_clicker(file_path):
    load_script(file_path)
    while 1:
        run_script()


if __name__ == "__main__":
    random.seed()
    if len(sys.argv) > 1:
        capture_mouse_coords()
    try:
        file_path = sys.argv[1]
        run_auto_clicker(file_path)
    except Exception as e:
        print("Error Occurred", e)
        k = input("press close to exit")
        raise
