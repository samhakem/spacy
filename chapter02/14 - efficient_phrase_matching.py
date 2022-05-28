import spacy

# Import the PhraseMatcher and initialize it
from spacy.matcher import PhraseMatcher

nlp = spacy.load('en_core_web_sm')

with open('/home/samhakem/PycharmProjects/chapter01/exercises/en/countries.txt', 'r') as f:
    COUNTRIES = f.read()

matcher = PhraseMatcher(nlp.vocab)
doc = nlp('Czech Republic may help Slovakia protect its airspace')

# Create pattern Doc objects and add them to the matcher
# This is the faster version of: [nlp(country) for country in COUNTRIES]
patterns = list(nlp.pipe(COUNTRIES))
matcher.add('COUNTRY', patterns)

# Call the matcher on the test document and print the result
matches = matcher(doc)
print([doc[start:end] for match_id, start, end in matches])
