import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']

def draw_cylinder(ax, x, y, w, h, color='#D5E8D4', ec='#2C3E50', lw=1.5, label=''):
    """Draw a clean 3D database cylinder."""
    r_h = h * 0.28
    
    # Body
    rect = patches.Rectangle((x - w/2, y - h/2), w, h, facecolor=color, edgecolor='none')
    ax.add_patch(rect)
    
    # Bottom ellipse
    bottom = Ellipse((x, y - h/2), w, r_h, facecolor=color, edgecolor=ec, lw=lw)
    ax.add_patch(bottom)
    
    # Side lines
    ax.plot([x - w/2, x - w/2], [y - h/2, y + h/2], color=ec, lw=lw)
    ax.plot([x + w/2, x + w/2], [y - h/2, y + h/2], color=ec, lw=lw)
    
    # Top ellipse
    top = Ellipse((x, y + h/2), w, r_h, facecolor=color, edgecolor=ec, lw=lw)
    ax.add_patch(top)
    
    # Label
    if label:
        ax.text(x, y - 0.03*h, label, ha='center', va='center', fontsize=8.5, fontweight='bold', color='#1A252F', linespacing=1.2)

def draw_box(ax, x, y, w, h, color='#FFF2CC', ec='#2C3E50', lw=1.5, label='', subtitle='', 
             style='round,pad=0.015,rounding_size=0.02', dashed=False, text_color='#1A252F', 
             title_color='#1A252F', fs_title=9.5, fs_sub=8.2, ha_sub='center'):
    """Draw a styled box with title and optional multiline subtitle."""
    ls = '--' if dashed else '-'
    box = FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle=style,
                         facecolor=color, edgecolor=ec, linewidth=lw, linestyle=ls)
    ax.add_patch(box)
    
    if label and subtitle:
        ax.text(x, y + h*0.22, label, ha='center', va='center', fontsize=fs_title, fontweight='bold', color=title_color)
        sub_x = x if ha_sub == 'center' else (x - w/2 + 1.2)
        ax.text(sub_x, y - h*0.22, subtitle, ha=ha_sub, va='center', fontsize=fs_sub, color=text_color, linespacing=1.3)
    elif label:
        ax.text(x, y, label, ha='center', va='center', fontsize=fs_title, fontweight='bold', color=title_color, linespacing=1.2)
    elif subtitle:
        sub_x = x if ha_sub == 'center' else (x - w/2 + 1.2)
        ax.text(sub_x, y, subtitle, ha=ha_sub, va='center', fontsize=fs_sub, color=text_color, linespacing=1.3)

def draw_arrow(ax, p1, p2, color='#2C3E50', lw=1.5, connectionstyle='arc3,rad=0'):
    """Draw an arrow from p1 to p2."""
    arrow = FancyArrowPatch(p1, p2,
                            arrowstyle='-|>',
                            mutation_scale=13,
                            linewidth=lw,
                            color=color,
                            connectionstyle=connectionstyle)
    ax.add_patch(arrow)

