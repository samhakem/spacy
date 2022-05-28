# Good data vs bad data

# Here’s an excerpt from a training set that labels the entity type TOURIST_DESTINATION in traveler reviews.

doc1 = nlp("i went to amsterdem last year and the canals were beautiful")
doc1.ents = [Span(doc1, 3, 4, label="TOURIST_DESTINATION")]

doc2 = nlp("You should visit Paris once, but the Eiffel Tower is kinda boring")
doc2.ents = [Span(doc2, 3, 4, label="TOURIST_DESTINATION")]

doc3 = nlp("There's also a Paris in Arkansas, lol")
doc3.ents = []

doc4 = nlp("Berlin is perfect for summer holiday: great nightlife and cheap beer!")
doc4.ents = [Span(doc4, 0, 1, label="TOURIST_DESTINATION")]

# Part 1
# Why is this data and label scheme problematic?

# Whether a place is a tourist destination is a subjective judgement and not a definitive category. It will be very
# difficult for the entity recognizer to learn.

# A much better approach would be to only label "GPE" (geopolitical entity) or "LOCATION" and then use a rule-based
# system to determine whether the entity is a tourist destination in this context. For example, you could resolve the
# entities types back to a knowledge base or look them up in a travel wiki.

import spacy
from spacy.tokens import Span

nlp = spacy.blank("en")

doc1 = nlp("i went to amsterdem last year and the canals were beautiful")
doc1.ents = [Span(doc1, 3, 4, label="GPE")]

doc2 = nlp("You should visit Paris once, but the Eiffel Tower is kinda boring")
doc2.ents = [Span(doc2, 3, 4, label="GPE")]

doc3 = nlp("There's also a Paris in Arkansas, lol")
doc3.ents = [Span(doc3, 4, 5, label="GPE"), Span(doc3, 6, 7, label="GPE")]

doc4 = nlp("Berlin is perfect for summer holiday: great nightlife and cheap beer!")
doc4.ents = [Span(doc4, 0, 1, label="GPE")]

# Rewrite the doc.ents to only use spans of the label "GPE" (cities, states, countries) instead of
# "TOURIST_DESTINATION".
# Don’t forget to add spans for the "GPE" entities that weren’t labeled in the old data.

# Once the model achieves good results on detecting GPE
# entities in the traveler reviews, you could add a rule-based component to
# determine whether the entity is a tourist destination in this context. For
# example, you could resolve the entities types back to a knowledge base or look
# them up in a travel wiki.
