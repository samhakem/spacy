# Docs, spans and entities from scratch

import spacy

from spacy.tokens import Doc, Span

nlp = spacy.load('en_core_web_sm')

words = ["I", "like", "David", "Bowie"]
spaces = [True, True, True, False]

# Create a doc from the words and spaces
doc = Doc(vocab=nlp.vocab, words=words, spaces=spaces)
print(doc.text)

# Create a span for "David Bowie" from the doc and assign it the label "PERSON"
# The 2 and 4 are start and end indices respectively
span = Span(doc, 2, 4, label="PERSON")

print(span.text, span.label_)

# Add the span to the doc's entities
doc.ents = [span]

# Print entities' text and labels
print([(ent.text, ent.label_) for ent in doc.ents])
