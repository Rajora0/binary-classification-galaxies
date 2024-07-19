import torch

def predict_class(image_tensor, model):
    """
    Predicts the class of the image using the model.

    Args:
        image_tensor (torch.Tensor): Transformed image.
        model (torch.nn.Module): The loaded PyTorch model.

    Returns:
        str: Predicted class (eliptical or spiral).
        float: Confidence of the prediction.
    """

    with torch.no_grad():
        device = torch.device("cpu")
        output = model(image_tensor.to(device))
        probabilities = torch.softmax(output, dim=1)
        predicted_class_index = torch.argmax(probabilities, dim=1).item()
        confidence = torch.max(probabilities).item()

    classes = ['eliptical', 'spiral']
    predicted_class = classes[predicted_class_index]

    return predicted_class, confidence