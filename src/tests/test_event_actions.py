import unittest
from unittest.mock import patch
from event.constants import CLICK_TYPES
from event.events import ClickEvent


class TestClickEvents(unittest.TestCase):
    @patch("event.events.pyautogui.click")
    def test_perform_click(self, mock_click):
        mock_x, mock_y = 100, 200
        mock_coords = [mock_x, mock_y]
        mock_offset = 0
        mock_click_type = CLICK_TYPES.left.__str__()

        ClickEvent.perform_click(mock_coords, mock_offset, mock_click_type)
        mock_click.assert_called_with(mock_x, mock_y, button=mock_click_type)

    @patch("event.events.random.randint")
    @patch("event.events.pyautogui.click")
    def test_perform_click_with_offset(self, _, mock_randint):
        mock_x, mock_y = 100, 200
        mock_coords = [mock_x, mock_y]
        mock_offset = 5
        mock_click_type = CLICK_TYPES.left.__str__()

        ClickEvent.perform_click(mock_coords, mock_offset, mock_click_type)
        mock_randint.assert_called_with(mock_offset * -1, mock_offset)


if __name__ == "__main__":
    unittest.main()
