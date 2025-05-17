import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "lux"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]

created_files = 0
existing_files = 0

for filepath_str in list_of_files:
    filepath = Path(filepath_str)
    filedir = filepath.parent
    filename = filepath.name

    try:
        # Create directories if they don't exist
        if not filedir.exists():
            filedir.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {filedir}")

        # Create file if it doesn't exist or is empty
        if not filepath.exists() or os.path.getsize(filepath) == 0:
            with open(filepath, "w") as f:
                pass
            logging.info(f"Created empty file: {filepath}")
            created_files += 1
        else:
            logging.info(f"{filename} already exists")
            existing_files += 1

    except Exception as e:
        logging.error(f"Error creating {filepath}: {e}")

# Summary
print(f"\nSummary: {created_files} files created, {existing_files} files already existed.")
