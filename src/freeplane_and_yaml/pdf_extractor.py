"""
PDF text extraction using PyMuPDF4LLM.
"""

import os
import pymupdf4llm


class PDFExtractor:
    """
    A class to extract text content from PDF files.
    """
    
    def __init__(self, strategy: str = "markdown"):
        """
        Initialize the PDF extractor.
        
        Args:
            strategy: The extraction strategy (only 'markdown' is currently supported)
        """
        self.strategy = strategy
        
        # For now, we only support the markdown strategy using pymupdf4llm
        if strategy != "markdown":
            print(f"Warning: Strategy '{strategy}' is not supported. Using 'markdown' instead.")
            self.strategy = "markdown"
            
    def extract_text(self, pdf_path: str) -> str:
        """
        Extract text from a PDF file.
        
        Args:
            pdf_path: Path to the PDF file
            
        Returns:
            Extracted text from the PDF
        """
        # Ensure the file exists
        if not os.path.isfile(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
            
        # Extract text using PyMuPDF4LLM's to_markdown function
        md_text = pymupdf4llm.to_markdown(pdf_path)
        return md_text