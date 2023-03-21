import unittest

from script.utils import bypass_iteration, calculate_itr_count


class TestUtilFunctions(unittest.TestCase):
    def test_bypass_iteration(self):
        self.assertFalse(bypass_iteration(0, 0))
        self.assertFalse(bypass_iteration(0, 1))
        self.assertFalse(bypass_iteration(None, 2))

        self.assertFalse(bypass_iteration(3, 6))
        self.assertTrue(bypass_iteration(3, 7))
        self.assertFalse(bypass_iteration(2, 0))
        self.assertTrue(bypass_iteration(2, 1))
        self.assertFalse(bypass_iteration(2, 2))

    def test_calculate_itr_count(self):
        value_obj = {"min": 5, "max": 5, "distribution": "linear"}
        self.assertEqual(calculate_itr_count(value_obj), 5)

        value_obj = {"min": 1, "max": 10, "distribution": "linear"}
        self.assertTrue(1 <= calculate_itr_count(value_obj) <= 10)

        value_obj = {"min": 5, "max": 15}
        self.assertTrue(5 <= calculate_itr_count(value_obj) <= 15)


if __name__ == "__main__":
    unittest.main()
