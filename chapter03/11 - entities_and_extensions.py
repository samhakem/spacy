# Entities and extensions

# In this exercise, you’ll combine custom extension attributes with the
# statistical predictions and create an attribute getter that returns a
# Wikipedia search URL if the span is a person, organization, or location.
#
# Complete the get_wikipedia_url getter so it only returns the URL if the
# span’s label is in the list of labels.Set the Span extension "wikipedia_url" u
# sing the getter get_wikipedia_url.Iterate over the entities in the doc and
# output their Wikipedia URL.

import spacy
from spacy.tokens import Span

nlp = spacy.load("en_core_web_sm")


def get_wikipedia_url(span):
    # Get a Wikipedia URL if the span has one of the labels
    if span.label_ in ("PERSON", "ORG", "GPE", "LOCATION"):
        entity_text = span.text.replace(" ", "_")
        return "https://en.wikipedia.org/w/index.php?search=" + entity_text


# Set the Span extension wikipedia_url using the getter get_wikipedia_url
Span.set_extension('wikipedia_url', getter=get_wikipedia_url)

doc = nlp(
    "In over fifty years from his very first recordings right through to his "
    "last album, David Bowie was at the vanguard of contemporary culture."
)
for ent in doc.ents:
    # Print the text and Wikipedia URL of the entity
    print(ent.text, ent._.wikipedia_url)