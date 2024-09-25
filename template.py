import os
from pathlib import Path
import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Project name
project_name = "textSummarizer"

# List of files to be created
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",  # Fixed typo in the filename
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipelining/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "configs/config.yaml",
    "params.yaml",  # Fixed filename (was missing a dot before yaml)
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]

# Create each file and necessary directories
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Directory created: {filedir}")

    # Create the file if it doesn't exist
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass  # Just create an empty file
        logging.info(f"File created: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
