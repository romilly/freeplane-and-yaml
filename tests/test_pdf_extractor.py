import os
import pytest
import tempfile
from freeplane_and_yaml.pdf_extractor import PDFExtractor

@pytest.fixture
def sample_pdf_path():
    """Get the path to a sample PDF file if one exists in private directory."""
    # Check if there's a sample PDF in the private directory
    private_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'private')
    
    if os.path.isdir(private_dir):
        pdf_files = [f for f in os.listdir(private_dir) if f.lower().endswith('.pdf')]
        if pdf_files:
            return os.path.join(private_dir, pdf_files[0])
    
    # If no PDF found, mark test as skipped
    pytest.skip("No sample PDF file found in the private directory")


def test_pdf_extractor_initialization():
    """Test that the PDF extractor can be initialized with various options."""
    # Default initialization
    extractor = PDFExtractor()
    assert extractor.strategy == "markdown"
    
    # With specific strategy - note that only markdown is supported
    extractor = PDFExtractor(strategy="text")
    assert extractor.strategy == "markdown"  # Should default to markdown


def test_extract_text_file_not_found():
    """Test that the extractor raises an error for non-existent files."""
    extractor = PDFExtractor()
    with pytest.raises(FileNotFoundError):
        extractor.extract_text("non_existent_file.pdf")


def test_extract_text_with_real_pdf(sample_pdf_path):
    """Test text extraction with a real PDF file."""
    # Skip this test if no sample PDF is available
    if not sample_pdf_path:
        pytest.skip("No sample PDF file found")
        
    # Create extractor
    extractor = PDFExtractor()
    
    # Extract text
    markdown_output = extractor.extract_text(sample_pdf_path)
    
    # Basic validation
    assert markdown_output, "Markdown output should not be empty"
    
    # Check basic markdown formatting
    assert "#" in markdown_output or "*" in markdown_output or "-" in markdown_output, \
        "Markdown output should contain some markdown formatting"