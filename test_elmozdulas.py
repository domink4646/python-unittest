import unittest
from elmozdulas import calculate_displacement

class TestElmozdulas(unittest.TestCase):
    def test_calc(self):
        self.assertEqual(calculate_displacement(10, 5), 50)
        self.assertEqual(calculate_displacement(0, 5), 0)
        self.assertAlmostEqual(calculate_displacement(2.5, 4), 10.0)

if __name__ == '__main__':
    unittest.main()