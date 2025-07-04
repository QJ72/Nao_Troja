import time
from PIL import Image

from nao_apps_py.nao_classes.NaoDatasetGenerator import NaoDatasetGenerator


class ImageCollector:
    def __init__(self, video_service, video_client, set_of_joints, dataset_name : str):
        self.video_service = video_service
        self.video_client = video_client
        self.set_of_joints = set_of_joints
        if dataset_name is not None:
            self.dataset_path = f"datasets/{dataset_name}"
            self.nao_dataset_generator = NaoDatasetGenerator(dataset_name)

    def get_new_image_from_nao(self):
        new_image = self.video_service.getImageRemote(self.video_client)
        if new_image is None:
            print("Error : Nao didn't screenshot")
            return None
        image_width = new_image[0]
        image_height = new_image[1]
        image_data = new_image[6]

        return Image.frombytes("RGB", (image_width, image_height), image_data)

    def mirror_image(self,image):
        return image.transpose(method=Image.FLIP_LEFT_RIGHT)

    def _save_image(self, image,file_name):
        if image is None:
            return False

        image.save(file_name)
        return True

    def collect_images(self, number_of_images, file_name, target_angles, add_to_dataset = True, for_training = True ,time_to_wait = 1):

        for i in range(number_of_images):
            image = self.get_new_image_from_nao()
            if for_training:
                final_file_name = f"train_images/{file_name}{i}.png"
            else :
                final_file_name = f"test_images/{file_name}{i}.png"
            if self._save_image(image, f"{self.dataset_path}/{final_file_name}") :
                print(f"{file_name}{i}.png")
                if not add_to_dataset:
                    return
                self.nao_dataset_generator.add_elemement_to_dataset(final_file_name, target_angles)
            else:
                print(f"Error : couldn't save image {file_name}{i}.png")
                return
            time.sleep(time_to_wait)

        self.nao_dataset_generator.save_to_json()