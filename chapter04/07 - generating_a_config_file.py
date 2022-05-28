# Generating a cofig file

# The init config command auto-generates a config file for training with the default settings. We want to train a
# named entity recognizer, so we’ll generate a config file for one pipeline component, ner. Because we’re executing
# the command in a Jupyter environment in this course, we’re using the prefix !. If you’re running the command in
# your local terminal, you can leave this out.

# Part 1
# Use spaCy’s init config command to auto-generate a config for an English pipeline.
# Save the config to a file config.cfg.
# Use the --pipeline argument to specify one pipeline component, ner.

# python -m spacy init config config.cfg --lang en --pipeline ner

# ⚠ To generate a more effective transformer-based config (GPU-only),
# install the spacy-transformers package and re-run this command. The config
# generated now does not use transformers.
# ℹ Generated config template specific for your use case
# - Language: en
# - Pipeline: ner
# - Optimize for: efficiency
# - Hardware: CPU
# - Transformer: None
# ✔ Auto-filled config with all values
# ✔ Saved config
# config.cfg
# You can now add your data and train your pipeline:
# python -m spacy train config.cfg --paths.train ./train.spacy --paths.dev ./dev.spacy
