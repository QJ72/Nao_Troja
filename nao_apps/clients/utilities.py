import socket
import base64
import os

import numpy as np

def send_request_to_server(data, HOST='127.0.0.1', PORT=8001):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((HOST, PORT))

    # Send data
    client_socket.sendall(data.encode('utf-8'))

    # Receive response
    response = client_socket.recv(1024).decode()
    print("Received: ", response)
    # Close the connection

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

def send_request_to_server_vision(image_path, HOST='127.0.0.1', PORT=8001):
    return send_request_to_server(os.path.abspath(image_path),HOST, PORT)

def treat_image_from_server_vision(answer):
    answer = answer.split(" ")
    return np.array([int(answer[0]), int(answer[1])])

def return_center_from_server_vision(image_path, HOST='127.0.0.1', PORT=8001):
    answer = send_request_to_server_vision(image_path, HOST, PORT)
    if answer == "exit":
        return answer
    return treat_image_from_server_vision(answer)