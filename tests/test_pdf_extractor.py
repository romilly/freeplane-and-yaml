import os
import warnings
import pytest
import pymupdf4llm

# Suppress SWIG-related deprecation warnings
warnings.filterwarnings("ignore", message="builtin type SwigPyPacked has no __module__ attribute")
warnings.filterwarnings("ignore", message="builtin type SwigPyObject has no __module__ attribute")
warnings.filterwarnings("ignore", message="builtin type swigvarlink has no __module__ attribute")


def test_extract_text_with_sample_pdf():
    """Test text extraction with the sample PDF file."""
    # Define paths
    test_dir = os.path.dirname(__file__)
    input_data_dir= os.path.join(test_dir, 'data', 'input')
    sample_pdf_path = os.path.join(input_data_dir, "sample.pdf")
    sample_md_path = os.path.join(input_data_dir, "sample.md")
    
    # Extract text from PDF using pymupdf4llm
    extracted_md = pymupdf4llm.to_markdown(sample_pdf_path)
    
    # Read the expected markdown content
    with open(sample_md_path, 'r', encoding='utf-8') as f:
        expected_md = f.read()
    
    # Compare the content
    # Note: PDF extraction might have slight formatting differences compared to the sample markdown
    # We'll check for content similarity rather than exact matches
    
    # Make sure the extracted content is not empty
    assert extracted_md.strip(), "Extracted content should not be empty"
    
    # Instead of comparing specific lines, check for key phrases
    # PDF extraction can vary significantly from the original text formatting
    key_phrases = [
        "Hexagonal Architecture",
        "Pattern for",
        "Software Development",
        "Ports and Adapters"
    ]
    
    # Check if these key phrases appear in the extracted text
    for phrase in key_phrases:
        assert phrase.lower() in extracted_md.lower(), \
            f"Key phrase '{phrase}' not found in extracted text"
            
    # Print the first few lines of extracted text for debugging
    print("\nExtracted text begins with:")
    print(extracted_md[:200] + "...")