import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

def create_drawio_xml(diagram_name, cells):
    mxfile = ET.Element("mxfile", host="app.diagrams.net", modified="2026-09-05T08:00:00.000Z", agent="Antigravity", version="24.0.0")
    diagram = ET.SubElement(mxfile, "diagram", name=diagram_name, id=diagram_name.lower().replace(" ", "_"))
    model = ET.SubElement(diagram, "mxGraphModel", dx="1200", dy="900", grid="1", gridSize="10", guides="1", tooltips="1", connect="1", arrows="1", fold="1", page="1", pageScale="1", pageWidth="1200", pageHeight="1400", math="0", shadow="0")
    root = ET.SubElement(model, "root")
    
    cell0 = ET.SubElement(root, "mxCell", id="0")
    cell1 = ET.SubElement(root, "mxCell", id="1", parent="0")
    
    for c in cells:
        cell_elem = ET.SubElement(root, "mxCell", id=str(c['id']), parent="1")
        if 'value' in c:
            cell_elem.set("value", c['value'])
        if 'style' in c:
            cell_elem.set("style", c['style'])
        if 'vertex' in c:
            cell_elem.set("vertex", "1")
        if 'edge' in c:
            cell_elem.set("edge", "1")
        if 'source' in c:
            cell_elem.set("source", str(c['source']))
        if 'target' in c:
            cell_elem.set("target", str(c['target']))
            
        if 'geometry' in c:
            g = c['geometry']
            geo = ET.SubElement(cell_elem, "mxGeometry", x=str(g.get('x', 0)), y=str(g.get('y', 0)), width=str(g.get('w', 0)), height=str(g.get('h', 0)))
            geo.set("as", "geometry")
            if 'relative' in g:
                geo.set("relative", "1")
                
    rough_string = ET.tostring(mxfile, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

# ==========================================
# 1. Figure 1: Proposed Methodology
# ==========================================
def build_fig1_drawio():
    cells = []
    
    # Styles
    s_orange = "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFE6CC;strokeColor=#D79B00;fontFamily=Helvetica;fontSize=13;fontStyle=1;strokeWidth=1.5;"
    s_cylinder = "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=15;fillColor=#D5E8D4;strokeColor=#82B366;fontFamily=Helvetica;fontSize=12;fontStyle=1;strokeWidth=1.5;"
    s_yellow = "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontFamily=Helvetica;fontSize=13;fontStyle=1;strokeWidth=1.5;"
    s_purple = "rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontFamily=Helvetica;fontSize=13;fontStyle=1;strokeWidth=1.5;"
    s_callout = "rounded=1;whiteSpace=wrap;html=1;dashed=1;dashPattern=5 5;fillColor=#F8F9FA;strokeColor=#7F8C8D;fontFamily=Helvetica;fontSize=11;align=left;spacingLeft=10;strokeWidth=1.2;"
    s_edge = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#2C3E50;strokeWidth=1.5;endArrow=classic;endFill=1;"
    s_dashed_edge = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#7F8C8D;strokeWidth=1.2;dashed=1;endArrow=classic;endFill=1;"

    # 1. Data Collection Phase
    cells.append({'id': 101, 'value': 'Data Collection Phase', 'style': s_orange, 'vertex': True, 'geometry': {'x': 100, 'y': 60, 'w': 180, 'h': 60}})
    # 2. Citrus Dataset
    cells.append({'id': 102, 'value': 'Citrus Dataset', 'style': s_cylinder, 'vertex': True, 'geometry': {'x': 380, 'y': 50, 'w': 160, 'h': 80}})
    # Edge 101 -> 102
    cells.append({'id': 201, 'style': s_edge, 'edge': True, 'source': 101, 'target': 102, 'geometry': {'relative': 1}})
    
    # Classes Callout
    cells.append({'id': 103, 'value': '• Greening<br>• Canker<br>• Blackspot<br>• Healthy', 'style': s_callout, 'vertex': True, 'geometry': {'x': 620, 'y': 50, 'w': 150, 'h': 80}})
    cells.append({'id': 202, 'style': s_dashed_edge, 'edge': True, 'source': 102, 'target': 103, 'geometry': {'relative': 1}})
    
    # 3 Partitions
    cells.append({'id': 104, 'value': 'Test Dataset', 'style': s_cylinder, 'vertex': True, 'geometry': {'x': 160, 'y': 190, 'w': 130, 'h': 65}})
    cells.append({'id': 105, 'value': 'Train Dataset', 'style': s_cylinder, 'vertex': True, 'geometry': {'x': 395, 'y': 190, 'w': 130, 'h': 65}})
    cells.append({'id': 106, 'value': 'Validation Dataset', 'style': s_cylinder, 'vertex': True, 'geometry': {'x': 630, 'y': 190, 'w': 130, 'h': 65}})
    
    cells.append({'id': 203, 'style': s_edge, 'edge': True, 'source': 102, 'target': 104, 'geometry': {'relative': 1}})
    cells.append({'id': 204, 'style': s_edge, 'edge': True, 'source': 102, 'target': 105, 'geometry': {'relative': 1}})
    cells.append({'id': 205, 'style': s_edge, 'edge': True, 'source': 102, 'target': 106, 'geometry': {'relative': 1}})
    
    # 3. Data Preprocessing
    cells.append({'id': 107, 'value': 'Data Preprocessing', 'style': s_orange, 'vertex': True, 'geometry': {'x': 365, 'y': 310, 'w': 190, 'h': 60}})
    cells.append({'id': 206, 'style': s_edge, 'edge': True, 'source': 105, 'target': 107, 'geometry': {'relative': 1}})
    
    cells.append({'id': 108, 'value': '• Rescale [0, 1]<br>• Rotate (±20°)<br>• Translation (20%)<br>• Shear &amp; Zoom<br>• Horizontal Flip', 'style': s_callout, 'vertex': True, 'geometry': {'x': 630, 'y': 295, 'w': 160, 'h': 90}})
    cells.append({'id': 207, 'style': s_dashed_edge, 'edge': True, 'source': 107, 'target': 108, 'geometry': {'relative': 1}})
    
    # 4. Load Pre-trained Models
    cells.append({'id': 109, 'value': 'Load Pre-Trained Models', 'style': s_orange, 'vertex': True, 'geometry': {'x': 365, 'y': 440, 'w': 190, 'h': 60}})
    cells.append({'id': 208, 'style': s_edge, 'edge': True, 'source': 107, 'target': 109, 'geometry': {'relative': 1}})
    
    cells.append({'id': 110, 'value': '• InceptionV3<br>• VGG19<br>• MobileNetV2<br>• ResNet50', 'style': s_callout, 'vertex': True, 'geometry': {'x': 630, 'y': 430, 'w': 160, 'h': 80}})
    cells.append({'id': 209, 'style': s_dashed_edge, 'edge': True, 'source': 109, 'target': 110, 'geometry': {'relative': 1}})
    
    # 5. Train and Validate the Models
    cells.append({'id': 111, 'value': 'Train and Validate<br>the Models', 'style': s_yellow, 'vertex': True, 'geometry': {'x': 365, 'y': 570, 'w': 190, 'h': 65}})
    cells.append({'id': 210, 'style': s_edge, 'edge': True, 'source': 109, 'target': 111, 'geometry': {'relative': 1}})
    
    # Inputs from Left (Train Dataset) & (Validation Dataset)
    cells.append({'id': 112, 'value': 'Train Dataset', 'style': s_cylinder, 'vertex': True, 'geometry': {'x': 140, 'y': 540, 'w': 120, 'h': 55}})
    cells.append({'id': 113, 'value': 'Validation Dataset', 'style': s_cylinder, 'vertex': True, 'geometry': {'x': 140, 'y': 610, 'w': 120, 'h': 55}})
    cells.append({'id': 211, 'style': s_edge, 'edge': True, 'source': 112, 'target': 111, 'geometry': {'relative': 1}})
    cells.append({'id': 212, 'style': s_edge, 'edge': True, 'source': 113, 'target': 111, 'geometry': {'relative': 1}})
    
    # Evaluate Model Complexity
    cells.append({'id': 114, 'value': 'Evaluate Model<br>Complexity', 'style': s_purple, 'vertex': True, 'geometry': {'x': 630, 'y': 570, 'w': 160, 'h': 65}})
    cells.append({'id': 213, 'style': s_edge, 'edge': True, 'source': 111, 'target': 114, 'geometry': {'relative': 1}})
    
    cells.append({'id': 115, 'value': '• Training Time<br>• Testing Time<br>• Memory Footprint', 'style': s_callout, 'vertex': True, 'geometry': {'x': 630, 'y': 670, 'w': 160, 'h': 70}})
    cells.append({'id': 214, 'style': s_dashed_edge, 'edge': True, 'source': 114, 'target': 115, 'geometry': {'relative': 1}})
    
    # 6. Test the Model
    cells.append({'id': 116, 'value': 'Test the Model', 'style': s_yellow, 'vertex': True, 'geometry': {'x': 365, 'y': 780, 'w': 190, 'h': 65}})
    cells.append({'id': 215, 'style': s_edge, 'edge': True, 'source': 111, 'target': 116, 'geometry': {'relative': 1}})
    
    cells.append({'id': 117, 'value': 'Test Dataset', 'style': s_cylinder, 'vertex': True, 'geometry': {'x': 140, 'y': 785, 'w': 120, 'h': 55}})
    cells.append({'id': 216, 'style': s_edge, 'edge': True, 'source': 117, 'target': 116, 'geometry': {'relative': 1}})
    
    # Evaluate Model Performance
    cells.append({'id': 118, 'value': 'Evaluate Model<br>Performance', 'style': s_purple, 'vertex': True, 'geometry': {'x': 630, 'y': 780, 'w': 160, 'h': 65}})
    cells.append({'id': 217, 'style': s_edge, 'edge': True, 'source': 116, 'target': 118, 'geometry': {'relative': 1}})
    
    cells.append({'id': 119, 'value': '• Accuracy<br>• Precision<br>• F1-Score<br>• Confusion Matrix', 'style': s_callout, 'vertex': True, 'geometry': {'x': 630, 'y': 880, 'w': 160, 'h': 80}})
    cells.append({'id': 218, 'style': s_dashed_edge, 'edge': True, 'source': 118, 'target': 119, 'geometry': {'relative': 1}})
    
    return create_drawio_xml("Proposed Methodology Flowchart", cells)

# ==========================================
# 2. Figure 5: Flowchart of Pre-Trained Models
# ==========================================
def build_fig5_drawio():
    cells = []
    s_yellow = "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontFamily=Helvetica;fontSize=13;fontStyle=1;strokeWidth=1.5;"
    s_green = "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontFamily=Helvetica;fontSize=12;fontStyle=1;strokeWidth=1.5;"
    s_models = "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontFamily=Helvetica;fontSize=13;fontStyle=1;strokeWidth=1.5;align=center;"
    s_edge = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#2C3E50;strokeWidth=1.5;endArrow=classic;endFill=1;"

    # 1. Raw Dataset
    cells.append({'id': 101, 'value': 'Raw Dataset', 'style': s_yellow, 'vertex': True, 'geometry': {'x': 320, 'y': 50, 'w': 200, 'h': 55}})
    # 2. Pre-Processing
    cells.append({'id': 102, 'value': 'Pre-Processing', 'style': s_yellow, 'vertex': True, 'geometry': {'x': 320, 'y': 150, 'w': 200, 'h': 55}})
    cells.append({'id': 201, 'style': s_edge, 'edge': True, 'source': 101, 'target': 102, 'geometry': {'relative': 1}})
    
    # 3. 3-way Split
    cells.append({'id': 103, 'value': 'Training Dataset', 'style': s_green, 'vertex': True, 'geometry': {'x': 100, 'y': 270, 'w': 160, 'h': 55}})
    cells.append({'id': 104, 'value': 'Pre-Trained Models<br><br><span style="font-size: 11px; font-weight: normal; color: #555;">(ResNet50, VGG19,<br>InceptionV3, MobileNetV2)</span>', 'style': s_models, 'vertex': True, 'geometry': {'x': 300, 'y': 250, 'w': 240, 'h': 95}})
    cells.append({'id': 105, 'value': 'Validation Dataset', 'style': s_green, 'vertex': True, 'geometry': {'x': 580, 'y': 270, 'w': 160, 'h': 55}})
    
    cells.append({'id': 202, 'style': s_edge, 'edge': True, 'source': 102, 'target': 103, 'geometry': {'relative': 1}})
    cells.append({'id': 203, 'style': s_edge, 'edge': True, 'source': 102, 'target': 104, 'geometry': {'relative': 1}})
    cells.append({'id': 204, 'style': s_edge, 'edge': True, 'source': 102, 'target': 105, 'geometry': {'relative': 1}})
    
    cells.append({'id': 205, 'style': s_edge, 'edge': True, 'source': 103, 'target': 104, 'geometry': {'relative': 1}})
    cells.append({'id': 206, 'style': s_edge, 'edge': True, 'source': 105, 'target': 104, 'geometry': {'relative': 1}})
    
    # 4. Categorize the Disease
    cells.append({'id': 106, 'value': 'Categorize the Disease', 'style': s_yellow, 'vertex': True, 'geometry': {'x': 320, 'y': 400, 'w': 200, 'h': 55}})
    cells.append({'id': 207, 'style': s_edge, 'edge': True, 'source': 104, 'target': 106, 'geometry': {'relative': 1}})
    
    # 5. Evaluate with Testing Dataset
    cells.append({'id': 107, 'value': 'Evaluate with<br>Testing Dataset', 'style': s_yellow, 'vertex': True, 'geometry': {'x': 320, 'y': 510, 'w': 200, 'h': 65}})
    cells.append({'id': 208, 'style': s_edge, 'edge': True, 'source': 106, 'target': 107, 'geometry': {'relative': 1}})
    
    # Test Dataset on the left
    cells.append({'id': 108, 'value': 'Test Dataset', 'style': s_green, 'vertex': True, 'geometry': {'x': 100, 'y': 515, 'w': 160, 'h': 55}})
    cells.append({'id': 209, 'style': s_edge, 'edge': True, 'source': 108, 'target': 107, 'geometry': {'relative': 1}})
    
    return create_drawio_xml("Pre-Trained Models Workflow", cells)

# ==========================================
# 3. Figure 6: TensorFlow Architecture
# ==========================================
def build_fig6_drawio():
    cells = []
    s_blue = "rounded=1;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;fontFamily=Helvetica;fontSize=12;fontStyle=1;strokeWidth=1.5;"
    s_yellow = "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF2CC;strokeColor=#D6B656;fontFamily=Helvetica;fontSize=12;fontStyle=1;strokeWidth=1.5;"
    s_green = "rounded=1;whiteSpace=wrap;html=1;fillColor=#D5E8D4;strokeColor=#82B366;fontFamily=Helvetica;fontSize=12;fontStyle=1;strokeWidth=1.5;"
    s_purple = "rounded=1;whiteSpace=wrap;html=1;fillColor=#E1D5E7;strokeColor=#9673A6;fontFamily=Helvetica;fontSize=12;fontStyle=1;strokeWidth=1.5;"
    s_edge = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#2C3E50;strokeWidth=1.5;endArrow=classic;endFill=1;"

    cells.append({'id': 101, 'value': 'Data Input Pipeline<br>(tf.data &amp; Augmentation)', 'style': s_blue, 'vertex': True, 'geometry': {'x': 100, 'y': 50, 'w': 200, 'h': 60}})
    cells.append({'id': 102, 'value': 'Model Architecture &amp; Layers<br>(Keras Functional API)', 'style': s_yellow, 'vertex': True, 'geometry': {'x': 360, 'y': 50, 'w': 200, 'h': 60}})
    cells.append({'id': 103, 'value': 'Training &amp; Optimization<br>(Adam, Cross-Entropy)', 'style': s_yellow, 'vertex': True, 'geometry': {'x': 620, 'y': 50, 'w': 200, 'h': 60}})
    
    cells.append({'id': 201, 'style': s_edge, 'edge': True, 'source': 101, 'target': 102, 'geometry': {'relative': 1}})
    cells.append({'id': 202, 'style': s_edge, 'edge': True, 'source': 102, 'target': 103, 'geometry': {'relative': 1}})
    
    cells.append({'id': 104, 'value': 'SavedModel Serialization<br>(Weights &amp; Computation Graph)', 'style': s_purple, 'vertex': True, 'geometry': {'x': 360, 'y': 160, 'w': 200, 'h': 60}})
    cells.append({'id': 203, 'style': s_edge, 'edge': True, 'source': 103, 'target': 104, 'geometry': {'relative': 1}})
    
    cells.append({'id': 105, 'value': 'Edge Deployment<br>(TensorFlow Lite / Mobile)', 'style': s_green, 'vertex': True, 'geometry': {'x': 180, 'y': 280, 'w': 200, 'h': 60}})
    cells.append({'id': 106, 'value': 'Cloud Serving<br>(TF Serving REST / gRPC)', 'style': s_green, 'vertex': True, 'geometry': {'x': 540, 'y': 280, 'w': 200, 'h': 60}})
    
    cells.append({'id': 204, 'style': s_edge, 'edge': True, 'source': 104, 'target': 105, 'geometry': {'relative': 1}})
    cells.append({'id': 205, 'style': s_edge, 'edge': True, 'source': 104, 'target': 106, 'geometry': {'relative': 1}})
    
    return create_drawio_xml("TensorFlow Framework Architecture", cells)

import os
os.makedirs('/home/neo/Documents/research-publish/citrus-disease-classification/diagrams', exist_ok=True)

with open('/home/neo/Documents/research-publish/citrus-disease-classification/diagrams/figure1_proposed_methodology.drawio', 'w') as f:
    f.write(build_fig1_drawio())

with open('/home/neo/Documents/research-publish/citrus-disease-classification/diagrams/figure5_pretrained_workflow.drawio', 'w') as f:
    f.write(build_fig5_drawio())

with open('/home/neo/Documents/research-publish/citrus-disease-classification/diagrams/figure6_tensorflow_architecture.drawio', 'w') as f:
    f.write(build_fig6_drawio())

print('Created all 3 .drawio files in diagrams/ directory successfully!')
