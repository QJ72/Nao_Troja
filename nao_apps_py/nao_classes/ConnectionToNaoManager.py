from errno import EHOSTUNREACH
import time

import qi

class ConnectionToNaoManager:
    def __init__(self):
        self.session = qi.Session()

    def connection_to_nao(self, host:str,port:str):
        adress = f"tcp://{host}:{port}"
        print(f"is session connected : {self.session.isConnected()}")
        if self.session.isConnected():
            return self.session

        while True:
            try :
                self.session.connect(adress)
                print(f"session : {self.session.isConnected()}")
                return self.session
            except Exception as e:
                print(f"error : {e}")
                if "No route to host" in str(e) :
                    print("No route to host - check network/IP")
                    return None
                time.sleep(1)
