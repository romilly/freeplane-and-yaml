# YAML to Freeplane Converter

A Python tool that converts YAML files into Freeplane mind maps. This allows you to generate mind maps programmatically from structured YAML data.

The YAML file can be created using [Claude AI](https://claude.ai/chat/). 
A suitable prompt is given [below](https://github.com/romilly/freeplane-and-yaml?tab=readme-ov-file#converting-documents-to-yaml-using-claude-ai).

You can read about how it got written using AI on [medium](https://medium.com/@romillyc/build-your-own-mind-map-tools-with-ai-b193564f2464?sk=b353aa7d16d6412e4aae8f3eab0ec554).
That's a _friend link_ so you can read it even if you're not a subscriber.

## Installation

This project requires Python and should be run in a virtual environment:

```bash
# Create and activate virtual environment in the directory of your choice
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install freeplane-and-yaml
```

If you want to use the text-to-mindmap feature with Claude AI, additional dependencies will be installed automatically. You'll need to set up your Anthropic API key in a `.env` file or as an environment variable.

```bash
# Create a .env file in your project directory
echo "ANTHROPIC_API_KEY=your_api_key_here" > .env
```


## Usage

Your YAML file should follow this [schema](https://raw.githubusercontent.com/romilly/freeplane-and-yaml/refs/heads/main/src/schema/mindmap-schema.json). It includes an example.

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Mind Map Schema",
  "description": "Schema for Freeplane-compatible mind map YAML format",
  
  "definitions": {
    "node": {
      "type": "object",
      "required": ["title"],
      "properties": {
        "title": {
          "type": "string",
          "description": "The display text for the node"
        },
        "note": {
          "type": "string",
          "description": "Rich text note attached to the node"
        },
        "children": {
          "type": "object",
          "description": "Child nodes of this node",
          "patternProperties": {
            "^[a-zA-Z0-9_]+$": {
              "$ref": "#/definitions/node"
            }
          },
          "additionalProperties": false
        }
      },
      "additionalProperties": false
    }
  },

  "type": "object",
  "required": ["root"],
  "properties": {
    "root": {
      "allOf": [
        { "$ref": "#/definitions/node" },
        { 
          "required": ["children"],
          "description": "The root node must have at least one child"
        }
      ]
    }
  },
  "additionalProperties": false,

  "examples": [
    {
      "root": {
        "title": "Example Mind Map",
        "note": "This is the root node",
        "children": {
          "topic1": {
            "title": "First Topic",
            "note": "Note for first topic",
            "children": {
              "subtopic1": {
                "title": "Subtopic 1",
                "note": "Note for subtopic"
              }
            }
          },
          "topic2": {
            "title": "Second Topic",
            "note": "Note for second topic"
          }
        }
      }
    }
  ]
}

```

### Converting YAML to Mind Map

To convert a YAML file to a Freeplane mind map:

```bash
# Convert YAML and store mind map in temp
convert data/marr.yaml temp
```

### Converting Text Directly to Mind Map

You can convert text files directly to mind maps using Claude AI:

1. First, set up your API key in a `.env` file at the project root:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

2. Then use the `text2mindmap` command:
   ```bash
   # Convert a text file to a mind map
   text2mindmap path/to/document.txt output_directory
   
   # Use a specific Claude model
   text2mindmap path/to/document.txt output_directory --model claude-3-opus-20240229
   
   # Use mock adapter (no API calls, for testing)
   text2mindmap path/to/document.txt output_directory --mock
   ```

This will:
1. Process the text document with Claude AI
2. Generate a YAML mind map representation
3. Convert the YAML to a Freeplane mind map (.mm file)
4. Save both files in the output directory

### Converting PDF Documents to Mind Map

You can also convert PDF documents directly to mind maps:

1. Ensure your API key is set up in a `.env` file:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   ```

2. Use the `pdf2mindmap` command:
   ```bash
   # Convert a PDF file to a mind map
   pdf2mindmap path/to/document.pdf output_directory
   
   # Choose a text extraction strategy
   pdf2mindmap path/to/document.pdf output_directory --strategy pages
   
   # Also save the extracted text
   pdf2mindmap path/to/document.pdf output_directory --save-text
   
   # Use mock adapter (no API calls, for testing)
   pdf2mindmap path/to/document.pdf output_directory --mock
   ```

PyMuPDF4LLM is used to extract text from PDF files, converting the PDF content to markdown format for optimal structure preservation.

This functionality uses PyMuPDF4LLM for text extraction and Claude AI for mind map generation.

### YAML Schema requirements explained

As the schema specifies, The YAML must conform to these rules:
- Must have a root node with a title and at least one child
- Each node requires a title
- Notes are optional
- Child node keys must be alphanumeric (including underscores)
- No additional properties are allowed beyond title, note, and children

For full schema details, see above.

### Converting Documents to YAML using Claude AI

You can use Claude Sonnet to automatically convert documents (PDFs, articles, specifications, etc.) into the required YAML format. Here's the workflow:

1. Share your document and the schema (above) with Claude Sonnet.
2. Use this prompt:
   ```
   I've uploaded a document and a schema file.  I'd like you to summarise the document as a yaml file following the schema that I uploaded.
   ```
3. Claude will generate a YAML file that follows the schema
4. Save Claude's output as a .yaml file
5. Convert it to a mind map using this tool

This workflow is useful for:
- Summarizing academic papers
- Converting product requirements documents (PRDs)
- Creating structured summaries of technical documentation
- Organizing research notes


The generated `.mm` file can be opened in Freeplane. When you first open the file, Freeplane will show this warning dialog because the file wasn't created by Freeplane itself:

![Freeplane Warning Dialog](images/warning-dialog.png)

This is normal and expected — click OK to load the mind map.

Here's an example of how the output looks:

![Example Mind Map](images/Screenshot%20at%202025-02-12%2010-43-23.png)

## Features

- Converts YAML structured data to Freeplane mind map format
- Directly converts text files to mind maps using Claude AI
- Converts PDF documents to mind maps using PyMuPDF4LLM and Claude AI
- Supports hierarchical node structure
- Includes node titles and optional notes
- Automatically alternates between right and left positions for top-level nodes
- Generates unique IDs for each node
- Validates input against JSON schema
- Hexagonal architecture design for easy extension with different LLM providers
- Multiple text extraction strategies for PDF documents

## License

_Apologies to readers from the USA. This README uses UK spelling._

This project is licensed under the MIT Licence — see the [LICENCE](LICENSE) file for details.
