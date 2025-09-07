"""
CAD Automation Toolkit
Author: Sai Pradyoth Goparaju
Description:
    Starter script for automating CAD workflows.
    - Reads part parameters from JSON input files
    - Prints part configuration for verification
"""

import json
import os

def load_part(file_path):
    """Load part parameters from a JSON file."""
    with open(file_path, "r") as f:
        return json.load(f)

def main():
    print(" CAD Automation Toolkit initialized!")

    # Path to example file
    example_file = os.path.join("examples", "bracket_example.json")

    # Check if file exists
    if os.path.exists(example_file):
        part = load_part(example_file)
        print("\n Part Configuration Loaded:")
        for key, value in part.items():
            print(f"  {key}: {value}")
    else:
        print("⚠ No example file found. Please add JSON input to /examples.")

if __name__ == "__main__":
    main()
