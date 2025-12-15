import unittest
from jelszoerosseg import jelszo_erosseg

class TestJelszoErosseg(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(jelszo_erosseg("alma"), 1)

    def test_length_5(self):
        self.assertEqual(jelszo_erosseg("almafa"), 2)

    def test_length_8(self):
        self.assertEqual(jelszo_erosseg("almafa12"), 4)

    def test_special_chars(self):
        self.assertEqual(jelszo_erosseg("a_b-c."), 8)

    def test_banned_words(self):
        self.assertEqual(jelszo_erosseg("titkosjelszo"), 0)
        self.assertEqual(jelszo_erosseg("alma123"), 0)

    def test_empty(self):
        self.assertEqual(jelszo_erosseg(""), 0)

if __name__ == '__main__':
    unittest.main()