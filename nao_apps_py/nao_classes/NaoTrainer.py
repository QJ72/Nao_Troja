import cv2
import matplotlib.pyplot as plt
import numpy as np
import torch

# Set threads for 18-core processor
torch.set_num_threads(16)  # Leave 2 cores for system
torch.set_num_interop_threads(2)

import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import os

from nao_apps_py.nao_classes.JointAnglesPredictor import JointAnglesPredictor
from nao_apps_py.nao_classes.NaoDataset import NaoDataset


class NaoTrainer:
    def __init__(self, dataset_name ="dataset", json_file ="annotations.json", neural_network_dir ="neural_network",
                 dataset_parent_folder ="datasets"):
        self.dataset_dir = f"{dataset_parent_folder}/{dataset_name}"
        self.json_file = json_file
        self.neural_network_dir = neural_network_dir

        self.model_name = "dummy_model"

        self.transform = transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize((224, 224)), # Split dataset
            transforms.ToTensor(),
            #Value from the ImageNet Dataset for alignement (resnet use as backbone in the nn, was trained on imageNet)
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
        ])

        self.device = self._setup_device()
        print(f"Using device: {self.device}")

        self.dataset = None

        self.train_loader = None
        self.test_loader = None

        self.model = None
        self.optimizer = None
        self.criterion = None
        self.scheduler = None
        self._setup_cpu_optimization()

    def _setup_device(self):
        if torch.cuda.is_available():
            self.device = torch.device("cuda")
        # Check for Intel GPU (XPU) support
        elif hasattr(torch, 'xpu') and torch.xpu.is_available():
            self.device = torch.device('xpu')
            print(f"Using Intel Arc GPU: {torch.xpu.get_device_name()}")
        else:
            self.device = torch.device('cpu')
            print("Using CPU (Intel GPU support not available)")
        return self.device

    def set_model_name(self, model_name: str):
        self.model_name = model_name
        return model_name

    def _setup_cpu_optimization(self):
        # Enable Intel MKL optimizations
        os.environ['MKL_NUM_THREADS'] = '16'
        os.environ['OMP_NUM_THREADS'] = '16'

        # Intel-specific optimizations
        if hasattr(torch.backends, 'mkl'):
            torch.backends.mkl.enabled = True
        if hasattr(torch.backends, 'mkldnn'):
            torch.backends.mkldnn.enabled = True

    def load_data(self, test_size=0.2, batch_size=32):
        self.dataset = NaoDataset(self.dataset_dir, self.json_file, self.transform)

        train_dataset = torch.utils.data.Subset(self.dataset, self.dataset.get_train_indices())
        test_dataset = torch.utils.data.Subset(self.dataset, self.dataset.get_test_indices())

        self.train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        self.test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

        print(f"Training samples: {len(train_dataset)}")
        print(f"Test samples: {len(test_dataset)}")

        return self.train_loader, self.test_loader

    def create_model(self, num_joints = 6):
        self.model = JointAnglesPredictor(num_joints).to(self.device)

        self.criterion = nn.MSELoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001, weight_decay=1e-4)
        self.scheduler = optim.lr_scheduler.ReduceLROnPlateau(
            self.optimizer, mode='min', patience=10, factor=0.5
        )

        return self.model

    def train_epoch(self):

        self.model.train()
        total_loss = 0

        for batch_idx, (images, targets) in enumerate(self.train_loader):
            images, targets = images.to(self.device), targets.to(self.device)

            self.optimizer.zero_grad()
            outputs = self.model(images)
            loss = self.criterion(outputs, targets)
            loss.backward()
            self.optimizer.step()

            total_loss += loss.item()

        return total_loss / len(self.train_loader)

    def validate(self):
        self.model.eval()
        total_loss = 0

        with torch.no_grad():
            for images, targets in self.test_loader:
                images, targets = images.to(self.device), targets.to(self.device)
                outputs = self.model(images)
                loss = self.criterion(outputs, targets)
                total_loss += loss.item()

        return total_loss / len(self.test_loader)

    def train(self, epochs=10):
        train_losses = []
        val_losses = []
        best_val_loss = float('inf')

        for epoch in range(epochs):
            print(f"Epoch {epoch + 1}/{epochs}")
            train_loss = self.train_epoch()
            val_loss = self.validate()

            train_losses.append(train_loss)
            val_losses.append(val_loss)

            self.scheduler.step(val_loss)
            print(f"val_loss: {val_loss}, best_val_loss: {best_val_loss}")

            if val_loss < best_val_loss:
                best_val_loss = val_loss
                torch.save(self.model.state_dict(), f'{self.neural_network_dir}/{self.model_name}')

            if epoch % 10 == 0:
                print(f'Epoch {epoch+1:3d}: Train Loss: {train_loss:.6f}, Val Loss: {val_loss:.6f}')

        print(f'Training completed. Best validation loss: {best_val_loss:.6f}')

        self.plot_training_curves(train_losses, val_losses)

        return train_losses, val_losses

    def plot_training_curves(self, train_losses, val_losses):
        plt.figure(figsize=(10, 6))
        plt.plot(train_losses, label='Training Loss')
        plt.plot(val_losses, label='Validation Loss')
        plt.xlabel('Epoch')
        plt.ylabel('Loss (MSE)')
        plt.title('Training Progress')
        plt.legend()
        plt.grid(True)
        plt.savefig('training_curves.png')
        plt.show()

    def predict(self, image_path):
        self.model.eval()

        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = self.transform(image).unsqueeze(0).to(self.device)

        with torch.no_grad():
            prediction = self.model(image)

        return prediction.cpu().numpy()[0]

    def evaluate_model(self):
        self.model.eval()
        all_predictions = []
        all_targets = []

        with torch.no_grad():
            for images, targets in self.test_loader:
                images, targets = images.to(self.device), targets.to(self.device)
                outputs = self.model(images)

                all_predictions.append(outputs.cpu().numpy())
                all_targets.append(targets.cpu().numpy())

        predictions = np.vstack(all_predictions)
        targets = np.vstack(all_targets)

        joint_names = self.dataset.get_joint_names()

        print("\nPer-joint evaluation:")
        for i, name in enumerate(joint_names):
            mse = np.mean((predictions[:, i] - targets[:, i]) ** 2)
            mae = np.mean(np.abs(predictions[:, i] - targets[:, i]))
            print(f"{name:15}: MSE={mse:.6f}, MAE={mae:.6f}")

        overall_mse = np.mean((predictions - targets) ** 2)
        overall_mae = np.mean(np.abs(predictions - targets))
        print(f"\nOverall: MSE={overall_mse:.6f}, MAE={overall_mae:.6f}")
