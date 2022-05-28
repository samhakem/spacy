# Simple components

import spacy
from spacy.language import Language

# Define the custom component
@Language.component("length_component")
def length_component_function(doc):
    # Get the doc's length
    doc_length = len(doc)
    print(f"This document is {doc_length} tokens long.")
    # Return the doc
    return doc

# Load the small English pipeline
nlp = spacy.load("en_core_web_sm")

# Add the component first in the pipeline and print the pipe names
nlp.add_pipe("length_component", first=True)
print(nlp.pipe_names)

# Process a text
doc = nlp("This is a sentence.")

# ValueError: [E966] `nlp.add_pipe` now takes the string name of the registered component
# factory, not a callable component. Expected string, but got <function length_component_function
# at 0x7f135d32d4d0> (name: 'None').

# - If you created your component with `nlp.create_pipe('name')`: remove nlp.create_pipe and
# call `nlp.add_pipe('name')` instead.

# - If you passed in a component like `TextCategorizer()`: call `nlp.add_pipe` with the string
# name instead, e.g. `nlp.add_pipe('textcat')`.

# - If you're using a custom component: Add the decorator `@Language.component` (for function
# components) or `@Language.factory` (for class components / factories) to your custom
# component and assign it a name, e.g. `@Language.component('your_name')`. You can then
# run `nlp.add_pipe('your_name')` to add it to the pipeline.
