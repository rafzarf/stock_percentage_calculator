import unittest

from main import calculate_percentage_return, validate_input


class TestStockReturnCalculator(unittest.TestCase):

    def test_calculate_percentage_return(self):

        self.assertEqual(calculate_percentage_return(100, 120), 20.0)

        self.assertEqual(calculate_percentage_return(50, 100), 100.0)

    def test_validate_input(self):

        self.assertFalse(validate_input("-50"))

        self.assertFalse(validate_input("abc"))

        self.assertEqual(validate_input("100"), 100.0)


if __name__ == "__main__":

    unittest.main()
