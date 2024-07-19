## Binary Galaxy Classification with EfficientNet-B0 and PyTorch

This project implements a binary classification model to distinguish between spiral and elliptical galaxies using the EfficientNet-B0 architecture and the PyTorch framework. The model was trained on a subset of the Galaxy Zoo dataset and achieved high accuracy in classifying galaxy images.

### Project Structure:

```
├── utils
│   ├── prediction.py
│   ├── model.py
│   └── transformations.py
└── app.py

```

### File Description:

- **app.py:** Contains the main code for the Gradio interface, which allows users to upload images and obtain predictions from the model.
- **utils/model.py:** Defines the `EffNet` class, which loads a pre-trained EfficientNet-B0 model and adds a dropout layer and a fully connected layer for binary classification.
- **utils/prediction.py:** Includes the `predict_class` function that receives an image tensor and returns the predicted class (elliptical or spiral) and the confidence of the prediction.
- **utils/transformations.py:** Defines the `transform_image` function, which loads an image from the specified path, applies the necessary transformations and returns the image tensor ready for use by the model.

### Dependencies:

The project requires the following Python libraries:

- torch
- torchvision
- efficientnet_pytorch
- Pillow
- gradio
- scikit-learn

You can install the dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### How to Run the Project:

1. Clone the repository:

```bash
git clone https://github.com/your-username/galaxy-classification.git
```

2. Navigate to the project directory:

```bash
cd galaxy-classification
```

3. Run the Gradio application:

```bash
python app.py
```

4. Access the Gradio interface in your browser, at the address provided in the terminal.

5. Upload an image of a galaxy and click "Submit." The model will classify the image as elliptical or spiral and display the predicted class and the confidence of the prediction.

### Training a Custom Model:

The project includes Jupyter notebooks that guide you through the process of training your own custom model.  Here's how:

1. **Data Preparation:**
   - Download the Galaxy Zoo dataset or use your own dataset of galaxy images.
   - Organize your data into separate folders for each class (e.g., "spiral" and "elliptical").
   - Use the provided data loading and preprocessing functions to prepare your data for training.

2. **Model Training:**
   - Open the `training.ipynb` Jupyter notebook.
   - Modify the notebook to load your prepared dataset.
   - Adjust hyperparameters such as learning rate, batch size, and number of epochs as needed.
   - Execute the notebook cells to train the model.

3. **Model Evaluation:**
   - Evaluate the trained model's performance on a separate test set.
   - Use metrics like accuracy, precision, recall, and F1-score to assess the model's effectiveness.

4. **Model Deployment:**
   - Once satisfied with your trained model, save it. 
   - Update the `app.py` file to load and utilize your custom-trained model.

### Acknowledgments:

- This project was inspired by the Galaxy Zoo challenge on Kaggle.
- We thank the creators of EfficientNet and PyTorch for their amazing work.
