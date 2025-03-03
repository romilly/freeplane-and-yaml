import json
import os
from typing import Dict, Any
from dotenv import load_dotenv
import anthropic
from .llm_adapter import LLMAdapter, DEFAULT_SCHEMA_PATH

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
            
        # Construct a prompt for Claude
        prompt = self._construct_prompt(text, schema)
        
        # Make the API call to Claude
        yaml_content = self._call_claude_api(prompt)
        
        return yaml_content
    
    def _call_claude_api(self, prompt: str) -> str:
        """
        Call the Claude API with the given prompt.
        
        Args:
            prompt: The prompt to send to Claude
            
        Returns:
            The generated YAML content
        """
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=4000,
                temperature=0.2,
                system="You are an expert at creating structured mind maps in YAML format. Your task is to organize the provided text into a hierarchical structure that follows the schema exactly. Only output valid YAML without any explanations, markdown code blocks, or extra text.",
                messages=[{"role": "user", "content": prompt}]
            )
            
            # Extract the response content
            content = message.content[0].text
            
            # Some basic preprocessing to ensure we get just the YAML
            # Remove any markdown code block syntax if present
            if content.startswith("```yaml"):
                content = content.replace("```yaml", "", 1)
                if content.endswith("```"):
                    content = content[:-3]
            elif content.startswith("```"):
                content = content.replace("```", "", 1)
                if content.endswith("```"):
                    content = content[:-3]
                    
            return content.strip()
            
        except Exception as e:
            raise RuntimeError(f"Error calling Claude API: {str(e)}") from e
        
    def _construct_prompt(self, text: str, schema: str) -> str:
        """
        Construct a prompt for Claude to generate a mind map.
        
        Args:
            text: The text content to convert to a mind map
            schema: The schema content
            
        Returns:
            A prompt string for Claude
        """
        return f"""
I need you to summarize the following text as a structured mind map in YAML format.
Please follow the schema specification provided below exactly.

# Schema:
```json
{schema}
```

# Text to summarize:
```
{text}
```

Please respond with ONLY the YAML content that follows the schema, without any additional text or explanations.
The YAML should have a root node with an appropriate title and organized children nodes that capture
the key points and structure of the text.
"""
    
    def _call_claude_api(self, prompt: str) -> str:
        """
        Call the Claude API with the given prompt.
        
        Args:
            prompt: The prompt to send to Claude
            
        Returns:
            The generated YAML content
        """
        # This would be replaced with actual API calls in a real implementation
        # For example, using the Anthropic Python client library
        
        # import anthropic
        # client = anthropic.Anthropic(api_key=self.api_key)
        # message = client.messages.create(
        #     model="claude-3-sonnet-20240229",
        #     max_tokens=4000,
        #     temperature=0.2,
        #     system="You are an expert at creating structured mind maps in YAML format.",
        #     messages=[{"role": "user", "content": prompt}]
        # )
        # return message.content[0].text
        
        pass