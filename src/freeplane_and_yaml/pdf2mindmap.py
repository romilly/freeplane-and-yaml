#!/usr/bin/env python3
"""
Convert PDF files to mind maps using PyMuPDF4LLM and Claude AI.
"""

import os
import sys
import argparse
import tempfile
from dotenv import load_dotenv
from .text_to_mindmap import TextToMindMap
from .claude_adapter import ClaudeAdapter
from .mock_adapter import MockLLMAdapter
from .pdf_extractor import PDFExtractor

# Load environment variables
load_dotenv()


def main():
    """Main entry point for the pdf2mindmap command-line tool."""
    parser = argparse.ArgumentParser(
        description="Convert a PDF file to a mind map using PyMuPDF4LLM and Claude AI"
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
        "--strategy",
        default="markdown",
        help="Text extraction strategy (only markdown is currently supported)"
    )
    parser.add_argument(
        "--mock", 
        action="store_true", 
        help="Use mock adapter instead of Claude API (for testing)"
    )
    parser.add_argument(
        "--model", 
        help="Claude model to use (defaults to claude-3-sonnet-20240229)"
    )
    parser.add_argument(
        "--api-key", 
        help="Anthropic API key (defaults to ANTHROPIC_API_KEY environment variable)"
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
    
    # Generate output file paths
    base_name = os.path.splitext(os.path.basename(args.input_file))[0]
    yaml_output = os.path.join(args.output_dir, f"{base_name}.yaml")
    mm_output = os.path.join(args.output_dir, f"{base_name}.mm")
    text_output = os.path.join(args.output_dir, f"{base_name}.txt") if args.save_text else None
    
    try:
        # Step 1: Extract text from the PDF
        print(f"Extracting text from {args.input_file} using strategy: {args.strategy}...")
        pdf_extractor = PDFExtractor(strategy=args.strategy)
        extracted_text = pdf_extractor.extract_text(args.input_file)
        
        # Save the extracted text if requested
        if text_output:
            with open(text_output, 'w', encoding='utf-8') as f:
                f.write(extracted_text)
            print(f"Saved extracted text to: {text_output}")
            
        # If the text is empty, report an error
        if not extracted_text.strip():
            print("Error: No text could be extracted from the PDF", file=sys.stderr)
            sys.exit(1)
        
        # Step 2: Create the appropriate adapter
        if args.mock:
            print("Using mock adapter (no real API calls will be made)")
            adapter = MockLLMAdapter()
        else:
            # Check if API key is available
            api_key = args.api_key or os.environ.get("ANTHROPIC_API_KEY")
            if not api_key or api_key == "your_api_key_here":
                print("Error: No Anthropic API key provided. Please set ANTHROPIC_API_KEY in .env file or use --api-key", file=sys.stderr)
                sys.exit(1)
                
            # Create the adapter
            adapter = ClaudeAdapter(api_key=api_key, model=args.model)
        
        # Step 3: Create a temporary text file for the extracted content
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as temp_file:
            temp_file.write(extracted_text)
            temp_file_path = temp_file.name
        
        try:
            # Step 4: Process the text with the text-to-mindmap service
            print("Converting extracted text to mind map format...")
            service = TextToMindMap(adapter)
            
            # First try to get the YAML directly to inspect it
            with open(temp_file_path, 'r', encoding='utf-8') as f:
                text_content = f.read()
            
            # Limit the text size to avoid timeouts
            MAX_CHARS = 40000  # Large documents may cause timeouts
            if len(text_content) > MAX_CHARS:
                print(f"Document is large ({len(text_content)} chars). Truncating to {MAX_CHARS} chars to avoid timeouts.")
                text_content = text_content[:MAX_CHARS] + "\n\n[Content truncated due to length...]"
            
            try:
                print(f"Sending document for processing...")
                yaml_content = adapter.generate_mind_map_yaml(text_content)
                
                # Save raw output for debugging
                debug_yaml_path = os.path.join(args.output_dir, f"{base_name}.raw.yaml")
                with open(debug_yaml_path, 'w', encoding='utf-8') as f:
                    f.write(yaml_content)
                print(f"Saved raw YAML for debugging to: {debug_yaml_path}")
                
                # Now continue with the regular process
                service.convert_text_file(temp_file_path, yaml_output, mm_output)
            except Exception as e:
                print(f"YAML conversion error: {e}")
                print("Saving debug information and continuing...")
                # Continue with original code path anyway
                service.convert_text_file(temp_file_path, yaml_output, mm_output)
            
            print("\nConversion successful!")
            print(f"YAML output: {yaml_output}")
            print(f"Mind map: {mm_output}")
            if text_output:
                print(f"Text output: {text_output}")
                
        finally:
            # Clean up the temporary file
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)
                
    except Exception as e:
        print(f"Error during conversion: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()