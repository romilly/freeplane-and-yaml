import os
from typing import Optional
from .llm_adapter import LLMAdapter
from .convert import converter


class TextToMindMap:
    """
    Service for converting text files to mind maps via LLM-generated YAML.
    
    This class follows the hexagonal architecture pattern, with the LLM adapter
    injected through the constructor, allowing for easy testing and flexibility
    in switching between different LLM providers.
    """
    
    def __init__(self, llm_adapter: LLMAdapter):
        """
        Initialize the service with an LLM adapter.
        
        Args:
            llm_adapter: An implementation of LLMAdapter
        """
        self.llm_adapter = llm_adapter
            
    def convert_text_file(self, input_file_path: str, output_yaml_path: str, output_mm_path: str = None) -> str:
        """
        Convert a text file to a mind map.
        
        Args:
            input_file_path: Path to the text file to convert
            output_yaml_path: Path where the YAML file should be saved
            output_mm_path: Optional path where the Freeplane .mm file should be saved
            
        Returns:
            The YAML content generated from the text
        """
        # Read the text file
        with open(input_file_path, 'r', encoding='utf-8') as f:
            text_content = f.read()
            
        # Convert text to YAML using the adapter
        yaml_content = self.llm_adapter.generate_mind_map_yaml(text_content)
        
        # Save the YAML output
        with open(output_yaml_path, 'w', encoding='utf-8') as f:
            f.write(yaml_content)
            
        # Optionally convert to Freeplane .mm format
        if output_mm_path:
            mm_content = converter(yaml_content)
            with open(output_mm_path, 'w', encoding='utf-8') as f:
                f.write(mm_content)
                
        return yaml_content