import socket
import numpy as np

from signal import signal, SIGPIPE, SIG_DFL

signal(SIGPIPE,SIG_DFL)

def create_server(HOST = '127.0.0.1',PORT = 8001, max_simultaneous_connection = 1):

    # Create a socket object 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    # Bind to an address and port 
    server_socket.bind((HOST, PORT))
    server_socket.listen(max_simultaneous_connection)
    
    print("Server is listening...")
    
    return server_socket
    
def bytes_to_image(byte_stream, width=640, height=640, channels=3):
    np_array = np.frombuffer(byte_stream, dtype=np.uint8)
    
    if channels == 1:
        image = np_array.reshape((height, width))
    else:
        image = np_array.reshape((height, width, channels))
    
    return image