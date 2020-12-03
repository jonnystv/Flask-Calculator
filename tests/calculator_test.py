import unittest

from modules import calculator
class TestCalculator(unittest.TestCase):

    def test_add_2_numbers(self):
        self.assertEqual("The answer to 8 plus 4 is 12", add_2_numbers(8, 4))