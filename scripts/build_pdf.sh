#!/usr/bin/env bash
set -e

echo "=== Compiling Citrus Disease Classification LaTeX Manuscript ==="
pdflatex -interaction=nonstopmode Thesis.tex
bibtex Thesis
pdflatex -interaction=nonstopmode Thesis.tex
pdflatex -interaction=nonstopmode Thesis.tex
echo "=== Build Complete: Thesis.pdf generated successfully! ==="
