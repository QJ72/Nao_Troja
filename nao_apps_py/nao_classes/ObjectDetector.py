import cv2
from ultralytics import YOLO
from DepthEstimator import DepthEstimator
import numpy as np


class ObjectDetector:
    def __init__(self, path_to_neural_network, device="cpu"):
        self.path_to_neural_network = path_to_neural_network
        self.model = YOLO(path_to_neural_network, task="detect")
        self.depth_model = DepthEstimator(device=device)

    def new_center_of_object(self,list_of_center):
        n = len(list_of_center)
        if n == 1:
            return list_of_center[0]

        new_center_current_indice = 1
        for i in range(1, n):
            if np.linalg.norm(list_of_center[i] - list_of_center[0]) < np.linalg.norm(
                    list_of_center[new_center_current_indice] - list_of_center[0]):
                new_center_current_indice = i
        return list_of_center[new_center_current_indice]

    def detect_object(self, image_path,target=None):
        results=self.model(source=image_path, stream=False)
        object_detected=False
        depth=-1
        image =cv2.imread(image_path)
        depth_map = self.depth_model.estimate_depth(image)
        current_centers = []
        xydepth = None

        for result in results:
            xywh = result.boxes.xywh  # center-x, center-y, width, height
            print("xywh : ", xywh)
            print("xyxy : ", result.boxes.xyxy)
            names = [result.names[cls.item()] for cls in result.boxes.cls.int()]  # class name of each box
            print(names)
            confs = result.boxes.conf  # confidence score of each box
            for i, (x, y) in enumerate(xywh[:, :2]):
                if len(names[i]) > 0:
                    current_centers.append(np.array([x, y]))
                    object_detected = True
                    depth = self.depth_model.get_depth_in_region(depth_map, result.boxes.xyxy[0])

            if object_detected:
                new_center = self.new_center_of_object(current_centers)
                xydepth = [new_center[0],new_center[1],depth]
                cv2.circle(image, (int(new_center[0]), int(new_center[1])), 10, (0, 255, 0), 10)
                cv2.imwrite("image_results.jpg", image)
                current_centers = [new_center]
            else:
                cv2.imwrite("image_results_without_object.jpg", image)
                break
        return xydepth