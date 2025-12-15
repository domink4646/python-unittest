import unittest
from armstrong import is_armstrong

class TestArmstrong(unittest.TestCase):
    def test_armstrong_numbers(self):
        self.assertTrue(is_armstrong(153))
        self.assertTrue(is_armstrong(370))
        self.assertTrue(is_armstrong(9474))
        self.assertTrue(is_armstrong(0))
        self.assertTrue(is_armstrong(1))

    def test_not_armstrong(self):
        self.assertFalse(is_armstrong(10))
        self.assertFalse(is_armstrong(100))

if __name__ == '__main__':
    unittest.main()