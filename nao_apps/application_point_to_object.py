import time
import qi
from nao_apps.nao_classes.PointerToObject import PointerToObject

if __name__ == '__main__':
    #default url : tcp://127.0.0.1:9559
    application = qi.Application(url="tcp://192.168.1.101:9559")
    application.start()
    print("Application started.")

    posture = application.session.service("ALRobotPosture")
    photo_capture = application.session.service("ALPhotoCapture")
    video_service = application.session.service("ALVideoDevice")
    motion_service = application.session.service("ALMotion")

    print(posture.getPosture())
    if posture.getPosture() != "Sit":
        posture.goToPosture("Sit", 0.2)

    pointer = PointerToObject(motion_service,video_service)

    print("Show object to Nao")
    time.sleep(5)
    pointer.point_at_target()

    pointer.unsuscribe_video_service()

    application.stop()
    time.sleep(5)