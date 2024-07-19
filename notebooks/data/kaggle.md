The error message indicates that the Kaggle API cannot find the `kaggle.json` file, which contains your Kaggle API credentials. This file should be placed in the `.kaggle` directory under your home directory.

Here's how to fix this issue:

1. **Obtain the `kaggle.json` file:**
   - Go to your Kaggle account settings (https://www.kaggle.com/account).
   - Scroll down to the "API" section and click on "Create New API Token". This will download a file named `kaggle.json`.

2. **Place the `kaggle.json` file in the correct location:**
   - Move the `kaggle.json` file to the `.kaggle` directory under your home directory. You can do this using the terminal:

     ```bash
     mkdir -p ~/.kaggle
     mv ~/Downloads/kaggle.json ~/.kaggle/
     chmod 600 ~/.kaggle/kaggle.json
     ```

   - The `chmod 600` command ensures that only you can read and write this file.

3. **Verify the Kaggle API installation:**
   - Make sure the Kaggle API is properly installed in your Anaconda environment. You can do this by running:

     ```bash
     conda install -c conda-forge kaggle
     ```

4. **Run the script again:**
   - After ensuring that your Kaggle credentials are correctly set up, run your script again:

     ```bash
     ./download_kaggle_data.sh
     ```

Your script should now be able to authenticate with Kaggle and download the data successfully.

### Updated Script
To ensure that the script does not proceed if the download fails, you can add error handling:

```bash
#!/bin/bash

# Check if the Kaggle API is installed
if ! command -v kaggle &> /dev/null
then
    echo "Kaggle API is not installed. Please install it and try again."
    exit 1
fi

# Download the competition data
if ! kaggle competitions download -c galaxy-zoo-the-galaxy-challenge; then
    echo "Failed to download the competition data."
    exit 1
fi

# Unzip the downloaded files (if necessary)
if ! unzip -o galaxy-zoo-the-galaxy-challenge.zip -d galaxy-zoo-data; then
    echo "Failed to unzip the competition data."
    exit 1
fi

echo "Download and extraction completed."
```

This version of the script will exit with an error message if the download or unzip steps fail.