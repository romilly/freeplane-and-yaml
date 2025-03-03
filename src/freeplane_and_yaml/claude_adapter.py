import json
import os
from typing import Dict, Any
from dotenv import load_dotenv
import anthropic
from .llm_adapter import LLMAdapter, DEFAULT_SCHEMA_PATH
from .yaml_utils import extract_yaml_from_markdown

# Load environment variables from .env file
load_dotenv()

class ClaudeAdapter(LLMAdapter):
    """
    Adapter for Anthropic's Claude API.
    
    This class provides an implementation of the LLMAdapter for Claude.
    It makes API calls to Claude to generate mind maps from text.
    """
    
    DEFAULT_MODEL = "claude-3-sonnet-20240229"  # Default Claude model to use
    
    def __init__(self, api_key: str = None, model: str = None):
        """
        Initialize the adapter with API credentials.
        
        Args:
            api_key: Anthropic API key, defaults to reading from ANTHROPIC_API_KEY environment variable
            model: Claude model to use, defaults to DEFAULT_MODEL
        """
        self.api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "No API key provided. Pass an API key to the constructor or "
                "set the ANTHROPIC_API_KEY environment variable in the .env file."
            )
        
        self.model = model or self.DEFAULT_MODEL
        self.client = anthropic.Anthropic(api_key=self.api_key)
            
    def generate_mind_map_yaml(self, text: str) -> str:
        """
        Generate a mind map in YAML format using Claude.
        
        Args:
            text: The text content to convert to a mind map
            
        Returns:
            A string containing the YAML representation of the mind map
        """
        # Read the schema content
        with open(DEFAULT_SCHEMA_PATH, 'r') as f:
            schema = f.read()
            
        # Make the API call to Claude
        yaml_content = self._call_claude_api(text, schema)
        
        return yaml_content
    
    def _call_claude_api(self, text: str, schema: str) -> str:
        """
        Call the Claude API with the text and schema.
        
        Args:
            text: The text content to convert to a mind map
            schema: The JSON schema content
            
        Returns:
            The generated YAML content
        """
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                temperature=0.2,
                system="You are an expert at creating structured mind maps in YAML format. Your task is to organize the provided text into a hierarchical structure that follows the schema exactly. Every node must include both a title and a descriptive note providing context or details for that node. Only output valid YAML without any explanations, markdown code blocks, or extra text.",
                messages=[{
                    "role": "user", 
                    "content": [
                        {
                            "type": "text", 
                            "text": """I'd like you to summarise a document as a yaml file following a schema.

Please respond with ONLY the YAML content that follows the schema, without any additional text or explanations.
The YAML should have a root node with an appropriate title and organized children nodes that capture
the key points and structure of the text.

IMPORTANT: Every node (including the root and ALL child nodes) should include both a title AND a note. 
The note should provide additional context, explanation, or details about that specific node."""
                        },
                        {
                            "type": "text", 
                            "text": f"Here is the schema to follow:\n\n{schema}"
                        },
                        {
                            "type": "text", 
                            "text": f"Here is the document to summarize:\n\n{text}"
                        }
                    ]
                }]
            )
            
            # Extract the response content
            content = message.content[0].text
            
            # Use the utility function to extract YAML from markdown
            content = extract_yaml_from_markdown(content)
                
            return content
            
        except Exception as e:
            raise RuntimeError(f"Error calling Claude API: {str(e)}") from e
        
    
