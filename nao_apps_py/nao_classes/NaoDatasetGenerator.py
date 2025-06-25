import os
import json

from nao_apps_py.nao_classes.NaoConstants import *

class NaoDatasetGenerator:
    def __init__(self, dataset_name : str, json_file ="annotations.json", dataset_parent_folder = "datasets"):
        self.dataset_parent_folder = dataset_parent_folder
        self.dataset_path = f"datasets/{dataset_name}"
        self.json_file = f"{self.dataset_path}/{json_file}"


        os.makedirs(self.dataset_parent_folder, exist_ok=True)
        os.makedirs(self.dataset_path, exist_ok=True)
        os.makedirs(f"{self.dataset_path}/train_images", exist_ok=True)
        os.makedirs(f"{self.dataset_path}/test_images", exist_ok=True)

        if not os.path.exists(self.json_file):
            with open(self.json_file, "w") as f:
                f.write("{}")
            print(f"Created file : {self.json_file}")

        self.json_data = self._init_json()

    def _init_json(self):
        json_data = {}
        try:
            with open(self.json_file) as json_file:
                json_data = json.load(json_file)
        except FileNotFoundError or json.decoder.JSONDecodeError:
            json_data = {}
            open(self.json_file, "w").close()

        if bool(json_data):
            return json_data

        data = {
            "metadata": {
                "task": "joint_position_regression",
                "input_type": "image_paths",
                "output_type": "joint_positions",
                "joint_names": joints_in_RArm,
                "joint_units": "radians",
                "joint_limits": {
                    "RShoulderPitch": [-2.0857, 2.0857],
                    "RShoulderRoll": [-0.3142, 1.3265],
                    "RElbowYaw": [-2.0857, 2.0857],
                    "RElbowRoll": [0.0349, 1.5446],
                    "RWristYaw": [-1.8238, 1.8238],
                    "RHand": [0.0, 1.0]
                },
                "num_samples": 0,
                "num_joints": number_of_joints_in_RArm
            },
            "data": {
                "image_paths": [],
                "joint_positions": []
            }
        }

        with open(self.json_file, 'w') as f:
            json.dump(data, f, indent=2)
            print(f"JSON file initialised: {self.json_file}")
        return data

    def add_elemement_to_dataset(self, file_name : str, joint_positions):
        self.json_data["data"]["image_paths"].append(file_name)
        self.json_data["data"]["joint_positions"].append(joint_positions)

    #May not be very elegant
    def save_to_json(self):
        with open(self.json_file, 'w') as f:
            json.dump(self.json_data, f, indent=2)