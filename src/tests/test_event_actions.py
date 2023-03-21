import unittest
from unittest.mock import patch, Mock
from event.constants import CLICK_TYPES
from event.events import ClickEvent, ImageEvent
from event.exceptions import FindImageError
from pyautogui import ImageNotFoundException


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


class TestImageEvents(unittest.TestCase):
    @patch("event.events.pyautogui.locateCenterOnScreen")
    def test_find_image(self, mock_locate):
        mock_image_path = "test_image.png"
        mock_region = (100, 200, 300, 400)
        mock_locate.return_value = (150, 150)
        result = ImageEvent.find_image(
            mock_image_path,
            confidence=0.6,
            grayscale=False,
            region=mock_region,
            attempts=1,
        )
        self.assertEqual(result, (150, 150))

    @patch("event.events.Delay.perform_delay_ms")
    @patch("event.events.pyautogui.locateCenterOnScreen")
    def test_image_not_found(self, mock_locate, _):
        mock_locate.raiseError.side_effect = ImageNotFoundException()
        mock_image_path = "test_image.png"
        mock_region = (100, 200, 300, 400)

        with self.assertRaises(FindImageError):
            ImageEvent.find_image(
                mock_image_path,
                confidence=0.6,
                grayscale=False,
                region=mock_region,
                attempts=3,
            )


if __name__ == "__main__":
    unittest.main()
