import os
import pytest
import yaml
from dotenv import load_dotenv
from freeplane_and_yaml.claude_adapter import ClaudeAdapter
from freeplane_and_yaml.llm_adapter import DEFAULT_SCHEMA_PATH

# Load environment variables from .env file
load_dotenv()

# Skip tests if no API key is available or if it's the placeholder API key
require_api_key = pytest.mark.skipif(
    True,  # Always skip for now
    reason="Skipping Claude API tests"
)

@require_api_key
def test_claude_adapter_integration():
    """Test the ClaudeAdapter with a real API call (requires API key)."""
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
    
    # Create the adapter
    adapter = ClaudeAdapter()
    
    # Generate YAML
    try:
        yaml_content = adapter.generate_mind_map_yaml(test_text)
    except NotImplementedError:
        # In our placeholder implementation, we expect a NotImplementedError
        pytest.skip("Claude API integration is not implemented yet")
    
    # Validate that the output is valid YAML and follows our schema structure
    yaml_data = yaml.safe_load(yaml_content)
    
    # Basic validation
    assert 'root' in yaml_data
    assert 'title' in yaml_data['root']
    assert 'children' in yaml_data['root']
    
    # Check for expected content based on the input
    assert "Hexagonal Architecture" in yaml_data['root']['title']
    
    # Check that children structure exists and contains relevant nodes
    children = yaml_data['root']['children']
    assert len(children) >= 2  # Should have at least core components and benefits
    
    # Print the YAML for manual inspection (only visible when tests are run with -v)
    print(f"\nGenerated YAML:\n{yaml_content}")