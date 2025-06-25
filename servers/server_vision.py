from create_server import *
from ultralytics import YOLO
from depth_model import DepthEstimator
import base64
import cv2

path_to_neural_network_from_user_interface = "servers/general.pt"

if __name__ == "__main__" :
    server_socket = create_server(HOST='127.0.0.2' ,PORT = 8002)

    model = YOLO(path_to_neural_network_from_user_interface, task="detect")

    depth_model = DepthEstimator(device="cpu")

    current_centers = []
    while True:
        connection_socket, addr = server_socket.accept()
        data_from_nao = connection_socket.recv(4048).decode('utf-8').strip() #absolute path to the image

        print(f"data from Nao : {data_from_nao}")

        if data_from_nao == "exit" :
            print("received exit")
            break

        results = model(source=data_from_nao, stream=False)

        response = ""
        object_detected = False
        depth = -1
        image = cv2.imread(data_from_nao)
        depth_map = depth_model.estimate_depth(image)

        for result in results:
            xywh = result.boxes.xywh  # center-x, center-y, width, height   
            print("xywh : ", xywh)
            print("xyxy : ", result.boxes.xyxy)
            names = [result.names[cls.item()] for cls in result.boxes.cls.int()]  # class name of each box
            print(names)
            confs = result.boxes.conf  # confidence score of each box
            image_result = cv2.imread(data_from_nao)    
            for i,(x, y) in enumerate(xywh[:, :2]):
                if len(names[i]) > 0:
                    current_centers.append(np.array([x,y]))
                    object_detected = True
                    depth = depth_model.get_depth_in_region(depth_map , result.boxes.xyxy[0])
            
            if object_detected :
                new_center = new_center_of_object(current_centers)
                response = f"{int(new_center[0])} {int(new_center[1])} {int(depth)}"
                cv2.circle(image_result,(int(new_center[0]),int(new_center[1])), 10 ,(0,255,0), 10)
                cv2.imwrite("image_results.jpg", image_result)
                current_centers = [new_center]
            else :
                cv2.imwrite("image_results_without_object.jpg", image_result)
                response = "exit"
                break
        
        print("answer : ", response)
        connection_socket.sendall(response.encode("utf-8"))

    server_socket.close()
    connection_socket.close()
    print("Server is closed.")