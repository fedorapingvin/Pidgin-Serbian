# Serbian to Pidgin Serbian Encoder/Decoder

# Vocabulary mapping from Serbian to Pidgin Serbian
vocabulary = {
    "Zdravo": "Cvrčak",
    "Doviđenja": "Pav",
    "Hrana": "Hrana",
    "Voda": "Voda",
    "Gnezdo": "Gnezdo",
    "Prijatelj": "Prijatelj",
    "Leteti": "Leteti",
    "Jesti": "Jesti",
    "Pevati": "Pevati",
    "Sleteti": "Sleteti",
    "Lep": "Lep",
    "Brz": "Brz",
    "Miran": "Miran",
    "gde": "gde",
    "je": "je",
    "leti": "leti",
    "visoko": "visoko",
    "Lepo": "Lep",
}

# Function to encode Serbian to Pidgin Serbian
def encode_to_pidgin(serbian_text):
    # Split the input text into words
    words = serbian_text.split()
    # Translate each word using the vocabulary mapping
    pidgin_words = [vocabulary.get(word, word) for word in words]
    # Join the translated words back into a sentence
    return ' '.join(pidgin_words)

# Function to decode Pidgin Serbian to Serbian
def decode_to_serbian(pidgin_text):
    # Reverse the vocabulary mapping for decoding
    reverse_vocabulary = {v: k for k, v in vocabulary.items()}
    # Split the input text into words
    words = pidgin_text.split()
    # Translate each word using the reverse vocabulary mapping
    serbian_words = [reverse_vocabulary.get(word, word) for word in words]
    # Join the translated words back into a sentence
    return ' '.join(serbian_words)

# Example usage
if __name__ == "__main__":
    # Test encoding
    serbian_sentence = "Zdravo, gde je hrana?"
    pidgin_sentence = encode_to_pidgin(serbian_sentence)
    print("Serbian:", serbian_sentence)
    print("Pidgin Serbian:", pidgin_sentence)

    # Test decoding
    pidgin_sentence = "Cvrčak, gde je hrana?"
    serbian_sentence = decode_to_serbian(pidgin_sentence)
    print("Pidgin Serbian:", pidgin_sentence)
    print("Serbian:", serbian_sentence)
