# YAML to Freeplane Converter

A Python tool that converts YAML files into Freeplane mind maps. This allows you to generate mind maps programmatically from structured YAML data.

The YAML file can be created using [Claude AI](https://claude.ai/chat/). A suitable prompt is given [below](#converting-documents-to-mind-maps-using-claude-ai).

You can read about how it got written using AI on [medium](https://medium.com/@romillyc/build-your-own-mind-map-tools-with-ai-b193564f2464?sk=b353aa7d16d6412e4aae8f3eab0ec554).
That's a friend link so you can read it even if you're not a subscriber.

## Installation

This project requires Python and should be run in a virtual environment:

```bash
# Create and activate virtual environment in the direcoty of your choice
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install freeplane-and-yaml
```


## Usage

The code should be run from the `src` directory after activating the virtual environment. Your YAML file should follow the schema defined in `schema/mindmap-schema.json`. Here's an example structure:

```yaml
root:
  title: "Your Main Topic"
  note: "Optional note for the main topic"
  children:
    subtopic1:
      title: "Subtopic 1"
      note: "Optional note for subtopic 1"
      children:
        # ... more nested topics
    subtopic2:
      title: "Subtopic 2"
      # ... and so on
```

### YAML Schema Requirements

The YAML must conform to these rules:
- Must have a root node with a title and at least one child
- Each node requires a title
- Notes are optional
- Child node keys must be alphanumeric (including underscores)
- No additional properties are allowed beyond title, note, and children

For full schema details, see `schema/mindmap-schema.json`.

### Converting Documents to Mind Maps using Claude AI

You can use Claude Sonnet to automatically convert documents (PDFs, articles, specifications, etc.) into the required YAML format. Here's the workflow:

1. Share your document and the schema (from `schema/mindmap-schema.json`)with Claude Sonnet.
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

### Converting YAML to Mind Map

To convert a YAML file to a Freeplane mind map:

```bash

# Convert YAML and store mind map in temp
convert data/marr.yaml temp

```

The generated `.mm` file can be opened in Freeplane. When you first open the file, Freeplane will show this warning dialog because the file wasn't created by Freeplane itself:

![Freeplane Warning Dialog](images/warning-dialog.png)

This is normal and expected — click OK to load the mind map.

Here's an example of how the output looks:

![Example Mind Map](images/Screenshot%20at%202025-02-12%2010-43-23.png)

## Features

- Converts YAML structured data to Freeplane mind map format
- Supports hierarchical node structure
- Includes node titles and optional notes
- Automatically alternates between right and left positions for top-level nodes
- Generates unique IDs for each node
- Validates input against JSON schema

## License

_Apologies to readers from the USA. This README uses UK spelling._

This project is licensed under the MIT Licence — see the [LICENCE](LICENSE) file for details.
