# Library Architecture

# The central data structures in spaCy are the Language class, the Vocab and the Doc object.
# The Language class is used to process a text and turn it into a Doc object. It’s typically
# stored as a variable called nlp. The Doc object owns the sequence of tokens and all their
# annotations. By centralizing strings, word vectors and lexical attributes in the Vocab, we
# avoid storing multiple copies of this data. This saves memory, and ensures there’s a single
# source of truth.
#
# Text annotations are also designed to allow a single source of truth: the Doc object owns
# the data, and Span and Token are views that point into it. The Doc object is constructed
# by the Tokenizer, and then modified in place by the components of the pipeline. The Language
# object coordinates these components. It takes raw text and sends it through the pipeline,
# returning an annotated document. It also orchestrates training and serialization.
