#!/bin/bash

echo "$(date) - Removing old image"
docker image rm sandyvoiceepayregistry.azurecr.io/voicee-pay-react:v1 

echo "$(date) - Done with image removal and started to rebuild the image"
docker build -t sandyvoiceepayregistry.azurecr.io/voicee-pay-react:v1 .

echo "$(date) - Done with rebuild and started pushing to ACR"
docker push sandyvoiceepayregistry.azurecr.io/voicee-pay-react:v1

echo "$(date) - Done pushing to ACR"
