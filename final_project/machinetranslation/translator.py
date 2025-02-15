from deep_translator import MyMemoryTranslator
from deep_translator import GoogleTranslator

def english_to_french(english_text):
    """
    This function translates English text to French

    Args:
        english_text (str): The text to be translated.

    Returns:
        str: The translated text in French.
    """
    translator = GoogleTranslator(source='en', target='fr')
    french_text = translator.translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    This function translates French text to English

    Args:
        french_text (str): The text to be translated.

    Returns:
        str: The translated text in English.
    """
    translator = GoogleTranslator(source='fr', target='en')
    english_text = translator.translate(french_text)
    return english_text