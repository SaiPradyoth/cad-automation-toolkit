"""
CAD Automation Toolkit
Author: Sai Pradyoth Goparaju
Description:
    Starter script for automating CAD workflows.
    - Reads part parameters from JSON input files
    - Prints part configuration for verification
    - Scans multiple JSON input files in examples/
"""

import json
import os

def load_part(file_path):
    """Load part parameters from a JSON file."""
    with open(file_path, "r") as f:
        return json.load(f)

def scan_examples():
    """Scan all JSON files in the examples folder."""
    examples_folder = "examples"

    if os.path.exists(examples_folder):
        print("\n📂 Scanning examples folder...")
        files = [f for f in os.listdir(examples_folder) if f.endswith(".json")]

        if files:
            for file in files:
                print(f"\n🔹 Loading {file}...")
                part = load_part(os.path.join(examples_folder, file))
                for key, value in part.items():
                    print(f"  {key}: {value}")
        else:
            print("⚠️ No JSON files found in examples/")
    else:
        print("⚠️ No examples folder found. Please add input files.")

def main():
    print("🚀 CAD Automation Toolkit initialized!")

    # Run old single-file logic
    example_file = os.path.join("examples", "bracket_example.json")
    if os.path.exists(example_file):
        part = load_part(example_file)
        print("\n📐 Single Part Configuration Loaded:")
        for key, value in part.items():
            print(f"  {key}: {value}")
    else:
        print("⚠️ No bracket_example.json found.")

    # Run new multi-file logic
    scan_examples()

if __name__ == "__main__":
    main()
