# Creating training data 1

# spaCy’s rule-based Matcher is a great way to quickly create training data for named entity models. A list of
# sentences is available as the variable TEXTS. You can print it to inspect it. We want to find all mentions of
# different iPhone models, so we can create training data to teach a model to recognize them as "GADGET".
#
# Write a pattern for two tokens whose lowercase forms match "iphone" and "x".
# Write a pattern for two tokens: one token whose lowercase form matches "iphone" and a digit.

import json
import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span

with open("exercises/en/iphone.json", encoding="utf8") as f:
    TEXTS = json.loads(f.read())

nlp = spacy.blank("en")
matcher = Matcher(nlp.vocab)

# Two tokens whose lowercase forms match "iphone" and "x"
pattern1 = [{'LOWER': 'iphone'}, {'LOWER': 'x'}]

# Token whose lowercase form matches "iphone" and a digit
pattern2 = [{'LOWER': 'iphone'}, {'IS_DIGIT': True}]

# Add patterns to the matcher and create docs with matched entities
matcher.add("GADGET", [pattern1, pattern2])
docs = []
for doc in nlp.pipe(TEXTS):
    matches = matcher(doc)
    spans = [Span(doc, start, end, label=match_id) for match_id, start, end in matches]
    print(spans)
    doc.ents = spans
    docs.append(doc)
