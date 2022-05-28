# Rules-based matching

# Import spacy
import spacy

# Load the English nlp object
nlp = spacy.load('en_core_web_sm')

# Compared to using regular expressions on raw text, spaCy’s rule-based matcher
# engines and components not only let you find the words and phrases you’re
# looking for – they also give you access to the tokens within the document and
# their relationships. This means you can easily access and analyze the surrounding
# tokens, merge spans into single tokens or add entries to the named entities in
# doc.ents.

# ** Adding patterns
#   * Let’s say we want to enable spaCy to find a combination of three tokens:
# 01 A token whose lowercase form matches “hello”, e.g. “Hello” or “HELLO”.
# 02 A token whose is_punct flag is set to True, i.e. any punctuation.
# 03 A token whose lowercase form matches “world”, e.g. “World” or “WORLD”.

[{"LOWER": "hello"}, {"IS_PUNCT": True}, {"LOWER": "world"}]

# IMPORTANT NOTE
# When writing patterns, keep in mind that each dictionary represents one token.
# If spaCy’s tokenization doesn’t match the tokens defined in a pattern, the #
# pattern is not going to produce any results. When developing complex patterns,
# make sure to check examples against spaCy’s tokenization:

doc = nlp("A complex-example,!")
print([token.text for token in doc])
