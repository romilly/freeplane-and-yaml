#!/usr/bin/env python3
"""
Test the YAML cleaning utility on existing files.
"""

from src.freeplane_and_yaml.yaml_utils import extract_yaml_from_markdown

# Input and output file paths
input_file = 'output/direct_claude_output.yaml'
output_file = 'output/clean_claude_output.yaml'

print(f"Reading raw Claude output from: {input_file}")
with open(input_file, 'r', encoding='utf-8') as f:
    raw_content = f.read()
    
# Clean up the content
cleaned_yaml = extract_yaml_from_markdown(raw_content)

# Save cleaned content
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(cleaned_yaml)
    
print(f"Cleaned YAML saved to: {output_file}")
print(f"Original file preserved at: {input_file}")