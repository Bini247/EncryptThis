import unittest
from encryptThis import encryptThis

class TestEncryptThis(unittest.TestCase):

    def test_encryptThis_five_letters(self):
        self.assertEqual(encryptThis("Hello"), '72olle')

    def test_encryptThis_four_letters(self):
        self.assertEqual(encryptThis("good"), '103doo')

    def test_encryptThis_two_words(self):
        self.assertEqual(encryptThis("hello world"), '104olle 119drlo')

    def test_encryptThis_empty_message(self):
        self.assertEqual(encryptThis(""), '')
