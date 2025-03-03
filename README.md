# PDF to Freeplane Mind Map Converter

A Python tool that converts PDF documents into Freeplane mind maps using OpenAI. This allows you to automatically generate structured mind maps from PDF documents.

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

You'll need to set up your OpenAI API key in a `.env` file or as an environment variable:

```bash
# Create a .env file in your project directory
echo "OPENAI_API_KEY=your_api_key_here" > .env
```


## Usage

### Converting PDF Documents to Mind Maps

To convert a PDF document to a Freeplane mind map:

```bash
# Convert a PDF file to a mind map
pdf2mindmap path/to/document.pdf output_directory

# Use a specific OpenAI model (default is gpt-4o-mini)
pdf2mindmap path/to/document.pdf output_directory --model gpt-4-turbo

# Also save the extracted text
pdf2mindmap path/to/document.pdf output_directory --save-text
```

The tool performs these steps:
1. Extracts text from the PDF using PyMuPDF4LLM (preserving structure as markdown)
2. Processes the text with OpenAI to generate a structured mind map in YAML format
3. Converts the YAML to a Freeplane mind map (.mm file)
4. Saves all files in the output directory

This is useful for:
- Summarizing academic papers
- Converting product requirements documents (PRDs)
- Creating structured summaries of technical documentation
- Organizing research notes or book content


The generated `.mm` file can be opened in Freeplane. When you first open the file, Freeplane will show this warning dialog because the file wasn't created by Freeplane itself:

![Freeplane Warning Dialog](images/warning-dialog.png)

This is normal and expected — click OK to load the mind map.

Here's an example of how the output looks:

![Example Mind Map](images/Screenshot%20at%202025-02-12%2010-43-23.png)

## Features

- Converts PDF documents to Freeplane mind maps using OpenAI
- Uses PyMuPDF4LLM for high-quality text extraction from PDFs
- Creates hierarchical mind maps with node titles and notes
- Automatically alternates between right and left positions for top-level nodes
- Generates unique IDs for each node
- Produces clean, well-structured YAML as an intermediate format
- Supports different OpenAI models (default is gpt-4o-mini)

## License

_Apologies to readers from the USA. This README uses UK spelling._

This project is licensed under the MIT Licence — see the [LICENCE](LICENSE) file for details.
