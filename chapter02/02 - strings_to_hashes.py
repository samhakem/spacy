# String to hashes

# Import spaCy and create the English nlp object
import spacy

nlp = spacy.load('en_core_web_sm')

# Process the text
doc = nlp('I have a cat')

# Look up the hash for the word "cat"
cat_hash = nlp.vocab.strings['cat']
print(cat_hash)

# Look up the cat_hash to get the string
cat_string = nlp.vocab.strings[cat_hash]
print(cat_string)

doc1 = nlp('David Bowie is a PERSON')

# Look up the hash for the string label "PERSON"
person_hash = nlp.vocab.strings['PERSON']
print(person_hash)

# Look up the person_hash to get the string
person_string = nlp.vocab.strings[person_hash]
print(person_string)
