from nao_classes.NaoDataset import NaoDataset
from nao_classes.NaoDatasetGenerator import NaoDatasetGenerator

def main():
    dataset = NaoDataset("datasets/dataset2")

    print(dataset.get_position_from_image_name("image(1,0)"))
    dataset_generator = NaoDatasetGenerator("dataset3")

    new_joints = ["LHipPitch","RHipPitch"]
    new_values = [-0.6994619369506836,-0.6995458602905273]

    dataset_generator.add_joints_to_dataset(new_joints, new_values)


if __name__ == '__main__':
    main()