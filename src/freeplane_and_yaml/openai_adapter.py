import os
from openai import OpenAI
from typing import Dict, Any
from dotenv import load_dotenv
from .llm_adapter import LLMAdapter, DEFAULT_SCHEMA_PATH
from .yaml_utils import extract_yaml_from_markdown

# Load environment variables from .env file
load_dotenv()

class OpenAIAdapter(LLMAdapter):
    """
    Adapter for OpenAI API.
    
    This class provides an implementation of the LLMAdapter for OpenAI models.
    It makes API calls to OpenAI to generate mind maps from text.
    """
    
    DEFAULT_MODEL = "gpt-4-turbo"  # Default OpenAI model to use
    
    def __init__(self, api_key: str = None, model: str = None):
        """
        Initialize the adapter with API credentials.
        
        Args:
            api_key: OpenAI API key, defaults to reading from OPENAI_API_KEY environment variable
            model: OpenAI model to use, defaults to DEFAULT_MODEL
        """
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "No API key provided. Pass an API key to the constructor or "
                "set the OPENAI_API_KEY environment variable in the .env file."
            )
        
        self.model = model or self.DEFAULT_MODEL
        self.client = OpenAI(api_key=self.api_key)
            
    def generate_mind_map_yaml(self, text: str) -> str:
        """
        Generate a mind map in YAML format using OpenAI.
        
        Args:
            text: The text content to convert to a mind map
            
        Returns:
            A string containing the YAML representation of the mind map
        """
        # Read the schema content
        with open(DEFAULT_SCHEMA_PATH, 'r') as f:
            schema = f.read()
            
        # Make the API call to OpenAI
        yaml_content = self._call_openai_api(text, schema)
        
        return yaml_content
    
    def _call_openai_api(self, text: str, schema: str) -> str:
        """
        Call the OpenAI API with the text and schema.
        
        Args:
            text: The text content to convert to a mind map
            schema: The JSON schema content
            
        Returns:
            The generated YAML content
        """
        try:
            # Build system prompt and user prompt
            system_prompt = "You are an expert at creating structured mind maps in YAML format. Your task is to organize the provided text into a hierarchical structure that follows the schema exactly. Every node must include both a title and a descriptive note providing context or details for that node. Only output valid YAML without any explanations, markdown code blocks, or extra text."
            
            user_prompt = f"""I'd like you to summarise a document as a yaml file following a schema.

Please respond with ONLY the YAML content that follows the schema, without any additional text or explanations.
The YAML should have a root node with an appropriate title and organized children nodes that capture
the key points and structure of the text. Aim to have one node per 20 lines of input text.

IMPORTANT: Every node (including the root and ALL child nodes) should include both a title AND a note. 
The note should provide additional context, explanation, or details about that specific node.

Here is the schema to follow:

{schema}

Here is the document to summarize:

{text}"""

            # Call the OpenAI API using the new client interface
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                max_tokens=16000,  # Maximum allowed for this model
                temperature=0.2,  # Low temperature for more deterministic output
            )
            
            # Extract the response content
            content = response.choices[0].message.content
            
            # Use the utility function to extract YAML from markdown
            content = extract_yaml_from_markdown(content)
                
            return content
            
        except Exception as e:
            raise RuntimeError(f"Error calling OpenAI API: {str(e)}") from e