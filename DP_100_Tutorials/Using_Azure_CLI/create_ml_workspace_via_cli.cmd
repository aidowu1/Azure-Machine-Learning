# List resource groups
az group list -o table

#Create a new resource group
az group create --name packt-azureml-rg -l uksouth

# Create a new Azure ml workspace
az extension add -n ml
az ml workspace create -n ml-demo3-ws -g packt-azureml-rg

# Delete Resource group
az group delete --name packt-azureml-rg

## Delete the workspace
az ml workspace delete -n ml-demo3-ws -g packt-azureml-rg 
