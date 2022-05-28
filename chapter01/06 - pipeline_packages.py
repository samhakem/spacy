# Pipeline packages

# # Import spacy
# import spacy
#
# # Create the English nlp object
# nlp = spacy.load('en_core_web_sm')

# What’s not included in a pipeline package that you can load into spaCy?

# Pipeline packages do NOT include
# The labelled data that the pipeline was trained on
# They do include:
#   A config file describing how to create the pipeline
#   Binary weights to make statistical predictions
#   Strings of the pipelines vocabulary
