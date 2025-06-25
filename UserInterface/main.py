from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
import os
import threading
import time
from nao_apps_py.nao_classes.ConnectionToNaoManager import ConnectionToNaoManager


script_path_server_API = "servers/server_requests.py"
script_path_server_computer_vision = "servers/server_vision.py"


class NonClickableCheckBox(CheckBox):
    def __init__(self, **kwargs):
        super(NonClickableCheckBox, self).__init__(**kwargs)
        self._active = False

    def on_touch_down(self, touch):
        return False if self.collide_point(*touch.pos) else super(NonClickableCheckBox, self).on_touch_down(touch)

class ServerBox(BoxLayout):
    def __init__(self, **kwargs):
        super(ServerBox, self).__init__(**kwargs)
        self.thread_server_API = threading.Thread(target=os.system, args=["python3 " + script_path_server_API])
        self.thread_server_computer_vision = threading.Thread(target=os.system, args=["python3 " + script_path_server_computer_vision])

    def checkbox_callback_call_API(self,checkbox,value):
        if value :
            print("launch server API")
            self.thread_server_API.start()
        else :
            os.system("fuser 8001/tcp -k")
            self.thread_server_API.join()
            self.thread_server_API = threading.Thread(target=os.system, args=["python3 " + script_path_server_API])

    def checkbox_callback_computer_vision(self,checkbox,value):
        if value:
            print("launch server vision")
            self.thread_server_computer_vision.start()
            time.sleep(3)
        else :
            os.system("fuser 8002/tcp -k")
            self.thread_server_computer_vision.join()
            self.thread_server_computer_vision = threading.Thread(target=os.system, args=["python3 " + script_path_server_computer_vision])

class NaoConnector(GridLayout):
    def __init__(self, **kwargs):
        super(NaoConnector, self).__init__(**kwargs)
        self.HOST = "10.11.45.211"
        self.PORT = "9559"
        self.connector_to_nao = ConnectionToNaoManager()
        self.session = None

    def textinput_callback_host(self, value):
        self.HOST = value
        print(self.HOST)

    def textinput_callback_port(self, value):
        self.PORT =value
        print(self.HOST)

    def connect_to_nao(self):
        self.session = self.connector_to_nao.connection_to_nao(self.HOST, self.PORT)
        if self.session is None:
            self.ids.is_nao_connected.active = False
        else :
            self.ids.is_nao_connected.active = True


class MainWindow(FloatLayout):
    pass

class MainApp(App):

    def build(self):
        main_window = MainWindow()
        return main_window

if __name__ == '__main__':
    MainApp().run()