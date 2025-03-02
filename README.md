# End-to-End-Wines-quality

Creating an end to end ML-based project

## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py

# How to create?
## Steps:

### STEP 1 - Build the repository

we created a repository for our project and added a "readme" file, ".gitignore" file for our python and finally a license of your choice(i chose MIT)
After creating the repository now, clone it with:-

```bash
https://github.com/(your_user_id)/(your_repository_name)
```

### STEP 2 - Creating a template.py file

We create a template.py file and create all our folders and files according to what we want to have in our project

### STEP 3 - Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.12 -y
```

```bash
conda activate mlproj
```

### STEP 4 - Complete setup.py

The setup.py file we created we complete it with our own credentials and details.
The "-e ." is added in requirements.txt to look for the setup.py file automatically

### STEP 5 - Install the requirements

Specify the libraries you want to use in requirements.txt and run the following command:-
```bash
pip install -r requirements.txt
```

### STEP 6 - Logger,Exception Handling, and Utilities

In src/mlProject create logger in __init__.py and run the following command:-
```bash
python main.py
```

This creates logs directory and shows running_logs.log file with logs