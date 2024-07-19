import gradio as gr
from utils.model import load_model
from utils.transformations import transform_image
from utils.prediction import predict_class

# Load the model only once when the application starts
net = load_model()

def classify_image(image_path):
    """
    Main function for the Gradio interface.
    """
    image_tensor = transform_image(image_path)
    predicted_class, confidence = predict_class(image_tensor, net)
    return f"Predicted Class: {predicted_class}, Confidence: {confidence:.2f}"

iface = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="filepath"),
    outputs="text",
    title="Galaxy Classification",
    description="Upload an image of a galaxy to classify it."
)

iface.launch()