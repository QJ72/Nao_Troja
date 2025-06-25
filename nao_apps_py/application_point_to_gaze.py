import time
import qi
from nao_apps_py.nao_classes.Pointer import *

if __name__ == '__main__':
    #default url : tcp://127.0.0.1:9559
    session = qi.Session()
    session.connect("tcp://192.168.1.101:9559")
    print("Session started.")

    posture = session.service("ALRobotPosture")
    photo_capture = session.service("ALPhotoCapture")
    video_service = session.service("ALVideoDevice")
    motion_service = session.service("ALMotion")
    memory_service = session.service("ALMemory")
    tracker_service = session.service("ALTracker")
    face_tracker_service = session.service("ALFaceTracker")

    pointer = Pointer(motion_service)

    print(posture.getPosture())
    if posture.getPosture() != "Sit":
        posture.goToPosture("Sit", 0.4)

    motion_service.setStiffnesses("Head", 1.0)

    face_tracker_service.startTracker()
    print("start tracking")

    resolution = 2  # VGA
    colorSpace = 11  # RGB

    videoClient = video_service.subscribe("python_client", resolution, colorSpace, 5)

    img = video_service.getImageRemote(videoClient)

    video_service.unsubscribe(videoClient)

    set_joins = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RElbowYaw", "RWristYaw"]
    set_coords = [0.2, -0.3, 0.0, 0.0, 0.0]
    motion_service.setAngles(set_joins, set_coords, 0.2)
    motion_service.openHand("RHand")

    for i in range(30):
        pointer.point_in_gaze_direction()
        time.sleep(0.02)
        print(i)

    face_tracker_service.stopTracker()
    motion_service.setStiffnesses("Head", 0.0)

    posture.goToPosture("Sit", 0.4)