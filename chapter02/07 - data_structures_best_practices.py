# Data structures best practices

import spacy

nlp = spacy.load('en_core_web_sm')

# Why is this code bad?
# It only uses lists of strings instead of native token attributes. T
# his is often less efficient, and can't express complex relationships.
# doc = nlp("Berlin looks like a nice city")
#
# # Get all tokens and part-of-speech tags
# token_texts = [token.text for token in doc]
# pos_tags = [token.pos_ for token in doc]
#
# for index, pos in enumerate(pos_tags):
#     # Check if the current token is a proper noun
#     if pos == "PROPN":
#         # Check if the next token is a verb
#         if pos_tags[index + 1] == "VERB":
#             result = token_texts[index]
#             print("Found proper noun before a verb:", result)

# Revised code; this one was tricky
# Get all tokens and part-of-speech tags
doc = nlp("Berlin is a nice city!")
for token in doc:
    # Check if the current token is a proper noun
    if token.i + 1 < len(doc):
        if token.pos_ == 'PROPN' and doc[token.i + 1].pos_ == 'VERB':
            print('Found a verb after a proper noun!')
            print(token.text, doc[token.i + 1].text)
