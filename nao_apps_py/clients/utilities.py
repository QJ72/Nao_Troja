import socket
import base64
import os
import cv2
import time

import numpy as np

def send_request_to_server(data, HOST='127.0.0.1', PORT=8001):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((HOST, PORT))

    client_socket.sendall(data.encode('utf-8'))

    response = client_socket.recv(1024).decode()
    print("Received: ", response)

    client_socket.close()

    return response

def encode_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            b64_image = base64.b64encode(image_file.read())

            return b64_image
    except Exception as e:
        print(e)
        return None

def send_image_to_server(image_path, HOST='127.0.0.1', PORT=8001):
    return send_request_to_server(encode_image(image_path),HOST, PORT)

def send_request_to_server_vision(image_path, HOST='127.0.0.2', PORT=8002):
    return send_request_to_server(os.path.abspath(image_path),HOST, PORT)

def treat_image_from_server_vision(answer):
    if answer == "exit" or answer == "":
        return [-1,-1]
    answer = answer.split(" ")
    return np.array([int(answer[0]), int(answer[1])])

def return_center_from_server_vision(image_path, HOST='127.0.0.1', PORT=8001):
    answer = send_request_to_server_vision(image_path, HOST, PORT)
    if answer == "exit":
        return answer
    return treat_image_from_server_vision(answer)

def save_image_from_remote(video_service, videoClient,filename = "nao_screenshot.jpg"):
    new_image = video_service.getImageRemote(videoClient)
    image_width = new_image[0]
    image_height = new_image[1]
    image_channels = new_image[2]
    image_data = new_image[6]
    image_data = np.frombuffer(image_data, dtype=np.uint8)
    image_data = image_data.reshape((image_height, image_width, image_channels))
    image_data = cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB)
    cv2.imwrite(filename, image_data)

def accurate_move(motion_service, list_joints, list_angles, speed = 0.1, wait_between = 0.5):
    for i in range(len(list_angles)):
        motion_service.setAngles(list_joints[i], list_angles[i], speed)
        time.sleep(wait_between)
    time.sleep(2*wait_between)

def grab_one_ball(motion_service, start_angles, end_angles, list_joints, list_angles, speed = 0.1):
    motion_service.openHand("RHand")
    accurate_move(motion_service, list_joints, start_angles)
    accurate_move(motion_service, list_joints, list_angles)
    motion_service.closeHand("RHand")
    accurate_move(motion_service, list_joints, end_angles)
    motion_service.openHand("RHand")

def grab_all_balls(motion_service,list_of_all, list_joints, start_angles,end_angles):
    for list_angles in list_of_all:
        motion_service.openHand("RHand")
        accurate_move(motion_service,list_joints,start_angles)

        print(motion_service.getAngles(list_joints, True))

        accurate_move(motion_service,list_joints, list_angles)

        print("goal : ", list_joints )
        print("real position : ",motion_service.getAngles(list_joints, True))
        motion_service.closeHand("RHand")

        accurate_move(motion_service,list_joints,end_angles)
        motion_service.openHand("RHand")