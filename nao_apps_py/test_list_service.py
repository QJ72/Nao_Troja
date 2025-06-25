from utilities import *
import qi


if __name__ == "__main__" :
    # default url : tcp://127.0.0.1:9559
    session = qi.Session()
    session.connect("tcp://192.168.1.101:9559")

    look_for_services(session)

    motion_service = session.service("ALMotion")

    motion_service.setStiffnesses("RArm", 0)

    print(motion_service.getSummary())
    print(motion_service.getRobotConfig())