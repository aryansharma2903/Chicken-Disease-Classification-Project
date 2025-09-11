import os
from pathlib import Path
# to log everything we are doing
import logging

# this is the logging format we will use
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(message)s')
project_name = "cnnClassifier"

# to create folders and fikes
list_of_files = [
    # we write all ci/cd deployment related code in one main.yaml file
    # for now we are keeping a gitkeep file later we will replace it with main.yaml
    ".github/workflows/.gitkeep",
    # to create a local package inside project_name folder we need a __init__.py
    # later we can import it as something like import model.py from project_name
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Creating directory: {filedir} for the file : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # if the file doesnt exist or is empty then it is created
        # open(filepath, "w") opens the file in write mode and pass statement creates the file
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")