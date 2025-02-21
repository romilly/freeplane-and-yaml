import sys
import os
from .convert import convert_yaml_file  # Import your conversion logic


def main():
    # Check for the correct number of arguments
    if len(sys.argv) != 3:
        print("Usage: convert input.yaml output_directory")
        sys.exit(1)

    # Parse arguments
    input_file = sys.argv[1]
    output_dir = sys.argv[2]

    # Validate the input YAML file
    if not input_file.endswith(".yaml"):
        print(f"Error: {input_file} is not a valid YAML file.")
        sys.exit(1)

    if not os.path.isfile(input_file):
        print(f"Error: Input file {input_file} does not exist.")
        sys.exit(1)

    # Validate the output directory
    if not os.path.isdir(output_dir):
        print(f"Error: Output directory {output_dir} does not exist.")
        sys.exit(1)

    # Generate the `.m` file name based on the input file
    base_name = os.path.basename(input_file).replace(".yaml", ".mm")
    output_file = os.path.join(output_dir, base_name)

    # Perform the conversion
    try:
        convert_yaml_file(input_file, output_file)
        print(f"Conversion complete: {output_file}")
    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)
