import os
import logging
from datetime import date

today = date.today()

LOGS_PATH = "../logs/"
LOG_FILE = LOGS_PATH + today.strftime("%b-%d-%Y") + "-debug.log"
LOG_LEVEL = int(os.getenv("LOG_LEVEL", logging.DEBUG))
LOG_FORMAT = "%(asctime)s - %(levelname)s: %(message)s"
WRITE_LOGS = os.getenv("WRITE_LOGS", "").lower() != "false"

logging.basicConfig(format=LOG_FORMAT)

log = logging.getLogger("autoclicker")
log.setLevel(LOG_LEVEL)

# write logs to log file
if WRITE_LOGS:
    handler = logging.FileHandler(LOG_FILE)
    formatter = logging.Formatter(LOG_FORMAT)
    handler.setFormatter(formatter)

    log.addHandler(handler)
