from clients.utilities import *
import os

from nao_apps.clients.utilities import treat_image_from_server_vision

if __name__ == "__main__" :
    print("call to server")

    image_path = "nao_screenshot.jpg"

    image_path = os.path.abspath(image_path)
    response = treat_image_from_server_vision(send_request_to_server(image_path, HOST='127.0.0.2', PORT=8002))

    print(response)