# ==========================================
# GENERATE FIGURE 1: Proposed Methodology
# ==========================================
def generate_figure_1():
    fig, ax = plt.subplots(figsize=(11, 10.5), dpi=300)
    ax.set_xlim(0, 110)
    ax.set_ylim(0, 106)
    ax.axis('off')
    
    c_orange = '#FFE6CC'   # Data Collection / Preprocessing
    c_green = '#D5E8D4'    # Datasets
    c_yellow = '#FFF2CC'   # Training / Testing
    c_purple = '#E1D5E7'   # Complexity / Performance
    c_callout = '#FAFBFD'  # Dashed detail boxes
    
    # 1. Top Section: Data Collection Phase -> Citrus Dataset -> Class Callout
    draw_box(ax, 14, 98, 20, 6.8, c_orange, label='Data Collection\nPhase', fs_title=9)
    draw_cylinder(ax, 43, 98, 17, 7, c_green, label='Citrus\nDataset')
    draw_arrow(ax, (24, 98), (34.5, 98))
    
    # Callout for Citrus Dataset classes (top right)
    draw_box(ax, 74, 98, 22, 8.5, c_callout, ec='#7F8C8D', lw=1.2, dashed=True,
             subtitle='• Greening\n• Canker\n• Blackspot\n• Healthy', fs_sub=8, ha_sub='left')
    draw_arrow(ax, (51.5, 98), (63, 98), color='#7F8C8D', lw=1.2)
    
    # 2. Dataset Splitting: 3 Cylinder branches
    draw_cylinder(ax, 19, 83, 13, 6.2, c_green, label='Test\nDataset')
    draw_cylinder(ax, 43, 83, 13, 6.2, c_green, label='Train\nDataset')
    draw_cylinder(ax, 67, 83, 13, 6.2, c_green, label='Validation\nDataset')
    
    # Arrows from Citrus Dataset down to 3 partitions
    draw_arrow(ax, (38, 93), (21, 87), connectionstyle='arc3,rad=0.08')
    draw_arrow(ax, (43, 93), (43, 87))
    draw_arrow(ax, (48, 93), (65, 87), connectionstyle='arc3,rad=-0.08')
    
    # 3. Data Preprocessing (below Train Dataset)
    draw_box(ax, 43, 68, 22, 6.8, c_orange, label='Data\nPreprocessing', fs_title=9)
    draw_arrow(ax, (43, 78.5), (43, 72))
    
    # Callout for Preprocessing
    draw_box(ax, 74, 68, 23, 10.5, c_callout, ec='#7F8C8D', lw=1.2, dashed=True,
             subtitle='• Rescale [0, 1]\n• Rotate (±20°)\n• Translation (20%)\n• Shear & Zoom\n• Horizontal Flip', fs_sub=8, ha_sub='left')
    draw_arrow(ax, (54, 68), (62.5, 68), color='#7F8C8D', lw=1.2)
    
    # 4. Load Pre-trained Models (below Preprocessing)
    draw_box(ax, 43, 53, 22, 6.8, c_orange, label='Load Pre-Trained\nModels', fs_title=9)
    draw_arrow(ax, (43, 64.6), (43, 57))
    
    # Callout for Pre-trained models
    draw_box(ax, 74, 53, 23, 8.5, c_callout, ec='#7F8C8D', lw=1.2, dashed=True,
             subtitle='• InceptionV3\n• VGG19\n• MobileNetV2\n• ResNet50', fs_sub=8, ha_sub='left')
    draw_arrow(ax, (54, 53), (62.5, 53), color='#7F8C8D', lw=1.2)
    
    # 5. Train and Validate the Models (central box)
    draw_box(ax, 43, 34, 22, 7.5, c_yellow, label='Train and Validate\nthe Models', fs_title=9)
    draw_arrow(ax, (43, 49.6), (43, 38.5))
    
    # Inputs: Train Dataset and Validation Dataset
    draw_cylinder(ax, 14, 38, 13, 5.8, c_green, label='Train\nDataset')
    draw_arrow(ax, (20.5, 38), (32, 35.5))
    
    draw_cylinder(ax, 14, 29, 13, 5.8, c_green, label='Validation\nDataset')
    draw_arrow(ax, (20.5, 29), (32, 32.5))
    
    # Right: Evaluate Model Complexity
    draw_box(ax, 74, 34, 23, 7.5, c_purple, label='Evaluate Model\nComplexity', fs_title=9)
    draw_arrow(ax, (54, 34), (62.5, 34))
    
    # Complexity callout (below Evaluate Model Complexity)
    draw_box(ax, 74, 22, 23, 8, c_callout, ec='#7F8C8D', lw=1.2, dashed=True,
             subtitle='• Training Time\n• Testing Time\n• Memory Required', fs_sub=8, ha_sub='left')
    draw_arrow(ax, (74, 30.2), (74, 26.5), color='#7F8C8D', lw=1.2)
    
    # 6. Test the Model & Performance Evaluation (bottom section)
    draw_box(ax, 43, 10, 22, 7.5, c_yellow, label='Test the Model', fs_title=9)
    draw_arrow(ax, (43, 30.2), (43, 14.5))
    
    # Left feed cylinder for Test Dataset
    draw_cylinder(ax, 14, 10, 13, 5.8, c_green, label='Test\nDataset')
    draw_arrow(ax, (20.5, 10), (32, 10))
    
    # Right: Evaluate Model Performance
    draw_box(ax, 74, 10, 23, 7.5, c_purple, label='Evaluate Model\nPerformance', fs_title=9)
    draw_arrow(ax, (54, 10), (62.5, 10))
    
    # Performance Callout (below Evaluate Model Performance)
    draw_box(ax, 74, -2, 23, 9, c_callout, ec='#7F8C8D', lw=1.2, dashed=True,
             subtitle='• Accuracy\n• Precision\n• F1-Score\n• Confusion Matrix', fs_sub=8, ha_sub='left')
    draw_arrow(ax, (74, 6.2), (74, 2.8), color='#7F8C8D', lw=1.2)
    
    ax.set_ylim(-7, 105)
    plt.tight_layout()
    plt.savefig('/home/neo/Documents/research-publish/citrus-disease-classification/Thesis/Untitled Diagram.png', dpi=300, bbox_inches='tight')
    plt.close()
    print('Refined Figure 1 with clear layout!')

if __name__ == '__main__':
    generate_figure_1()
