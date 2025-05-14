import cv2
from ultralytics import YOLO


model = YOLO('best.onnx')

image_path = "example_image.jpg"

results = model(source=image_path)

for result in results:
    xywh = result.boxes.xywh  # center-x, center-y, width, height
    print("xywh : ", xywh)
    names = [result.names[cls.item()] for cls in result.boxes.cls.int()]  # class name of each box
    confs = result.boxes.conf  # confidence score of each box
    image_result = cv2.imread(image_path)
    for (x, y) in xywh[:, :2]:
        cv2.circle(image_result, (int(x), int(y)), 5, (0, 255, 0), 50)

    cv2.imwrite("image_result.jpg", image_result)  # Warning : only in python3