# Processing streams

# In this exercise, you’ll be using nlp.pipe for more efficient text processing.
# The nlp object has already been created for you. A list of tweets about a
# popular American fast food chain are available as the variable TEXTS.
#
# Part 1
# Rewrite the example to use nlp.pipe. Instead of iterating over the texts and
# processing them, iterate over the doc objects yielded by nlp.pipe.

# Exmaple 1

import json
import spacy

nlp = spacy.load("en_core_web_sm")

with open("exercises/en/tweets.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

# Process the texts and print the adjectives
# for text in TEXTS:
for doc in nlp.pipe(TEXTS):
    print([token.text for token in doc if token.pos_ == "ADJ"])

# Example 2

import json
import spacy

nlp = spacy.load("en_core_web_sm")

with open("exercises/en/tweets.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

# Process the texts and print the entities
# docs = [nlp(text) for text in TEXTS]
docs = list(nlp.pipe(TEXTS))
entities = [doc.ents for doc in docs]
print(*entities)

# Example 3

import spacy

nlp = spacy.blank("en")

people = ["David Bowie", "Angela Merkel", "Lady Gaga"]

# Create a list of patterns for the PhraseMatcher
patterns = list(nlp.pipe(people)) # for person in people
