import cv2
import numpy as np
from nao_apps.clients.utilities import return_center_from_server_vision
from nao_apps.nao_classes import Pointer

class NaoPointer(Pointer):
    def __init__(self, motion_service, video_service,resolution = 2, colorSpace = 11): #resolution and colorSpace a bit arbitrary
        Pointer.__init__(self, motion_service)
        self.video_service = video_service
        self.videoClient = video_service.subscribe("Naopointer_client", resolution, colorSpace, 5)
        motion_service.setStiffnesses("Head", 1.0)

    def unsuscribe_video_service(self):
        self.video_service.unsubscribe("Naopointer_client")

    def __adjust_head(self, difference_between_centers, pixels_precision = 20):
        head_yaw = self.motion_service.getAngles("HeadYaw", True)[0]
        head_pitch = self.motion_service.getAngles("HeadPitch", True)[0]

        if np.sum(difference_between_centers) > 2*pixels_precision:
            print("Difference between centers : ", difference_between_centers)
            if difference_between_centers[0] < -pixels_precision :
                self.motion_service.setAngles("HeadYaw", head_yaw+1, 0.2)
            elif difference_between_centers[0] > pixels_precision :
                self.motion_service.setAngles("HeadYaw", head_yaw-1, 0.2)

            if difference_between_centers[1] < -pixels_precision :
                self.motion_service.setAngles("HeadPitch", head_pitch+1, 0.2)
            elif difference_between_centers[1] > pixels_precision :
                self.motion_service.setAngles("HeadPitch", head_pitch-1, 0.2)
            self.look_at_target()



    def __get_new_image_from_nao(self):
        new_image = self.video_service.getImageRemote(self.videoClient)
        if new_image is None:
            print("Error : Nao didn't screenshot")
        image_width = new_image[0]
        image_height = new_image[1]
        image_channels = new_image[2]
        image_data = new_image[6]
        image_data = np.frombuffer(image_data, dtype=np.uint8)
        image_data = image_data.reshape((image_height, image_width, image_channels))
        image_data =  cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
        return image_data, image_width, image_height

    def save_new_image(self):
        new_image, _, _ = self.__get_new_image_from_nao()
        cv2.imwrite("../nao_screenshot.jpg", new_image)

    def look_at_target(self):
        image_data, image_width, image_height = self.__get_new_image_from_nao()
        cv2.imwrite("../nao_screenshot.jpg", image_data)
        center_image = np.array([image_width//2, image_height//2])

        center_object = return_center_from_server_vision("../nao_screenshot.jpg", HOST='127.0.0.2', PORT=8002)
        diff = center_object - center_image

        self.__adjust_head(diff)

    def point_at_target(self):
        self.look_at_target()
        self.point_in_gaze_direction()

    def test_look_at_target(self):
        new_image, _, _ = self.__get_new_image_from_nao()