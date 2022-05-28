# Predicting named entities in context

# Sometimes the training data won't contain all entities we need. Check out this example:

# Import spacy
import spacy

# Load the English nlp object
nlp = spacy.load('en_core_web_sm')

text = "Upcoming iPhone X release date leaked as Apple reveals pre-orders"

# Process the text
doc6 = nlp(text)

# Iterate over the entities
for ent in doc6.ents:
    # Print the entity text and label
    print(ent.text, ent.label_)

# Get the span for "iPhone X"
iphone_x = doc6[1:3]

# Print the span text
print("Missing entity:", iphone_x.text)
# We don't have to do this manually; we can use rule-based matching to find particular words and phrases.
