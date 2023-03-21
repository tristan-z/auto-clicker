import unittest
from unittest.mock import patch, MagicMock, mock_open
from event.constants import EVENT_TYPES
from script.actions import handle_event, run_script, execute_script, load_script
from script.exceptions import ScriptFileError

upper_str_of_enum = lambda e: e.__str__().upper()


class TestHandleEvent(unittest.TestCase):
    @patch("event.events.Click")
    def test_handle_click_event(self, mock_click):
        event_config = {
            "type": upper_str_of_enum(EVENT_TYPES.CLICK),
            "coords": [100, 200],
        }
        handle_event(event_config)
        mock_click.assert_called_with(**event_config)
        mock_click.return_value.print_notes.assert_called_once()
        mock_click.return_value.execute.assert_called_once()

    @patch("event.events.Delay")
    def test_handle_delay_event(self, mock_delay):
        event_config = {"type": upper_str_of_enum(EVENT_TYPES.DELAY), "delay_time": 5}
        handle_event(event_config)
        mock_delay.assert_called_with(**event_config)
        mock_delay.return_value.print_notes.assert_called_once()
        mock_delay.return_value.execute.assert_called_once()

    @patch("event.events.Num")
    def test_handle_num_event(self, mock_num):
        event_config = {"type": upper_str_of_enum(EVENT_TYPES.NUM), "value": 123}
        handle_event(event_config)
        mock_num.assert_called_with(**event_config)
        mock_num.return_value.print_notes.assert_called_once()
        mock_num.return_value.execute.assert_called_once()

    @patch("event.events.Key")
    def test_handle_key_event(self, mock_num):
        event_config = {"type": upper_str_of_enum(EVENT_TYPES.KEY), "key": 123}
        handle_event(event_config)
        mock_num.assert_called_with(**event_config)
        mock_num.return_value.print_notes.assert_called_once()
        mock_num.return_value.execute.assert_called_once()

    @patch("event.events.ClickImage")
    def test_handle_click_image_event(self, mock_num):
        event_config = {
            "type": upper_str_of_enum(EVENT_TYPES.IMAGE_CLICK),
            "pixel_offset": 123,
        }
        handle_event(event_config)
        mock_num.assert_called_with(**event_config)
        mock_num.return_value.print_notes.assert_called_once()
        mock_num.return_value.execute.assert_called_once()

    @patch("event.events.FindImage")
    def test_handle_find_image_event(self, mock_num):
        event_config = {
            "type": upper_str_of_enum(EVENT_TYPES.IMAGE_FIND),
            "confidence": 123,
        }
        handle_event(event_config)
        mock_num.assert_called_with(**event_config)
        mock_num.return_value.print_notes.assert_called_once()
        mock_num.return_value.execute.assert_called_once()

    @patch("event.events.Delay")
    @patch("event.events.Click")
    def test_handle_click_event(self, mock_click, mock_delay):
        event_config = {
            "type": upper_str_of_enum(EVENT_TYPES.CLICK),
            "coords": [100, 200],
        }
        handle_event(event_config)
        mock_click.assert_called_with(**event_config)
        mock_click.return_value.print_notes.assert_called_once()
        mock_click.return_value.execute.assert_called_once()
        mock_delay.assert_not_called()


class TestRunScript(unittest.TestCase):
    @patch("script.actions.keyboard")
    def test_run_script_invalid_script(self, _):
        script = {}
        with self.assertRaises(ScriptFileError):
            run_script(script)

    @patch("script.actions.execute_script")
    @patch("script.actions.keyboard")
    def test_run_script_iterations_in_script(self, mock_keyboard, mock_execute_script):
        script = {"iterations": 10}
        run_script(script)

        mock_keyboard.Listener.assert_called()
        mock_execute_script.assert_called()


class TestExecuteScript(unittest.TestCase):
    @patch("script.actions.handle_event")
    def test_execute_script_no_children(self, mock_handle_event):
        script_segment = {
            "iterations": {"min": 2, "max": 2, "distribution": "linear"},
            "execution_modulo": None,
        }
        execute_script(script_segment)

        mock_handle_event.assert_called_with(script_segment)

    @patch("script.actions.handle_event")
    def test_execute_script_with_children(self, mock_handle_event):
        parent_itrs, child1_itrs, child2_itrs = 2, 2, 3
        script_segment = {
            "iterations": {
                "min": parent_itrs,
                "max": parent_itrs,
                "distribution": "linear",
            },
            "children": [
                {
                    "iterations": {
                        "min": child1_itrs,
                        "max": child1_itrs,
                        "distribution": "linear",
                    },
                    "execution_modulo": None,
                },
                {
                    "iterations": {
                        "min": child2_itrs,
                        "max": child2_itrs,
                        "distribution": "linear",
                    },
                    "execution_modulo": None,
                },
            ],
            "execution_modulo": None,
        }
        execute_script(script_segment)

        expected_call_count = parent_itrs * (child1_itrs + child2_itrs)
        self.assertEqual(mock_handle_event.call_count, expected_call_count)

    @patch("script.actions.handle_event")
    def test_execute_script_with_execution_modulo(self, mock_handle_event):
        parent_itrs, child_itrs = 2, 3
        child_mod = 2
        script_segment = {
            "iterations": {
                "min": parent_itrs,
                "max": parent_itrs,
                "distribution": "linear",
            },
            "children": [
                {
                    "type": "DELAY",
                    "delay_time": 1000,
                    "time_offset": 100,
                    "iterations": {
                        "min": child_itrs,
                        "max": child_itrs,
                        "distribution": "linear",
                    },
                    "execution_modulo": child_mod,
                },
            ],
        }
        execute_script(script_segment)

        expected_parent_call_count = parent_itrs // child_mod
        expected_call_count = expected_parent_call_count * child_itrs
        self.assertEqual(mock_handle_event.call_count, expected_call_count)


if __name__ == "__main__":
    unittest.main()
