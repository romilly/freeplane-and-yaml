import jsonschema
import yaml
import json

def validate_mindmap_yaml(yaml_content, schema_file='mindmap_schema.json'):
    # Load the schema
    with open(schema_file, 'r') as f:
        schema = json.load(f)
    
    # Parse YAML to Python dict
    data = yaml.safe_load(yaml_content)
    
    # Validate against schema
    try:
        jsonschema.validate(instance=data, schema=schema)
        return True
    except jsonschema.exceptions.ValidationError as e:
        print(f"Validation error: {e}")
        return False

# Example usage:
yaml_content = """
root:
  title: "My Mind Map"
  note: "Example note"
  children:
    topic1:
      title: "First Topic"
      note: "First note"
"""

is_valid = validate_mindmap_yaml(yaml_content)
print(f"YAML is valid: {is_valid}")
