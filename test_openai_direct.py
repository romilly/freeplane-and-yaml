#!/usr/bin/env python3
"""
Direct test of OpenAI API with extracted text.
"""

import os
from src.freeplane_and_yaml.openai_adapter import OpenAIAdapter
from src.freeplane_and_yaml.yaml_utils import extract_yaml_from_markdown

# Read the extracted text
with open('output/A_new_look_at_habits_and_the_habit_goal.txt', 'r', encoding='utf-8') as f:
    text_content = f.read()
    
# Truncate to stay within token limits
text_content = text_content[:20000]

# Create the OpenAI adapter with gpt-4o-mini model
openai_adapter = OpenAIAdapter(model="gpt-4o-mini")

# Call the API through the adapter
print("Calling OpenAI API...")
try:
    yaml_content = openai_adapter.generate_mind_map_yaml(text_content)
    
    # Clean up and save
    with open('output/openai_direct_output.yaml', 'w', encoding='utf-8') as f:
        f.write(yaml_content)
        
    print(f"Saved OpenAI output to: output/openai_direct_output.yaml")
    
except Exception as e:
    print(f"Error: {str(e)}")