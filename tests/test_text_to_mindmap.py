import os
import pytest
import yaml
from freeplane_and_yaml.text_to_mindmap import TextToMindMap
from freeplane_and_yaml.mock_adapter import MockLLMAdapter
from freeplane_and_yaml.llm_adapter import DEFAULT_SCHEMA_PATH

# Paths
TESTS_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(TESTS_DIR, "data")
INPUT_DIR = os.path.join(DATA_DIR, "input")
EXPECTED_DIR = os.path.join(DATA_DIR, "expected")
GENERATED_DIR = os.path.join(DATA_DIR, "generated")

@pytest.fixture(scope="function")
def prepare_generated_directory():
    """Clean up files inside the generated directory before the test."""
    if not os.path.exists(GENERATED_DIR):
        os.makedirs(GENERATED_DIR)
    else:
        for file in os.listdir(GENERATED_DIR):
            file_path = os.path.join(GENERATED_DIR, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
    yield


def test_text_to_mindmap_with_mock_adapter(prepare_generated_directory):
    """Test the TextToMindMap class with a mock adapter."""
    # Test file paths
    input_file = os.path.join(INPUT_DIR, "sample.txt")
    expected_yaml_file = os.path.join(EXPECTED_DIR, "sample.yaml")
    output_yaml_file = os.path.join(GENERATED_DIR, "sample.yaml")
    output_mm_file = os.path.join(GENERATED_DIR, "sample.mm")
    
    # Read the expected YAML
    with open(expected_yaml_file, 'r', encoding='utf-8') as f:
        expected_yaml = f.read()
    
    # Create a mock adapter with the expected YAML as its response
    mock_adapter = MockLLMAdapter(expected_yaml)
    
    # Create the TextToMindMap service with the mock adapter
    service = TextToMindMap(mock_adapter)
    
    # Convert the sample text file
    yaml_content = service.convert_text_file(input_file, output_yaml_file, output_mm_file)
    
    # Verify that the adapter was called with the correct arguments
    with open(input_file, 'r', encoding='utf-8') as f:
        expected_text = f.read()
    
    assert mock_adapter.last_text == expected_text
    
    # Verify that the output YAML file was created with the correct content
    assert os.path.exists(output_yaml_file)
    with open(output_yaml_file, 'r', encoding='utf-8') as f:
        actual_yaml = f.read()
    assert actual_yaml == expected_yaml
    
    # Verify that the output MM file was created
    assert os.path.exists(output_mm_file)
    
    # Verify that the YAML is valid and follows our schema structure
    yaml_data = yaml.safe_load(yaml_content)
    assert 'root' in yaml_data
    assert 'title' in yaml_data['root']
    assert 'children' in yaml_data['root']


def test_text_to_mindmap_initialization():
    """Test that the TextToMindMap class is properly initialized."""
    mock_adapter = MockLLMAdapter()
    service = TextToMindMap(mock_adapter)
    assert service.llm_adapter == mock_adapter
    
    # Verify the schema path exists
    assert os.path.exists(DEFAULT_SCHEMA_PATH)
    assert os.path.basename(DEFAULT_SCHEMA_PATH) == "mindmap-schema.json"