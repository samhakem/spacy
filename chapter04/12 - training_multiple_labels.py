# Training multiple labels

# Here’s a small sample of a dataset created to train a new entity type "WEBSITE". The original dataset contains a
# few thousand sentences. In this exercise, you’ll be doing the labeling by hand. In real life, you probably want to
# automate this and use an annotation tool – for example, Brat, a popular open-source solution, or Prodigy,
# our own annotation tool that integrates with spaCy.

# Example 1

# Complete the token offsets for the "WEBSITE" entities in the data.

import spacy
from spacy.tokens import Span

nlp = spacy.blank("en")

doc1 = nlp("Reddit partners with Patreon to help creators build communities")
doc1.ents = [
    Span(doc1, 0, 1, label="WEBSITE"),
    Span(doc1, 3, 4, label="WEBSITE"),
]

doc2 = nlp("PewDiePie smashes YouTube record")
doc2.ents = [Span(doc2, 2, 3, label="WEBSITE")]

doc3 = nlp("Reddit founder Alexis Ohanian gave away two Metallica tickets to fans")
doc3.ents = [Span(doc3, 0, 1, label="WEBSITE")]

# And so on...

# Example 2

# A model was trained with the data you just labelled, plus a few thousand similar examples. After training,
# it’s doing great on "WEBSITE", but doesn’t recognize "PERSON" anymore. Why could this be happening?

# The training data included no examples of "PERSON", so the model learned that this label is incorrect.
# If "PERSON" entities occur in the training data but aren’t labelled, the model will learn that they shouldn’t be
# predicted. Similarly, if an existing entity type isn’t present in the training data, the model may ”forget” and
# stop predicting it.

import spacy
from spacy.tokens import Span

nlp = spacy.blank("en")

doc1 = nlp("Reddit partners with Patreon to help creators build communities")
doc1.ents = [
    Span(doc1, 0, 1, label="WEBSITE"),
    Span(doc1, 3, 4, label="WEBSITE"),
]

doc2 = nlp("PewDiePie smashes YouTube record")
doc2.ents = [Span(doc2, 0, 1, label="PERSON"), Span(doc2, 2, 3, label="WEBSITE")]

doc3 = nlp("Reddit founder Alexis Ohanian gave away two Metallica tickets to fans")
doc3.ents = [Span(doc3, 0, 1, label="WEBSITE"), Span(doc3, 2, 4, label="PERSON")]

# And so on...
