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

.PHONY: help Makefile serve clean dev i18n-init i18n- i18n-help

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

serve: html
	@python -m http.server -d $(BUILDDIR)/html 8000

clean:
	@rm -rf "$(BUILDDIR)/*"

dev:
	sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

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
	@ls -1 locale/ | grep -v 'README' || echo "No translations available"