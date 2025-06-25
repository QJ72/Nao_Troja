import errno
import time
import socket

import qi

class ConnectionToNaoManager:
    def __init__(self):
        self.session = qi.Session()

    def connection_to_nao(self, host,port):
        adress = "tcp://" + host + ":" + port
        if self.session.isConnected():
            return self.session

        while True:
            try :
                self.session.connect(adress)
                return self.session
            except Exception as e:
                print(e)
                if e.__class__ == RuntimeError :
                    return None