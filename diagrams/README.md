# 📊 Visual Diagrams (Draw.io / diagrams.net Source of Truth)

This folder contains the editable source files for all system diagrams and methodology flowcharts used in the manuscript.

---

## 📁 Diagram Files

| File | Diagram Description | In-Paper Figure |
| :--- | :--- | :--- |
| [`figure1_proposed_methodology.drawio`](./figure1_proposed_methodology.drawio) | End-to-end multi-stage research methodology flowchart | **Figure 1** |
| [`figure5_pretrained_workflow.drawio`](./figure5_pretrained_workflow.drawio) | Transfer learning fine-tuning and classification pipeline | **Figure 5** |
| [`figure6_tensorflow_architecture.drawio`](./figure6_tensorflow_architecture.drawio) | Training, serialization, and edge/cloud deployment framework | **Figure 6** |

---

## 🛠️ How to View & Edit in draw.io

You can edit these diagrams with full visual control using either of the following methods:

### Option 1: Directly in Browser via app.diagrams.net (Recommended)
1. Go to [**app.diagrams.net**](https://app.diagrams.net/) (or [draw.io](https://draw.io)).
2. Click **"Open from GitHub"** or **"Open Existing Diagram"**.
3. Select this repository: `abdullahmiraz/citrus-disease-classification`.
4. Choose the `.drawio` file from the `diagrams/` folder.
5. Modify nodes, text, colors, or connections visually.
6. Click **File $\rightarrow$ Save** to commit your changes directly to the GitHub repository!

### Option 2: In VS Code / Antigravity IDE
1. Install the **"Draw.io Integration"** extension (`hediet.vscode-drawio`).
2. Simply click any `.drawio` file in the file explorer to open the interactive diagram editor inside your IDE.

---

## 🔄 Syncing with LaTeX / Overleaf

When you modify any `.drawio` diagram:
1. Export as **PNG (300 DPI)** or **PDF (Cropped)** from draw.io.
2. Save the exported image into the `figures/` folder.
3. The LaTeX manuscript and Overleaf project will automatically load the updated figure!
