import os 
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "mlProject"

# You can edit or add names of files and folders of what you wanna have here
# You can run it again after editing and it will add the file you have added after having run the script once already without duplicating other files and folders
# NOTE:- It wont delete files though.(I think for now you need to do it manually yourself)
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
    "templates/index.html"
]

# Function in order to create our files and folders
for filepath in list_of_files:
    filepath = Path(filepath) # It detects the OS you using and reads the folder and file names accordingly then further
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)) == 0: # This is done so in order to not read and skip the folders which are already made and have content in it
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")