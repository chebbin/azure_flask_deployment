# azure_flask_deployment
azure flask deployment

## Setting up the application
Did this with the professor on the zoom, and then tried multiple times using the slides as a reference, but was unable to successfully deploy the website

### First step geting the cli
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

### Tested the install and then logged in with it
az
az login -use device-code

### Got the azure student subscription ID and changed into it
az account list --output table
az account set -subscription a6fd43ef-7c0c-4ee8-a8c1-823303c65e74

### Set up the resource group in azure
chevi504

### Created the web name 
az webapp up --resource-group chevi504 --name chevi-504-flask --runtime PYTHON:3.9 --sku B1
Got a long error message starting and ending with:
ZIP does not support timestamps before 1980








