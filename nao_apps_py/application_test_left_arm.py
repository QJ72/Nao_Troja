import time

import qi

from nao_apps_py.nao_classes.ArmManager import ArmManager

joints_in_RArm = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
joints_in_LArm = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand"]

def main():
    # default url : tcp://127.0.0.1:9559
    session = qi.Session()
    session.connect("tcp://10.11.45.211:9559")

    print("session connected")
    motion_service = session.service("ALMotion")
    motion_service.setStiffnesses("Body", 1)

    left_arm = ArmManager(motion_service, "LArm")
    target_angles = [0,0,0,0,0,0]

    left_arm.move_to_target_joints_angles(target_angles,0.2)
    print(left_arm.get_current_angles())
    print("after move")

if __name__ == "__main__":
    main()