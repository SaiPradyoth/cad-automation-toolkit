# CAD Automation Toolkit

A Python-based project to explore **CAD workflow automation**.  
This toolkit is being developed as part of my engineering portfolio to show how **software can accelerate product design, validation, and manufacturing**.

---

## ✨ Features (Planned)
- **Parametric Part Generation** – Create CAD models from JSON/CSV inputs.  
- **Tolerance Stack-Up Analysis** – Automate GD&T calculations.  
- **Batch Export** – Export to STEP, IGES, and DXF in one go.  
- **Validation Integration** – Connect with FEA tools (ABAQUS/ANSYS) for stress & thermal analysis.  

---

## Repository Structure
---
## 🖥️ Example Run

When running `hello.py`, the toolkit loads CAD parameters from JSON files:

CAD Automation Toolkit initialized!

📐 Single Part Configuration Loaded:
part_name: mounting_bracket
length_mm: 120
width_mm: 40
thickness_mm: 5
hole_diameter_mm: 10
material: Aluminum 6061

📂 Scanning examples folder...

🔹 Loading bracket_example.json...
part_name: mounting_bracket
length_mm: 120
width_mm: 40
thickness_mm: 5
hole_diameter_mm: 10
material: Aluminum 6061

🔹 Loading plate_example.json...
part_name: base_plate
length_mm: 200
width_mm: 150
thickness_mm: 10
hole_diameter_mm: 12
material: Stainless Steel 304
