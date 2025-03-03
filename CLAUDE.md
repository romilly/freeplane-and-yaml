# CLAUDE.md for freeplane-and-yaml

## Build/Test Commands
- Run all tests: `python -m pytest`
- Run a single test: `python -m pytest tests/test_convert.py::test_convert_yaml_file`
- Install package in dev mode: `pip install -e .`
- Run conversion: `convert data/filename.yaml output_directory`

## Code Style Guidelines
- Python 3.9+ compatible code
- Function and variable names: snake_case
- Class names: PascalCase
- Use docstrings for functions and classes
- Use `yaml.safe_load()` for YAML parsing
- Error handling with try/except and appropriate exit codes
- Type hints are not mandatory but recommended
- Import order: standard library, third-party, local modules
- Follow PEP 8 formatting guidelines

## Project Structure
- Logic in `src/freeplane_and_yaml/convert.py`
- CLI interface in `src/freeplane_and_yaml/cli.py`
- Tests in `tests/` matching source structure
- YAML input files in `data/` or `tests/data/`
- Output files in `output/` or `tests/data/generated/`