import torch.nn as nn
from torchvision.models import resnet18
import torchvision.transforms as transforms
import torch

class JointAnglesPredictor(nn.Module):
    def __init__(self, num_joints=6):
        super(JointAnglesPredictor, self).__init__()

        self.backbone = resnet18(pretrained=True)

        self.backbone.fc = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(256, num_joints)
        )
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    def forward(self, x):
        return self.backbone(x)

    def predict_joints(self,image):
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], #see training for value
                                 std=[0.229, 0.224, 0.225])
        ])
        image = transform(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            joints = self(image)

        return joints.cpu().numpy()[0]