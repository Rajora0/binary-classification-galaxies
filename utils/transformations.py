from PIL import Image
import torchvision.transforms as transforms

IMAGE_SHAPE = (200, 200)

def transform_image(image_path):
    """
    Loads, transforms, and prepares the image for the model.

    Args:
        image_path (str): Path to the image.

    Returns:
        torch.Tensor: Transformed image ready for the model.
    """

    transform = transforms.Compose([
        transforms.Resize(IMAGE_SHAPE),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(degrees=10),
        transforms.ToTensor(),
    ])

    image = Image.open(image_path).convert('RGB')
    image = transform(image)
    image = image.unsqueeze(0)  # Add batch dimension
    return image