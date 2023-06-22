import unittest
from translator import englishToFrench


class TranslatorTestCase(unittest.TestCase):
    def test_english_to_french(self):
        english_text = "Hello"
        expected_french_translation = "Bonjour"
        french_translation = englishToFrench(english_text)
        self.assertEqual(french_translation, expected_french_translation)
        english_text = "Goodbye"
        expected_french_translation = "Au revoir"
        french_translation = englishToFrench(english_text)
        self.assertEqual(french_translation, expected_french_translation)


if __name__ == '__main__':
    unittest.main()
