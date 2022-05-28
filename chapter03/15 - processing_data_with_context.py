# Processing data with context

# In this exercise, you’ll be using custom attributes to add author
# and book meta information to quotes.
#
# A list of [text, context] examples is available as the variable
# DATA. The texts are quotes from famous books, and the contexts
# dictionaries with the keys "author" and "book".
#
# Use the set_extension method to register the custom attributes
# "author" and "book" on the Doc, which default to None.
# Process the [text, context] pairs in DATA using nlp.pipe with as_tuples=True.
# Overwrite the doc._.book and doc._.author with the respective info
# passed in as the context.

import json
import spacy
from spacy.tokens import Doc

with open("exercises/en/bookquotes.json", encoding="utf8") as f:
    DATA = json.loads(f.read())

nlp = spacy.blank("en")

# Register the Doc extension "author" (default None)
Doc.set_extension('author', default=None)

# Register the Doc extension "book" (default None)
Doc.set_extension('book', default=None)

for doc, context in nlp.pipe(DATA, as_tuples=True):
    # Set the doc._.book and doc._.author attributes from the context
    doc._.book = context['book']
    doc._.author = context['author']

    # Print the text and custom attribute data
    print(f"{doc.text}\n — '{doc._.book}' by {doc._.author}\n")
