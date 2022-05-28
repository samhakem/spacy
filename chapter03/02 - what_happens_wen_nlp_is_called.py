# What happens when you call nlp

# What does spaCy do when you call nlp on a string of text?

doc = nlp("This is a sentence.")

# Tokenize the text and apply each pipeline component in order.
# The tokenizer turns a string of text into a Doc object. spaCy
# then applies every component in the pipeline on document, in order.
