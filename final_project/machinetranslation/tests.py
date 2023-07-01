import unittest
from translator import english_to_french, french_to_english

class TestingTheTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertEqual(english_to_french("Yes"),"Oui")

        self.assertNotEqual(english_to_french("Hello"),"Salut")
        self.assertNotEqual(english_to_french("Yes"),"Non")

    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Good morning")
        self.assertEqual(french_to_english("Merci"), "THANKS")

        self.assertNotEqual(french_to_english("Bonjour"), "Good night")
        self.assertNotEqual(french_to_english("Merci"), "Goodbye")


if __name__ == "__main__":
    unittest.main()