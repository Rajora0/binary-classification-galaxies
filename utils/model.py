import os
import torch
import torch.nn as nn
from efficientnet_pytorch import EfficientNet

class EffNet(nn.Module):
    def __init__(self, n_classes):
        super(EffNet, self).__init__()
        self.b4 = EfficientNet.from_pretrained('efficientnet-b0')
        self.drop = nn.Dropout(0.2)
        self.fc = nn.Linear(1000, n_classes)

    def forward(self, image):
        x = self.b4(image)
        x = self.drop(x)
        out = self.fc(x)
        return out

def load_model():
    device = torch.device("cpu")
    net = EffNet(n_classes=2).to(device)
    model_path = os.path.join(os.path.dirname(__file__), 'models', 'modelo_galaxias.pth')
    net.load_state_dict(torch.load(model_path))  # Adjust path if needed
    net.eval()
    return net