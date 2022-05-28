# Inspecting the pipeline
#
# Let’s inspect the small English pipeline!
#
# Load the en_core_web_sm pipeline and create the nlp object.
# Print the names of the pipeline components using nlp.pipe_names.
# Print the full pipeline of (name, component) tuples using nlp.pipeline.

import spacy

# Load the en_core_web_sm pipeline
nlp = spacy.load('en_core_web_sm')

# Print the names of the pipeline components
print(nlp.pipe_names)

# Print the full pipeline of (name, component) tuples
print(nlp.pipeline)
