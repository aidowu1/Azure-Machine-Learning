#! /usr/bin/sh

# Create random string
guid=$(cat /proc/sys/kernel/random/uuid)
suffix=${guid//[-]/}
suffix=${suffix:0:18}

# Set the necessary variables
RESOURCE_GROUP="rg-dp100-l${suffix}"
RESOURCE_PROVIDER="Microsoft.MachineLearning"
REGION="uksouth"
WORKSPACE_NAME="mlw-dp100-l${suffix}"
COMPUTE_INSTANCE="ci${suffix}"
COMPUTE_CLUSTER="aml-cluster"
ENVIRONMENT_CONFIG="./mslearn-aml-cli/Allfiles/Labs/01/basic-env.yml"
DATA_PATH="./mslearn-aml-cli/Allfiles/Labs/01/data-local-path.yml"

echo "Clone the lab repo..."
git clone https://github.com/MicrosoftLearning/mslearn-aml-cli.git mslearn-aml-cli

# Register the Azure Machine Learning resource provider in the subscription
echo "Register the Machine Learning resource provider:"
az provider register --namespace $RESOURCE_PROVIDER

# Create the resource group and workspace and set to default
echo "Create a resource group and set as default:"
az group create --name $RESOURCE_GROUP --location $REGION
az configure --defaults group=$RESOURCE_GROUP

echo "Create an Azure Machine Learning workspace:"
az ml workspace create --name $WORKSPACE_NAME 
az configure --defaults workspace=$WORKSPACE_NAME 

# Create compute instance
echo "Creating a compute instance with name: " $COMPUTE_INSTANCE
az ml compute create --name ${COMPUTE_INSTANCE} --size STANDARD_DS11_V2 --type ComputeInstance 

# Create an environment (i.e. based on the yaml file: mslearn-aml-cli/Allfiles/Labs/01/basic-env.yml which calls the Conda file located here:  conda-envs/basic-env-cpu.yml)
echo "Creating an environment.."
az ml environment create --file ${ENVIRONMENT_CONFIG}

# Create a dataset in the workspace from a local CSV (i.e. based on the yaml file: data-local-path.yml which points to the data file: Allfiles/Labs/01/data/diabetes.csv)
echo "Creating the dataset.."
az ml data create --file ${DATA_PATH}



