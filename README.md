# Comparative Performance and Computational Complexity Analysis of Pre-Trained Deep Learning Models for Citrus Fruit Disease Classification

This repository contains the complete LaTeX source code, dataset figures, bibliography, and compiled manuscript for the research paper:

> **"Comparative Performance and Computational Complexity Analysis of Pre-Trained Deep Learning Models for Citrus Fruit Disease Classification"**  
> *Submitted to the International Journal of Computer Applications (IJCA)*

---

## 📁 Repository Structure

```
citrus-disease-classification/
├── Thesis/
│   ├── Thesis.tex                         # Primary manuscript LaTeX source
│   ├── References.bib                     # Curated bibliography database (32 entries)
│   ├── ijcaArticle.cls                    # Official IJCA document class
│   ├── ijcaArticle.bst                    # Official IJCA BibTeX style (consecutive citation order)
│   ├── Thesis.pdf                         # Compiled 7-page publication-ready PDF
│   └── *.png                              # 8 High-resolution (300+ DPI) figures
├── submission-guide/                      # Official IJCA submission template & guide
├── IJCA_Submission_Package.zip           # Self-contained archive for Overleaf / IJCA portal
├── Referee's Report.pdf                   # Minor revisions report from PhDFocus / IJCA
└── README.md
```

---

## 🔬 Research Overview & Key Contributions

- **Multi-Class Pathology**: Classification across 4 citrus condition classes (*Canker*, *Black Spot*, *Greening (HLB)*, and *Healthy*) using 1,463 standardized RGB images.
- **Deep Transfer Learning Architectures**: Fine-tuning and empirical benchmarking of MobileNetV2, InceptionV3, ResNet50, and VGG19.
- **Dual-Faceted Evaluation**: Comprehensive assessment of both diagnostic accuracy (Accuracy, Precision, Recall, F1-Score) and computational complexity (Training Duration, Inference Latency, Memory Footprint).
- **Core Finding**: MobileNetV2 achieved the superior performance-complexity trade-off with **96.77% accuracy**, **98.54% F1-score**, minimal memory consumption (**9.82 MB**), and rapid training (**406.29 s**), demonstrating optimal feasibility for edge agricultural monitoring.

---

## 🛠️ Building the Document

To compile the LaTeX manuscript locally:

```bash
cd Thesis/
pdflatex -interaction=nonstopmode Thesis.tex
bibtex Thesis
pdflatex -interaction=nonstopmode Thesis.tex
pdflatex -interaction=nonstopmode Thesis.tex
```

---

## 📄 License & Authors

- Nur E Jannatul Farjana
- Abdullah Miraz
- Krishna Das

*Department of Computer Science and Engineering, International University of Business Agriculture and Technology (IUBAT), Dhaka, Bangladesh.*
