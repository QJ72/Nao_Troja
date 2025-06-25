import qi

from nao_apps_py.nao_classes.ArmManager import ArmManager

joints_in_RArm = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]
joints_in_LArm = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand"]


def main():
    # default url : tcp://127.0.0.1:9559
    session = qi.Session()
    session.connect("tcp://10.11.45.211:9559")
    motion_service = session.service("ALMotion")
    posture = session.service("ALRobotPosture")
    video_service = session.service("ALVideoDevice")
    video_client = video_service.subscribe("video_client", 2, 11, 5)

    posture.goToPosture("Crouch", 0.2)

    right_arm_manager = ArmManager(motion_service,"RArm")
    left_arm_manager = ArmManager(motion_service,"LArm")

    starting_and_end_angles = [0.0583338737487793, 0.1088719367980957, 0.06592011451721191, 0.127363920211792,
                               -0.05526590347290039, 0.39480000734329224]

    right_arm_manager.move_to_target_joints_angles(starting_and_end_angles)
    left_arm_manager.move_to_target_joints_angles([1.5,0.15,0,0,0,0])
    motion_service.setStiffnesses("LArm", 0)


if __name__ == "__main__":
    main()