import json

import cv2
import numpy as np
import torch
from torch.utils.data import Dataset


class NaoDataset(Dataset):
    def __init__(self, dataset_dir: str, json_file="annotations.json", transform=None):
        self.dataset_path = dataset_dir
        self.transform = transform
        print(f"Dataset loaded: {self.dataset_path}")
        json_path = f"{self.dataset_path}/{json_file}"

        self.data = None

        with open(json_path, 'r') as f:
            self.data = json.load(f)
            if 'data' in self.data and 'metadata' in self.data:
                self.image_paths = self.data['data']['image_paths']
                self.joint_positions = np.array(self.data['data']['joint_positions'], dtype=np.float32)
                self.joint_names = self.data['metadata']['joint_names']
            else:
                raise ValueError("JSON structure not recognized")

        self.train_indices = []
        self.test_indices = []


        for i, image_path in enumerate(self.image_paths):
            if "test" in image_path:
                self.test_indices.append(i)
            else :
                self.train_indices.append(i)

    def get_meta_data(self):
        return self.data["metadata"]

    def get_data(self):
        return self.data["data"]

    def get_position_from_image_name(self, image_name):
        for i,name in enumerate(self.image_paths):
            if image_name in name:
                return [angle for angle in self.joint_positions[i]]
        return None


    def get_joint_names(self):
        return self.joint_names

    def get_train_indices(self):
        return self.train_indices

    def get_test_indices(self):
        return self.test_indices

    def __len__(self):
        return len(self.image_paths)

    def __getitem__(self, idx):
        img_name = self.image_paths[idx]
        img_path = f"{self.dataset_path}/{img_name}"

        try:
            image = cv2.imread(str(img_path))
            if image is None:
                raise ValueError(f"Could not load image: {img_path}")
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        except Exception as e:
            print(f"Error loading image {img_path}: {e}")
            image = np.zeros((480, 640, 3), dtype=np.uint8)

        joints = self.joint_positions[idx]

        if self.transform is not None:
            image = self.transform(image)

        return image, torch.tensor(joints, dtype=torch.float32)

    def get_joint_names(self):
        """Return list of joint names"""
        return self.joint_names

    def get_joint_limits(self):
        """Return joint limits if available in metadata"""
        # You can extend this to read from metadata
        return {
            'RShoulderPitch': [-2.0857, 2.0857],
            'RShoulderRoll': [-0.3142, 1.3265],
            'RElbowYaw': [-2.0857, 2.0857],
            'RElbowRoll': [0.0349, 1.5446],
            'RWristYaw': [-1.8238, 1.8238],
            'RHand': [0.0, 1.0]
        }