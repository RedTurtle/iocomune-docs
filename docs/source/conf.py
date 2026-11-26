# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Manuali d'uso"
copyright = "2026, RedTurtle Technology S.r.l."
author = "RedTurtle"
release = "0.1"
html_show_copyright = True

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]
myst_enable_extensions = ["colon_fence"]  # consente i riquadri con :::{note} ... :::

templates_path = ["_templates"]
# note di rilascio nascoste per ora (vedi index.md)
exclude_patterns = ["_snippets", "io-comune", "io-prenoto", "io-cittadino"]

# Locales section
language = "it"
locale_dirs = ["locales"]  # Dir dove si trovano i file .mo e .po
gettext_compact = False  # Imposta su False per ottenere file .pot completi

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "furo"
html_static_path = ["_static"]
# Aggiungi il percorso dei CSS personalizzati
html_css_files = [
    "css/style.css",  # Assicurati che il percorso sia relativo a '_static'
    "css/redturtle.css",  # colori RedTurtle (dal design system): toglierlo per tornare al tema blu
]
html_favicon = "_static/img/favicon-redturtle.png"
# These are options specifically for the Wagtail Theme.
html_theme_options = dict(
    project_name="Manuali d'uso",
    logo_url="/",
    logo_alt="RedTurtle",
    logo_height=48,
    logo="img/tartaruga-cerchio.svg",
    logo_width=48,
    github_url="https://github.com/RedTurtle/iocomune-docs/blob/main/docs/source/",
    header_links="Help-desk|https://redturtle.tpondemand.com/helpdesk/auth/login?ReturnUrl=%2F,redturtle.it|https://www.redturtle.it/",
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

# niente sorgenti .md pubblicati né link "mostra sorgente"
html_copy_source = False
html_show_sourcelink = False
