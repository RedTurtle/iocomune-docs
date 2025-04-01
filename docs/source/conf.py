# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Documentazione io-Comune"
copyright = "2025, RedTurtle"
author = "RedTurtle"
release = "0.1"
html_show_copyright = True

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]

templates_path = ["_templates"]
exclude_patterns = []

language = "it"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "furo"
html_static_path = ["_static"]
# Aggiungi il percorso dei CSS personalizzati
html_css_files = [
    "css/style.css",  # Assicurati che il percorso sia relativo a '_static'
]
# These are options specifically for the Wagtail Theme.
html_theme_options = dict(
    project_name="Documentazione io-Comune",
    logo_url="/",
    logo_alt="Documentazione io-Comune",
    logo_height=59,
    logo="img/logo.png",
    logo_width=45,
    github_url="https://github.com/RedTurtle/iocomune-docs/blob/main/docs/",
    header_links="Top 1|http://example.com/one, Top 2|http://example.com/two",
    # footer_links=",".join(
    #     [
    #         "About Us|http://example.com/",
    #         "Contact|http://example.com/contact",
    #         "Legal|http://example.com/dev/null",
    #     ]
    # ),
)
html_search_options = {"highlight": True}
html_show_sphinx = False

try:
    extensions
except NameError:
    extensions = []

extensions.append("sphinx_wagtail_theme")
html_theme = "sphinx_wagtail_theme"
