
#!/usr/bin/env python3
"""
Direct test of Claude API with extracted text.
"""

import os
import json
import anthropic
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up the Claude client
api_key = os.environ.get("ANTHROPIC_API_KEY")
client = anthropic.Anthropic(api_key=api_key)

# Read the extracted text
with open('output/A_new_look_at_habits_and_the_habit_goal.txt', 'r', encoding='utf-8') as f:
    text_content = f.read()
    
# Truncate if needed for testing
text_content = text_content[:40000]

# Read the schema
with open('src/schema/mindmap-schema.json', 'r', encoding='utf-8') as f:
    schema = f.read()

# Construct the prompt
prompt = """I'd like you to summarise a document as a yaml file following a schema.

Please respond with ONLY the YAML content that follows the schema, without any additional text or explanations.
The YAML should have a root node with an appropriate title and organized children nodes that capture
the key points and structure of the text.

IMPORTANT: Every node (including the root and ALL child nodes) should include both a title AND a note. 
The note should provide additional context, explanation, or details about that specific node."""

# Call Claude API
print("Calling Claude API...")
message = client.messages.create(
    model="claude-3-sonnet-20240229",
    max_tokens=4000,
    temperature=0.2,
    system="You are an expert at creating structured mind maps in YAML format. Your task is to organize the provided text into a hierarchical structure that follows the schema exactly. Every node must include both a title and a descriptive note providing context or details for that node. Only output valid YAML without any explanations, markdown code blocks, or extra text.",
    messages=[{
        "role": "user", 
        "content": [
            {"type": "text", "text": prompt},
            {"type": "text", "text": f"Here is the schema to follow:\n\n{schema}"},
            {"type": "text", "text": f"Here is the document to summarize:\n\n{text_content}"}
        ]
    }]
)

# Extract and save the response
content = message.content[0].text

# Remove any initial text before the YAML content
if "```yaml" in content:
    content = content.split("```yaml", 1)[1]
    if "```" in content:
        content = content.split("```", 1)[0]
elif "```" in content:
    content = content.split("```", 1)[1]
    if "```" in content:
        content = content.split("```", 1)[0]

# Clean up and save
content = content.strip()
with open('output/direct_claude_output.yaml', 'w', encoding='utf-8') as f:
    f.write(content)
    
print(f"Saved Claude output to: output/direct_claude_output.yaml")