"""
CAD Automation Toolkit
Author: Sai Pradyoth Goparaju
Description:
    - Reads part parameters from JSON input files
    - Prints part configuration for verification
    - Creates 3D CAD parts in FreeCAD
"""

import json
import os

# FreeCAD imports
import FreeCAD, Part

def load_part(file_path):
    """Load part parameters from a JSON file."""
    with open(file_path, "r") as f:
        return json.load(f)

def create_plate(params):
    """Create a plate with optional hole from parameters."""
    length = params["length_mm"]
    width = params["width_mm"]
    thickness = params["thickness_mm"]
    hole_dia = params["hole_diameter_mm"]

    # Create base box
    plate = Part.makeBox(length, width, thickness)

    # Create hole (at 20,20 for demo)
    hole = Part.makeCylinder(hole_dia/2, thickness)
    hole.translate(FreeCAD.Vector(20, 20, 0))

    return plate.cut(hole)

def scan_examples():
    """Scan all JSON files in examples/ and create CAD parts."""
    examples_folder = "examples"

    if os.path.exists(examples_folder):
        print("\n📂 Scanning examples folder...")
        files = [f for f in os.listdir(examples_folder) if f.endswith(".json")]

        if files:
            doc = FreeCAD.newDocument("CAD_Automation")
            for file in files:
                print(f"\n🔹 Loading {file}...")
                part_data = load_part(os.path.join(examples_folder, file))
                for key, value in part_data.items():
                    print(f"  {key}: {value}")

                # Generate CAD geometry
                shape = create_plate(part_data)
                obj = doc.addObject("Part::Feature", part_data["part_name"])
                obj.Shape = shape

            doc.recompute()
            print("\n✅ CAD parts generated in FreeCAD document!")
        else:
            print("⚠️ No JSON files found in examples/")
    else:
        print("⚠️ No examples folder found. Please add input files.")

def main():
    print("🚀 CAD Automation Toolkit initialized!")

    # Run single-file preview (first bracket)
    example_file = os.path.join("examples", "bracket_example.json")
    if os.path.exists(example_file):
        part = load_part(example_file)
        print("\n📐 Single Part Configuration Loaded:")
        for key, value in part.items():
            print(f"  {key}: {value}")

    # Multi-part + CAD creation
    scan_examples()

if __name__ == "__main__":
    main()
