# 📊 Visual Diagrams (Draw.io / diagrams.net Source of Truth)

This directory contains the editable source files for all architecture and methodology diagrams used in the manuscript.

---

## 📁 Diagram Files

| File | Diagram Description | In-Paper Figure |
| :--- | :--- | :--- |
| [`fig1_methodology.drawio`](./fig1_methodology.drawio) | End-to-end multi-stage research methodology flowchart | **Figure 1** |
| [`fig5_pretrained_workflow.drawio`](./fig5_pretrained_workflow.drawio) | Transfer learning fine-tuning and classification pipeline | **Figure 5** |
| [`fig6_tensorflow_architecture.drawio`](./fig6_tensorflow_architecture.drawio) | Training, serialization, and edge/cloud deployment framework | **Figure 6** |

---

## 🛠️ How to View & Edit in draw.io

You can edit these diagrams visually using either of the following methods:

### Option 1: Directly in Browser via app.diagrams.net (Recommended)
1. Go to [**app.diagrams.net**](https://app.diagrams.net/) (or [draw.io](https://draw.io)).
2. Click **"Open from GitHub"** $\rightarrow$ select `abdullahmiraz/citrus-disease-classification`.
3. Choose any diagram from the `diagrams/` folder (e.g., [`fig1_methodology.drawio`](./fig1_methodology.drawio)).
4. Make edits visually and press `Ctrl+S` / `Cmd+S` to **commit directly back to GitHub**!

### Option 2: In VS Code / Antigravity IDE
1. Install the **"Draw.io Integration"** extension (`hediet.vscode-drawio`).
2. Click any `.drawio` file to open the visual diagram canvas directly inside your IDE.

---

## 🔄 Syncing with LaTeX / Overleaf

When you modify any `.drawio` diagram:
1. Export as **PNG (300 DPI)** or **PDF (Cropped)** from draw.io.
2. Save the exported image into the `figures/` directory.
3. The LaTeX manuscript and Overleaf project will automatically compile with the updated figure.
