# Import spacy
import spacy

# Create and declare the English nlp variable, which:
#   * contains processing pipeline - tokenizer and components
#   * includes language data, config and meta
nlp = spacy.load('en_core_web_sm')
nlp1 = spacy.load('de_core_web_sm')
nlp2 = spacy.load('es_core_web_sm')

# Process some English text
doc = nlp('A picture is worth 1000 words.')

# Print the document text
print(doc.text)

# Process some German text
doc1 = nlp1('Das ist mir Wurst')

# Print the document text
print(doc1.text)

# Process some Spanish text
doc2 = nlp2('No hay dos sin tres')

# Print the document text
print(doc2.text)
