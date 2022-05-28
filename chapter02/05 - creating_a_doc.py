# Creating a Doc

import spacy

from spacy.tokens import Doc

nlp = spacy.load('en_core_web_sm')

# Desired text: "spaCy is cool!"
words = ["spaCy", "is", "cool", "!"]
spaces = [True, True, False, False]

# Create a Doc from the words and spaces
doc2 = Doc(vocab=nlp.vocab, words=words, spaces=spaces)
print(doc2.text)

# Desired text: "Go, get started!"
words = ["Go", ",", "get", "started", "!"]
spaces = [False, True, True, False, False]

# Create a Doc from the words and spaces
doc3 = Doc(vocab=nlp.vocab, words=words, spaces=spaces)
print(doc3.text)

# Desired text: "Oh, really?!"
words = ["Oh", ",", "really", "?", "!"]
spaces = [False, True, False, False, False]

# Create a Doc from the words and spaces
doc4 = Doc(vocab=nlp.vocab, words=words, spaces=spaces)
print(doc4.text)
