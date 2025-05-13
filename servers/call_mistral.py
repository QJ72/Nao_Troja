from create_server import *
import os
from mistralai import Mistral
from dotenv import load_dotenv

if __name__ == "__main__" :
    load_dotenv()

    api_key = os.environ["MISTRAL_API_KEY"]
    model = "mistral-large-latest"

    client = Mistral(
        api_key=os.environ.get("MISTRAL_API_KEY"),
    )

    server_socket = create_server()

    while True:
        connection_socket, addr = server_socket.accept()
        
        data_from_nao = connection_socket.recv(2048)

        if data_from_nao == "exit" :
            break
        
        if data_from_nao == '' :
            continue

        try : 
            response = client.chat.complete(
            model= model,
            messages=[
                {"role": "user",
                 "content": data_from_nao}
                ]
            )

            response = str(response.choices[0].message.content).encode('UTF-8')

        except Exception as e :
            response = str(e).encode('UTF-8')

        connection_socket.sendall(response)

    server_socket.close()
    connection_socket.close()
