import unittest
from andela import word

class TestCase(unittest.TestCase):
    def test_word(self):
        self.assertEqual(word(199),'one hundred and ninety nine')