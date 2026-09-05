# 🍊 Comparative Performance and Computational Complexity Analysis of Pre-Trained Deep Learning Models for Citrus Fruit Disease Classification

[![LaTeX Build](https://img.shields.io/badge/LaTeX-Overleaf%20Compatible-brightgreen.svg?logo=overleaf)](https://www.overleaf.com/)
[![Draw.io](https://img.shields.io/badge/Diagrams-Draw.io%20%2F%20diagrams.net-orange.svg?logo=diagramsdotnet)](https://app.diagrams.net/)
[![IJCA Status](https://img.shields.io/badge/IJCA-Accept%20with%20Minor%20Revisions-blue.svg)](https://ijca.phdfocus.com/)
[![License](https://img.shields.io/badge/License-Academic%20Research-lightgrey.svg)]()

This repository contains the complete LaTeX source code, editable **Draw.io** diagrams, 300+ DPI figures, curated bibliography, and automated compilation workflows for our research manuscript submitted to the **International Journal of Computer Applications (IJCA)**.

---

## 📁 Practical Repository Structure

```
citrus-disease-classification/
├── .github/
│   └── workflows/
│       └── build-and-export.yml           # CI: Auto-export draw.io diagrams & build LaTeX PDF
├── diagrams/                              # 🎨 Editable Draw.io source diagrams (Source of Truth)
│   ├── fig1_methodology.drawio            # Figure 1: Proposed Methodology
│   ├── fig5_pretrained_workflow.drawio    # Figure 5: Transfer Learning Workflow
│   ├── fig6_tensorflow_architecture.drawio# Figure 6: Framework Architecture
│   └── README.md                          # Interactive editing guide
├── figures/                               # 🖼️ Publication-ready 300+ DPI figures
│   ├── fig1_methodology.png
│   ├── fig2_class_distribution.png
│   ├── fig3_sample_images.png
│   ├── fig4_dataset_split.png
│   ├── fig5_pretrained_workflow.png
│   ├── fig6_tensorflow_architecture.png
│   ├── fig7_confusion_matrices.png
│   └── fig8_performance_metrics.png
├── scripts/                               # ⚙️ Helper scripts & figure generation
│   ├── build_pdf.sh                       # Local compilation script
│   ├── generate_figures.py                # Python Matplotlib/PIL renderer
│   └── generate_drawio.py                 # Draw.io XML generator
├── docs/                                  # 📋 Referee report & submission checklists
│   ├── referee_report.pdf
│   └── submission_checklist.md
├── submission-guide/                      # 📜 Official IJCA template and guidelines
├── main.tex                               # 📄 Main LaTeX manuscript (Overleaf Root)
├── references.bib                         # 📚 Curated bibliography (32 references)
├── ijcaArticle.cls                        # 🏛️ Official IJCA document class
├── ijcaArticle.bst                        # 🔢 Official IJCA consecutive citation style
├── main.pdf                               # 📕 Compiled 7-page publication PDF
├── IJCA_Submission_Package.zip            # 📦 Upload-ready distribution archive
├── .gitignore
└── README.md
```

---

## 🎨 How to Edit & Maintain Diagrams in Draw.io

All system diagrams are stored as native **`.drawio`** files in the [`diagrams/`](./diagrams/) directory.

### Method 1: Web Browser (Zero Setup)
1. Navigate to [**app.diagrams.net**](https://app.diagrams.net/).
2. Click **"Open from GitHub"** $\rightarrow$ select `abdullahmiraz/citrus-disease-classification`.
3. Choose any diagram from the `diagrams/` folder (e.g., [`fig1_methodology.drawio`](./diagrams/fig1_methodology.drawio)).
4. Make your edits visually and press `Ctrl+S` / `Cmd+S` to **commit directly to GitHub**!

### Method 2: In VS Code / Antigravity IDE
1. Install the **Draw.io Integration** extension (`hediet.vscode-drawio`).
2. Click any `.drawio` file to open the interactive diagram editor right inside your IDE.

---

## ☁️ Overleaf Online Integration

This repository is structured for seamless 1-click synchronization with **Overleaf**:

1. In Overleaf, create a new project and select **"Import from GitHub"**.
2. Select `abdullahmiraz/citrus-disease-classification`.
3. Overleaf will automatically detect `main.tex` in the root folder, resolve all image assets via `figures/`, and compile immediately with 0 configuration needed.

---

## 🔬 Core Research Findings

- **Evaluated Models**: MobileNetV2, InceptionV3, ResNet50, and VGG19 on 1,463 citrus pathology images.
- **Top Performer**: **MobileNetV2** demonstrated the optimal accuracy-complexity balance:
  - **96.77% Accuracy** & **98.54% F1-Score**
  - **9.82 MB Memory Footprint** (91.7% reduction vs. VGG19)
  - **406.29 s Training Duration** (88% reduction vs. VGG19)
- **Deployment Feasibility**: Highly viable for real-time edge monitoring and mobile drone diagnostics.

---

## 🛠️ Local Build Instructions

To compile the LaTeX manuscript locally:

```bash
./scripts/build_pdf.sh
```

---

## 👥 Authors

- **Nur E Jannatul Farjana**
- **Abdullah Miraz**
- **Krishna Das**

*Department of Computer Science and Engineering, International University of Business Agriculture and Technology (IUBAT), Dhaka, Bangladesh.*
