import unittest
from unittest.mock import patch
from event.constants import EVENT_TYPES
from script.actions import handle_event

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


if __name__ == "__main__":
    unittest.main()
