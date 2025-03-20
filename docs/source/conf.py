# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import docs_italia_theme

project = "Documentazione io-Comune"
copyright = "2025, RedTurtle"
author = "RedTurtle"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "docs_italia_theme",
]

templates_path = ["_templates"]
exclude_patterns = []

language = "it"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "docs_italia_theme"
html_theme_path = [docs_italia_theme.get_html_theme_path()]
html_static_path = ["_static"]
