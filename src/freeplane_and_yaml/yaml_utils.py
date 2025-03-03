"""
Utility functions for YAML handling.
"""

def extract_yaml_from_markdown(content):
    """
    Extract YAML content from markdown-formatted text.
    
    Args:
        content: The markdown text containing YAML code blocks
        
    Returns:
        The extracted YAML content
    """
    # Remove any initial text before the YAML content
    if "```yaml" in content:
        content = content.split("```yaml", 1)[1]
        if "```" in content:
            content = content.split("```", 1)[0]
    elif "```" in content:
        content = content.split("```", 1)[1]
        if "```" in content:
            content = content.split("```", 1)[0]
            
    # Clean up and return
    return content.strip()