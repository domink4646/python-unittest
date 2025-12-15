import unittest
from maganhangzo import remove_vowels

class TestMaganhangzo(unittest.TestCase):
    def test_remove(self):
        self.assertEqual(remove_vowels("almafa"), "lmf")
        self.assertEqual(remove_vowels("Árvíztűrő tükörfúrógép"), "rvztr tkrfrgp")
    
    def test_no_vowels(self):
        self.assertEqual(remove_vowels("xyz"), "xyz")

    def test_empty(self):
        self.assertEqual(remove_vowels(""), "")

if __name__ == '__main__':
    unittest.main()