from nao_classes.NaoDataset import NaoDataset
from nao_classes.NaoDatasetGenerator import NaoDatasetGenerator

def main():
    dataset_generator = NaoDatasetGenerator("dataset2", json_file="annotations.json")
    print(dataset_generator.json_data)

if __name__ == '__main__':
    main()