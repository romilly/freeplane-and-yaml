"""
End-to-end test for PDF to Mind Map conversion.

This module tests the complete PDF to Mind Map conversion pipeline, which includes:
1. PDF text extraction using pymupdf4llm
2. Text to YAML conversion using OpenAI (real API call)
3. YAML to Freeplane mind map conversion

The test uses a sample PDF file and validates that the entire pipeline 
produces the expected output files with actual API calls.
"""

import os
import tempfile
import warnings
import pytest
import xml.etree.ElementTree as ET
import yaml
from freeplane_and_yaml.convert_pdf_to_mindmap import convert_pdf_to_mindmap

# Suppress SWIG-related deprecation warnings from pymupdf4llm
warnings.filterwarnings("ignore", message="builtin type SwigPyPacked has no __module__ attribute")
warnings.filterwarnings("ignore", message="builtin type SwigPyObject has no __module__ attribute")
warnings.filterwarnings("ignore", message="builtin type swigvarlink has no __module__ attribute")


def test_convert_pdf_to_mindmap():
    """Test the end-to-end PDF to Mind Map conversion process with the real OpenAI API."""
    # Skip this test if API key environment variable is not set 
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        pytest.skip("OPENAI_API_KEY environment variable not set")
    
    # Define paths
    test_dir = os.path.dirname(__file__)
    input_data_dir = os.path.join(test_dir, 'data', 'input')
    sample_pdf_path = os.path.join(input_data_dir, "sample.pdf")
    
    # Create temporary directory for output files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Define output paths
        base_name = "test_output"
        yaml_output = os.path.join(temp_dir, f"{base_name}.yaml")
        mm_output = os.path.join(temp_dir, f"{base_name}.mm")
        text_output = os.path.join(temp_dir, f"{base_name}.txt")
        
        print(f"\nRunning end-to-end test with real OpenAI API call")
        print(f"Input: {sample_pdf_path}")
        print(f"Output directory: {temp_dir}")
        
        # Call the conversion function with real API
        convert_pdf_to_mindmap(
            base_name=base_name,
            input_file=sample_pdf_path,
            mm_output=mm_output,
            model="gpt-4o-mini",  # Use a smaller model to reduce costs
            text_output=text_output,
            yaml_output=yaml_output
        )
        
        # Verify that all expected output files were created
        assert os.path.exists(yaml_output), "YAML output file was not created"
        assert os.path.exists(mm_output), "Mind map output file was not created"
        assert os.path.exists(text_output), "Text output file was not created"
        
        # Verify the content of the files
        
        # 1. Check that the text file contains content from the PDF
        with open(text_output, 'r', encoding='utf-8') as f:
            extracted_text = f.read()
            assert "Hexagonal Architecture" in extracted_text, "PDF text extraction failed"
        
        # 2. Check that the YAML file contains the expected structure from the real API
        with open(yaml_output, 'r', encoding='utf-8') as f:
            yaml_content = yaml.safe_load(f.read())
            assert 'root' in yaml_content, "YAML file does not have the expected structure"
            assert 'title' in yaml_content['root'], "YAML root node has no title"
            assert 'children' in yaml_content['root'], "YAML root node has no children"
            
            # Print some info about the generated content
            print(f"\nGenerated YAML structure:")
            print(f"Root title: {yaml_content['root']['title']}")
            print(f"Number of top-level sections: {len(yaml_content['root']['children'])}")
        
        # 3. Check that the mind map file is valid XML and has the expected structure
        tree = ET.parse(mm_output)
        root = tree.getroot()
        
        # Check that it's a valid Freeplane map
        assert root.tag == "map", "Root element is not a map"
        assert root.get("version"), "Map has no version attribute"
        
        # Check that the map has nodes
        nodes = root.findall(".//node")
        assert len(nodes) > 0, "Mind map has no nodes"
        print(f"Mind map contains {len(nodes)} nodes")
        
        # Check for rich content (notes)
        rich_contents = root.findall(".//richcontent")
        assert len(rich_contents) > 0, "Mind map has no rich content"
        print(f"Mind map contains {len(rich_contents)} rich content elements")


if __name__ == "__main__":
    pytest.main(["-v", __file__])