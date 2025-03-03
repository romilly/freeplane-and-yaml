#!/usr/bin/env python3
"""
Convert text files to mind maps using Claude AI.
"""

import os
import sys
import argparse
from dotenv import load_dotenv
from .text_to_mindmap import TextToMindMap
from .claude_adapter import ClaudeAdapter
from .mock_adapter import MockLLMAdapter

# Load environment variables
load_dotenv()


def main():
    """Main entry point for the text2mindmap command-line tool."""
    parser = argparse.ArgumentParser(
        description="Convert a text file to a mind map using Claude AI"
    )
    parser.add_argument(
        "input_file", 
        help="Path to the input text file"
    )
    parser.add_argument(
        "output_dir", 
        help="Directory to save the output files"
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
    
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.isfile(args.input_file):
        print(f"Error: Input file '{args.input_file}' does not exist", file=sys.stderr)
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
    
    try:
        # Create the appropriate adapter
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
        
        # Create the service
        service = TextToMindMap(adapter)
        
        # Process the file
        print(f"Converting {args.input_file} to mind map format...")
        service.convert_text_file(args.input_file, yaml_output, mm_output)
        
        print("\nConversion successful!")
        print(f"YAML output: {yaml_output}")
        print(f"Mind map: {mm_output}")
        
    except Exception as e:
        print(f"Error during conversion: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()