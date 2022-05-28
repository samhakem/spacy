# Lexical attributes

# Import spacy
import spacy

# Create the English nlp object
nlp = spacy.load('en_core_web_sm')

# Process the text
doc = nlp(
    "In 1990, more than 60% of people in East Asia were in extreme poverty. "
    "Now less than 4% are."
)

# Token object
# Iterate over the tokens in the doc: declare temp var to iter over the doc object
for token in doc:
    # Check if the token resembles a number: token.(attr)
    # Does the token represent a number? e.g. “10.9”, “10”, “ten”, etc.
    # type: bool

    if token.like_num:
        # Get the next token in the document: var_declared = doc(object)[token.i + 1]
        next_token = doc[token.i + 1]
        # Check if the next token's text equals "%": if var.text(object) == "delimiter"
        if next_token.text == "%":
            print("Percentage found:", token.text)

print('Index:   ', [token.i for token in doc])
print('Text:    ', [token.text for token in doc])

print('is_alpha:', [token.is_alpha for token in doc])
print('is_punct:', [token.is_punct for token in doc])
print('like_num:', [token.like_num for token in doc])
