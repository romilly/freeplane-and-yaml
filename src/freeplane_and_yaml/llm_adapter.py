from abc import ABC, abstractmethod
from typing import Dict, Any
import os

# Default schema path - using a path that works both in development and when installed
# First try the package-relative path (for installed package)
DEFAULT_SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'schema', 'mindmap-schema.json')

# If that doesn't exist, try the development path
if not os.path.exists(DEFAULT_SCHEMA_PATH):
    DEFAULT_SCHEMA_PATH = os.path.abspath(
        os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
            "src", "schema", "mindmap-schema.json"
        )
    )


class LLMAdapter(ABC):
    """
    Abstract base class for LLM adapters.
    This follows the hexagonal architecture pattern to isolate the LLM service from our core logic.
    """
    
    @abstractmethod
    def generate_mind_map_yaml(self, text: str) -> str:
        """
        Generate a mind map in YAML format from the provided text,
        following the schema defined in DEFAULT_SCHEMA_PATH.
        
        Args:
            text: The text content to convert to a mind map
            
        Returns:
            A string containing the YAML representation of the mind map
        """
        pass