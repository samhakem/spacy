# Debugging patters
# Why does this pattern not match the tokens “Silicon Valley” in the doc?
# The tokenizer doesn’t create tokens for single spaces, so there’s no token
# with the value " " in between.
# The tokenizer already takes care of splitting off whitespace and each
# dictionary in the pattern describes one token.

pattern = [{"LOWER": "silicon"}, {"TEXT": " "}, {"LOWER": "valley"}]

doc = nlp("Can Silicon Valley workers rein in big tech from within?")
