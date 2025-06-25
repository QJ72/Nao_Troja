import qi
import utilities

if __name__ == '__main__':
    #default url : tcp://127.0.0.1:9559
    session = qi.Session()
    session.connect("tcp://192.168.1.100:9559")
    motion_service = session.service("ALMotion")
    posture = session.service("ALRobotPosture")

    posture.goToPosture("SitRelax",0.2)


    joint_names = motion_service.getBodyNames("Body")
    joint_angles = motion_service.getAngles(joint_names, True)
    for name,angle in zip(joint_names,joint_angles):
        print(f"joints : {name}, angle : {angle}")