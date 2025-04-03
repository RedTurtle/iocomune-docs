# iocomune-docs

Documentazione di io-Comune

Questa documentazione è deployata su github pages con Sphinx.

### Development

Seguono indicazioni per lo sviluppo in locale:

- Crea un virtualenv python e succesivamente `pip install -r requirements.txt`.
- Tutti i comandi base necessari per lo sviluppo si trovano nel Makefile, si riporta qui di seguito

```
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
 @$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile serve clean dev i18n-init i18n i18n- i18n-help

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
 @$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Serve in locale usando python http.server sulla 8000
serve: html
 @python -m http.server -d $(BUILDDIR)/html 8000

# Pulisci la cartella di build
clean:
 @rm -rf "$(BUILDDIR)/*"

# Avvia in dev mode
dev:
 sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Inizializzazione delle traduzioni
i18n-init:
 sphinx-build -b gettext source _build/gettext

# Regola per aggiornare le traduzioni per una lingua specifica
i18n-%:
 sphinx-intl update -p _build/gettext -l $* && sphinx-intl build

# Helper per mostrare le lingue disponibili e l'uso del comando
i18n-help:
 @echo "Usage: make i18n-<language>"
 @echo "Example: make i18n-it"
 @echo ""
 @echo "Available languages:"
 @ls -1 source/locales/ || echo "No translations available"

# Dopo aver inizializzato le traduzioni, puoi aggiornare con questo comando tutte le traduzioni disponibili per i locale disponibili
i18n:
 @for loc in $(shell ls -1 source/locales/) ; do \
  $(MAKE) i18n-$$loc; \
 done
```
