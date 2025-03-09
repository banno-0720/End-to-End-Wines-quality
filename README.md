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

we created a repository for our project and added a "readme.md" file, ".gitignore" file for our python and finally a license of your choice(i chose MIT)
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

In src/mlProject create logger in "__init__.py" and run the following command:-
```bash
python main.py
```
This creates logs directory and shows "running_logs.log" file with logs

Next, we edit "common.py" for utilities

### STEP 7 - Experiment

Create "Experiment.ipynb" and create the full implementation of your model first in here and understand it

### STEP 8 - Implementing the workflow

Implementing the workflow mentioned above and updating everything accordingly now
Also created the data_ingestion notebook

1. config.yaml contains the basic configuration commands and stuff(so far my understanding of it)
2. schema.yaml contains the data validation commands
3. params.yaml contains the model parameters
4. Copy and paste the entity you created in the notebook
5. Copy and paste the configuration you created in the notebook
6. Add a file in components directory and add the code accordingly
7. Add a file in pipeline directory and write the code accordingly
8. Update the main.py
9. Finally update the app.py

Do this same with data_validation step, then data_transformation step, then model_training step and finally with model_evaluation step

### STEP 9 - Prediction with pipeline

Create "prediction.py" file and write the code accordingly

### STEP 10 - Creating the application

Create the web application or software application whichever you want and take the inputs on it and then finally predict the output with the help of "prediction.py" file created above in the "app.py" file

### STEP 11 - Dockerization

Create docker file with name "Dockerfile". 
The name should be same otherwise it wont work, so make sure it is.

### STEP 12 - CI/CD pipeline

Create a directory of "/.github/worflows" and inside it write the code accordingly which connects to the cloud server and deploys the app

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 970547337635.dkr.ecr.ap-south-1.amazonaws.com/mlproj

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app