from create_server import *
import os
from openai import OpenAI
from dotenv import load_dotenv
    
if __name__ == "__main__" :
    load_dotenv()

    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    server_socket = create_server()

    prompt = "Describe this image"

    while True:
        connection_socket, addr = server_socket.accept()
        
        data_from_nao = connection_socket.recv(4048).decode("utf-8").strip()

        if data_from_nao == "exit" :
            break
        
        if data_from_nao == '' :
            continue

        try : 
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "input_image", "image_url": f"data:image/png;base64,{data_from_nao}"},
            ],
        },
    ],
            )
        except Exception as e :
            response = str(e).encode('UTF-8')

        connection_socket.sendall(response)

    server_socket.close()
    connection_socket.close()