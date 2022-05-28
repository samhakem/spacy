# Getting started

# Notes:
#
# What is nlp? Nlp as a blanket term strives to build programs that have
# a level of language comprehension based on speech or unstructured text.
# It then uses this comprehension to respond with text or speech of its own,
# in much the same way as we do.
#
# - unstructured text -
# add eggs and milk
# to shopping list
#
# >NLP<
#
# - structured -
#     < shopping list >
#     <item [eggs]>
#     <item [milk]>
# </>
#
# Doc, sent, token, span, spangroup(No.)
#
# python -m venv .env
# source .env/bin/activate
# pip install -U pip setuptools wheel
# pip install -U spacy
# python -m spacy download en_core_web_sm
# /home/samhakem/PycharmProjects/explosion_lab/venv/bin/python -m spacy download en

# Central data structures include: Language class, Vocab and Doc object.
# Language class processes text and turns it into a Doc object stored as var nlp
