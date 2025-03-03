from setuptools import setup, find_packages

setup(
    name="freeplane-and-yaml",  # Your package name (it must be unique on PyPI)
    version="0.3.0",  # Simplified to focus on PDF-to-mindmap with OpenAI
    description="A tool to convert PDF files to Freeplane mind maps using OpenAI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",  # Use Markdown for PyPI description
    url="https://github.com/romilly/freeplane-and-yaml",  # Replace with your repository URL
    author="Romilly Cocking",
    author_email="romilly.cocking@gmail.com",
    license="MIT",  # Choose your license (e.g., MIT, Apache)
    packages=find_packages(where="src"),  # Look for packages in src/
    package_dir={"": "src"},  # Root of packages is src/
    include_package_data=True,  # Include non-Python files listed in MANIFEST.in
    install_requires=[
        "PyYAML",
        "python-dotenv",
        "openai",
        "pymupdf4llm",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Your license
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9", # Specify minimum Python version
    entry_points={
        "console_scripts": [
            "pdf2mindmap=freeplane_and_yaml.pdf2mindmap:main",
        ],
    },

)