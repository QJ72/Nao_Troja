from nao_classes.NaoDataset import NaoDataset

def main():
    dataset = NaoDataset("datasets/dataset2")

    print(dataset.get_position_from_image_name("image(1,0)"))



if __name__ == '__main__':
    main()