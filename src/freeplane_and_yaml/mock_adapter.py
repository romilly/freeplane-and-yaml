from .llm_adapter import LLMAdapter, DEFAULT_SCHEMA_PATH

class MockLLMAdapter(LLMAdapter):
    """
    Mock implementation of the LLMAdapter for testing.
    
    This adapter returns predefined YAML content instead of making actual API calls.
    """
    
    def __init__(self, yaml_response: str = None):
        """
        Initialize the mock adapter with an optional predefined YAML response.
        
        Args:
            yaml_response: Optional predefined YAML to return
        """
        self.yaml_response = yaml_response
        self.last_text = None  # Store the last text received for verification in tests
        
    def generate_mind_map_yaml(self, text: str) -> str:
        """
        Return the predefined YAML response instead of generating one.
        
        Args:
            text: The text content (will be stored but not used)
            
        Returns:
            The predefined YAML response
        """
        # Store the input for verification in tests
        self.last_text = text
        
        # Return the predefined response
        if self.yaml_response is None:
            # Return a simple default response if none was provided
            return """root:
  title: Sample Mind Map
  note: Generated by MockLLMAdapter
  children:
    topic1:
      title: First Topic
      note: First topic note
    topic2:
      title: Second Topic
      note: Second topic note
"""
        return self.yaml_response