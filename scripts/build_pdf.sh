#!/usr/bin/env bash
set -e

echo "=== Compiling Citrus Disease Classification LaTeX Manuscript (main.tex) ==="
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
echo "=== Build Complete: main.pdf generated successfully! ==="
