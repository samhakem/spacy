# Using the training CLI

# Let’s use the config file generated in the previous exercise and the training corpus we’ve created to train a named
# entity recognizer!
#
# The train command lets you train a model from a training config file. A file config_gadget.cfg is already available
# in the directory exercises/en, as well as a file train_gadget.spacy containing the training examples, and a file
# dev_gadget.spacy containing the evaluation examples. Because we’re executing the command in a Jupyter environment
# in this course, we’re using the prefix !. If you’re running the command in your local terminal, you can leave this
# out.
#
# Call the train command with the file exercises/en/config_gadget.cfg.
# Save the trained pipeline to a directory output.
# Pass in the exercises/en/train_gadget.spacy and exercises/en/dev_gadget.spacy paths.

# python -m spacy train ./exercises/en/config_gadget.cfg --output ./output --paths.train
# ./exercises/en/train_gadget.spacy --paths.dev ./exercises/en/dev_gadget.spacy
