import os
import xml.etree.ElementTree as ET
import pytest
from convert_yaml_to_freeplane import convert_yaml_file

# Define paths
TESTS_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(TESTS_DIR, "data")
GENERATED_DIR = os.path.join(DATA_DIR, "generated")
EXPECTED_DIR = os.path.join(DATA_DIR, "expected")


@pytest.fixture(scope="function")
def prepare_generated_directory():
    """Fixture to clean up files inside the generated directory before the test."""
    # Ensure the 'generated' directory exists
    if not os.path.exists(GENERATED_DIR):
        os.makedirs(GENERATED_DIR)
    else:
        # Remove all files in the 'generated' directory
        for file in os.listdir(GENERATED_DIR):
            file_path = os.path.join(GENERATED_DIR, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
    yield


def extract_node_structure(node):
    """
    Recursively extract the structure of the node, ignoring specific attributes
    like ID, timestamps, and formatting.

    Args:
        node (xml.etree.ElementTree.Element): The XML node to process.

    Returns:
        dict: A dictionary representing the structure of the XML node with titles and children.
    """
    # Extract the node's title
    title_element = node.find("richcontent[@TYPE='NODE']")
    if title_element is not None:
        title = "".join(title_element.itertext()).strip()  # Convert rich text to plain text
    else:
        title = node.get("TEXT", "").strip()  # Fallback to TEXT attribute if no rich content

    # Recursively process child nodes
    children = [extract_node_structure(child) for child in node.findall("node")]

    # Return the node's structure as a dictionary
    return {"title": title, "children": children}


def compare_node_structures(struct1, struct2):
    """
    Recursively compare two node structures.

    Args:
        struct1 (dict): The first node structure.
        struct2 (dict): The second node structure.

    Returns:
        bool: True if structures are identical, False otherwise.
    """
    if struct1["title"] != struct2["title"]:
        return False

    if len(struct1["children"]) != len(struct2["children"]):
        return False

    # Recursively compare children
    for child1, child2 in zip(struct1["children"], struct2["children"]):
        if not compare_node_structures(child1, child2):
            return False

    return True


def test_convert_yaml_file(prepare_generated_directory):
    # Input and output file paths
    input_file = os.path.join(DATA_DIR, "brain.yaml")
    output_file = os.path.join(GENERATED_DIR, "brain.mm")
    expected_file = os.path.join(EXPECTED_DIR, "brain.mm")

    # Perform the conversion using the correct method
    convert_yaml_file(input_file, output_file)

    # Check that the generated file exists
    assert os.path.exists(output_file), "Output file was not generated."

    # Parse the generated and expected .mm files
    generated_tree = ET.parse(output_file)
    expected_tree = ET.parse(expected_file)

    # Extract the root node structures
    generated_structure = extract_node_structure(generated_tree.getroot())
    expected_structure = extract_node_structure(expected_tree.getroot())

    # Compare structures
    assert compare_node_structures(generated_structure, expected_structure), (
        "The generated file's structure does not match the expected structure."
    )
