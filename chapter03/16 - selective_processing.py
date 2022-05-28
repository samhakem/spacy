# Selective processing

# In this exercise, you’ll use the nlp.make_doc and nlp.select_pipes
# methods to only run selected components when processing a text.

# Part 1
# Rewrite the code to only tokenize the text using nlp.make_doc.

# Exmaple 1

import spacy

nlp = spacy.load("en_core_web_sm")
text = (
    "Chick-fil-A is an American fast food restaurant chain headquartered in "
    "the city of College Park, Georgia, specializing in chicken sandwiches."
)

# Only tokenize the text
# doc = nlp(text)
doc = nlp.make_doc(text)
print([token.text for token in doc])

# Example 2

import spacy

nlp = spacy.load("en_core_web_sm")
text = (
    "Chick-fil-A is an American fast food restaurant chain headquartered in "
    "the city of College Park, Georgia, specializing in chicken sandwiches."
)

# Disable the tagger and lemmatizer
with nlp.select_pipes(disable=['tagger', 'lemmatizer']):
    # Process the text
    doc = nlp(text)
    # Print the entities in the doc
    print(doc.ents)
