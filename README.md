# auto-clicker

Automate mouse and keyboard events.

---

## Dependencies

- python 3.10+

---

## Setup

Run `make` to initiate setup.

---

## Usage

### Visualize Mouse Coordinates

From `src` execute the following:

```
python3 main.py
```

### Execute Script

Create a script file, following the format enforced by the JSON Schema: `scripts/docs/auto-clicker-input.schema.json`

A sample script can be found in `scripts/sample.json`

Schema docs can be found in `scripts/docs`

From `src` execute the following:

```
python3 main.py scripts/sample.json
```

---

## Logging

Logs will be written to a date-stamped file in `logs` by default.

To disable writing to log file, configure the `WRITE_LOGS` environment variable to `false`

To change the log level, configure the `LOG_LEVEL` environment variable to an `int` associated with the [desired level](https://docs.python.org/3/library/logging.html#levels).
