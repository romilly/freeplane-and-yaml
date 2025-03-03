#!/usr/bin/env python3
"""
Convert PDF files to mind maps using PyMuPDF4LLM and AI.
"""

import os
import sys
import argparse
import tempfile
import pymupdf4llm
from dotenv import load_dotenv

from freeplane_and_yaml.convert_pdf_to_mindmap import convert_pdf_to_mindmap
from .text_to_mindmap import TextToMindMap
from .openai_adapter import OpenAIAdapter

# Load environment variables
load_dotenv()


def main():
    """Main entry point for the pdf2mindmap command-line tool."""
    parser = argparse.ArgumentParser(
        description="Convert a PDF file to a mind map using PyMuPDF4LLM and OpenAI"
    )
    parser.add_argument(
        "input_file", 
        help="Path to the input PDF file"
    )
    parser.add_argument(
        "output_dir", 
        help="Directory to save the output files"
    )
    parser.add_argument(
        "--model", 
        help="OpenAI model to use (defaults to gpt-4o-mini)"
    )
    parser.add_argument(
        "--save-text",
        action="store_true",
        help="Save the extracted text to a file"
    )
    
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.isfile(args.input_file):
        print(f"Error: Input PDF file '{args.input_file}' does not exist", file=sys.stderr)
        sys.exit(1)
        
    # Make sure it's a PDF file
    if not args.input_file.lower().endswith('.pdf'):
        print(f"Error: Input file must be a PDF file: {args.input_file}", file=sys.stderr)
        sys.exit(1)
    
    # Validate output directory
    if not os.path.isdir(args.output_dir):
        try:
            os.makedirs(args.output_dir, exist_ok=True)
            print(f"Created output directory: {args.output_dir}")
        except Exception as e:
            print(f"Error: Could not create output directory '{args.output_dir}': {e}", file=sys.stderr)
            sys.exit(1)
    input_file = args.input_file
    output_dir = args.output_dir
    save_text = args.save_text
    # Generate output file paths
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    yaml_output = os.path.join(output_dir, f"{base_name}.yaml")
    mm_output = os.path.join(output_dir, f"{base_name}.mm")
    text_output = os.path.join(output_dir, f"{base_name}.txt") if save_text else None
    model = args.model
    
    try:
        convert_pdf_to_mindmap(base_name, input_file, mm_output, model, text_output, yaml_output)

    except Exception as e:
        print(f"Error during conversion: {e}", file=sys.stderr)
        sys.exit(1)




if __name__ == "__main__":
    main()