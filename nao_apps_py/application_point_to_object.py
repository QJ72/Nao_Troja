import time
import qi
import almath
from nao_apps_py.nao_classes.PointerToObject import PointerToObject

if __name__ == '__main__':
    #default url : tcp://127.0.0.1:9559
    session = qi.Session()
    session.connect("tcp://192.168.1.101:9559")
    print("Session started.")

    posture = session.service("ALRobotPosture")
    photo_capture = session.service("ALPhotoCapture")
    video_service = session.service("ALVideoDevice")
    motion_service = session.service("ALMotion")

    print(posture.getPosture())
    if posture.getPosture() != "Sit":
        posture.goToPosture("Sit", 0.2)

    pointer = PointerToObject(motion_service,video_service)

    print("Show object to Nao")
    time.sleep(5)
    pointer.point_at_target()

    pointer.unsuscribe_video_service()