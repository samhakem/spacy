# Predicting linguistic annotations
# Call spacy.explain to find out what tag or label means in loop
# example: spacy.explain("PROPN") or spacy.explain("GPE").

# Import spacy
import spacy

# Load the English nlp object
nlp = spacy.load('en_core_web_sm')

text = "It’s official: Apple is the first U.S. public company to reach a $1 trillion market value"

# Process the text
doc = nlp(text)

for token in doc:
    # Get the token text, part-of-speech tag and dependency label
    token_text = token.text
    token_pos = token.pos_
    token_dep = token.dep_
    # This is for formatting only
    print(f"{token_text:<12}{token_pos:<10}{token_dep:<10}")

# Iterate over the predicted entities
for ent in doc.ents:
    # Print the entity text and its label
    print(ent.text, ent.label_)

# Get a description for a given POS tag, dependency label or entity type.
spacy.explain("NORP")
# Nationalities or religious or political groups

doc = nlp("Hello world")
for word in doc:
   print(word.text, word.tag_, spacy.explain(word.tag_))

# Hello UH interjection
# world NN noun, singular or mass
