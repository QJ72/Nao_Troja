import socket
import os
from mistralai import Mistral
from dotenv import load_dotenv
from signal import signal, SIGPIPE, SIG_DFL

signal(SIGPIPE,SIG_DFL)

def create_server(HOST = 'localhost',PORT = 8001, max_simultaneous_connection = 1):

    # Create a socket object 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    # Bind to an address and port 
    server_socket.bind((HOST, PORT)) 
    server_socket.listen(max_simultaneous_connection)
    
    print("Server is listening...")
    
    return server_socket

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
