import os
import json
import shutil

from nao_apps_py.nao_classes.NaoConstants import *

class NaoDatasetGenerator:
    def __init__(self, dataset_name : str, json_file ="annotations.json", dataset_parent_folder = "datasets", joint_names = joints_in_RArm):
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

        self.json_data = self._init_json(joint_names)

    def _init_json(self, joint_names = joints_in_RArm):
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
                "joint_names": joint_names,
                "joint_units": "radians",
                "num_samples": 0,
                "num_joints": len(joint_names)
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

    def get_joints_names(self):
        return self.json_data["metadata"]["joint_names"]

    def get_number_of_joints(self):
        return self.json_data["metadata"]["num_joints"]

    def get_metadata(self):
        return self.json_data["metadata"]

    def add_elemement_to_dataset(self, file_name : str, joint_positions):
        self.json_data["data"]["image_paths"].append(file_name)
        self.json_data["data"]["joint_positions"].append(joint_positions)
        self.json_data["metadata"]["num_samples"] += 1

    def add_joints_to_dataset(self, new_joints, new_values):
        if new_joints in self.json_data["metadata"]["joint_names"]:
            print("Error")
            return False
        for joint in new_joints:
            self.json_data["metadata"]["joint_names"].append(joint)
        for value in new_values:
            for joint_positions in self.json_data["data"]["joint_positions"] :
                joint_positions.append(value)

        self.json_data["metadata"]["num_joints"] += len(self.json_data["metadata"]["joint_names"])
        self.json_data["metadata"]["num_samples"] = len(self.json_data["data"]["image_paths"])
        self.save_to_json()
        return True

    #May not be very elegant
    def save_to_json(self):
        with open(self.json_file, 'w') as f:
            json.dump(self.json_data, f, indent=2)