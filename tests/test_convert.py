import os
import sys
import filecmp
import pytest

# Include the src directory in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Import the `convert_yaml_to_freeplane` function
from convert_yaml_to_freeplane import convert_yaml_file
# Define paths
TESTS_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(TESTS_DIR, "data")
GENERATED_DIR = os.path.join(DATA_DIR, "generated")
EXPECTED_DIR = os.path.join(DATA_DIR, "expected")


@pytest.fixture
def cleanup_generated():
    """Fixture to clean up files inside the generated directory after the test."""
    if not os.path.exists(GENERATED_DIR):
        os.makedirs(GENERATED_DIR)
    else:
        # Clear files in the 'generated' directory
        for file in os.listdir(GENERATED_DIR):
            file_path = os.path.join(GENERATED_DIR, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
    yield
    # Cleanup after test
    for file in os.listdir(GENERATED_DIR):
        file_path = os.path.join(GENERATED_DIR, file)
        if os.path.isfile(file_path):
            os.unlink(file_path)


def test_convert_yaml_file(cleanup_generated):
    # Input and output file paths
    input_file = os.path.join(DATA_DIR, "brain.yaml")
    output_file = os.path.join(GENERATED_DIR, "brain.mm")
    expected_file = os.path.join(EXPECTED_DIR, "brain.mm")

    # Perform the conversion
    convert_yaml_file(input_file, output_file)

    # Check that the generated file exists
    assert os.path.exists(output_file), "Output file was not generated."

    # Compare the generated file with the expected file
    assert filecmp.cmp(output_file, expected_file, shallow=False), (
        "The generated file does not match the expected output."
    )