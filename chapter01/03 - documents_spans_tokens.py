# Import spacy
import spacy

# Create the English nlp object
nlp = spacy.load('en_core_web_sm')

# Documents, spans and tokens

# ** Doc object
#   * Created by var that takes parameter 'string' and processes nlp object
doc = nlp('I like tree kangaroos and narwhals.')

# Index position of token in Doc object to call single token(ie string character)
first_token = doc[0]

# Index into the Doc to get a single Token
token = doc[1]

# Get the token text via the .text attribute
print(token.text)

# ** The token object
# Iterate over tokens in a doc
# Print the first token
for token in doc:
    print(first_token.text)

# ** Span object
# Slice of the Doc for "tree kangaroos"
tree_kangaroos = doc[2:4]

# Get via .text attribute
print(tree_kangaroos.text)

# A slice of the Doc for "tree kangaroos and narwhals" (without the ".")
tree_kangaroos_and_narwhals = doc[2:]
print(tree_kangaroos_and_narwhals.text)
