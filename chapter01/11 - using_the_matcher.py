# Using the matcher

# Import spacy
import spacy

# Import the Matcher
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# Initialize the Matcher with the shared vocabulary: call the class with params
# nlp.vocab storage class
matcher = Matcher(nlp.vocab)

# Create a pattern matching two tokens: "iPhone" and "X"
# pattern = [{"LOWER": "hello"}, {"LOWER": "world"}]
# matcher.add("HelloWorld", [pattern])
# doc = nlp("hello world!")
# matches = matcher(doc)

pattern = [{'LOWER': 'iphone'}, {'LOWER': 'x'}]

# Add the pattern to the matcher
matcher.add("IPHONE_X_PATTERN", [pattern])

# Use the matcher on the doc
matches = matcher(doc)
print("Matches:", [doc[start:end].text for match_id, start, end in matches])
