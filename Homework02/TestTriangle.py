import unittest
from Homework02_functions import is_triangle


class TestTriangle(unittest.TestCase):

    def test_isTriangle(self):
        self.assertFalse(is_triangle(1, 1, 5))
