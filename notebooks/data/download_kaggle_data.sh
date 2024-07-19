#!/bin/bash

# Check if the Kaggle API is installed
if ! command -v kaggle &> /dev/null
then
    echo "Kaggle API is not installed. Please install it and try again."
    exit
fi

# Download the competition data
kaggle competitions download -c galaxy-zoo-the-galaxy-challenge

# Unzip the downloaded files (if necessary)
unzip -o galaxy-zoo-the-galaxy-challenge.zip -d galaxy-zoo-data

echo "Download and extraction completed."
