from googletrans import Translator
import re

# Dictionary for replacing difficult English words/phrases with Hinglish
word_replacements = {
    "definitely": "मझु ेसि र्फ",
    "share": "शेयर",
    "feedback": "फीडबैक",
    "comment section": "कमेंट सेक्शन",
    "big video": "बड़ा वीडियो",
    "products": "उत्पादों",
    "waiting": "इंतजार",
    "bag": "बैग"
}

# Function to perform Hinglish translation
def translate_to_hinglish(text):
    # Translate English to Hinglish using googletrans
    translator = Translator()
    translation = translator.translate(text, src="en", dest="hi")
    translated_text = translation.text

    # Replace difficult English words/phrases with Hinglish equivalents
    for word, replacement in word_replacements.items():
        translated_text = re.sub(r'\b' + word + r'\b', replacement, translated_text, flags=re.IGNORECASE)

    return translated_text

# Get user input in English
user_input = input("Enter an English sentence: ")

# Translate the user input to Hinglish
hinglish_output = translate_to_hinglish(user_input)

# Print the translated Hinglish sentence
print(f"Hinglish: {hinglish_output}")
