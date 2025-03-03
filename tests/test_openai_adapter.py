import os
import pytest
import yaml
from dotenv import load_dotenv
from freeplane_and_yaml.openai_adapter import OpenAIAdapter

# Load environment variables from .env file
load_dotenv()

def test_openai_adapter_integration():
    """Test the OpenAIAdapter with a real API call."""
    # Create a simple test document
    test_text = """
    # Hexagonal Architecture
    
    Hexagonal Architecture is a software design pattern that promotes separation of concerns
    by organizing code into distinct layers.
    
    ## Core Components
    
    - Domain Logic
    - Ports (interfaces)
    - Adapters (implementations)
    
    ## Benefits
    
    - Testability
    - Flexibility
    - Maintainability
    """
    
    # Create the adapter with gpt-4o-mini model to minimize costs
    adapter = OpenAIAdapter(model="gpt-4o-mini")
    
    # Generate YAML
    yaml_content = adapter.generate_mind_map_yaml(test_text)
    
    # Parse the YAML (this will fail if the output is not valid YAML)
    yaml_data = yaml.safe_load(yaml_content)
    
    # Check for basic structure
    assert 'root' in yaml_data
    assert 'children' in yaml_data['root']
    
    # Check for expected content
    assert "Hexagonal Architecture" in yaml_data['root']['title']
    
    # Print the YAML for manual inspection (only visible when tests are run with -v)
    print(f"\nGenerated YAML:\n{yaml_content}")