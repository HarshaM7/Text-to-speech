import random
import torch
from transformers import MarianTokenizer, MarianMTModel

# Initialize the MarianMT tokenizer and model for English to Hindi translation
model_name = "Helsinki-NLP/opus-mt-en-hi"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# English input sentence
english_sentence = "I had about a 30 minute demo just using this new headset."

# Tokenize and convert English text to tensors
inputs = tokenizer(english_sentence, return_tensors="pt")

# Generate Hindi text
with torch.no_grad():
    hindi_ids = model.generate(inputs.input_ids, max_length=100, num_return_sequences=1)

# Decode and print the Hindi translation
hindi_translation = tokenizer.decode(hindi_ids[0], skip_special_tokens=True)

# Define a list of words to keep in English
english_words_to_keep = ["I", "demo", "new"]

# Tokenize the Hindi translation
hindi_words = hindi_translation.split()

# Initialize the Hinglish sentence
hinglish_sentence = []

# Keep track of English words used so far
used_english_words = set()

# Combine English and Hindi words to create a Hinglish sentence
for word in hindi_words:
    if word in english_words_to_keep:
        if word not in used_english_words:
            hinglish_sentence.append(word)
            used_english_words.add(word)
        else:
            hinglish_sentence.append(random.choice(english_words_to_keep))  # Randomly choose an English word
    else:
        hinglish_sentence.append(word)

# Combine mixed words to form the final Hinglish sentence
output_sentence = " ".join(hinglish_sentence)

# Print the Hinglish sentence
print("Hinglish Sentence:", output_sentence)
