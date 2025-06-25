import time

import qi

from nao_apps_py.nao_classes.ArmManager import ArmManager
from nao_apps_py.nao_classes.ImageCollector import ImageCollector

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

    video_service.setActiveCamera(video_client, 1)

    print(video_service.getActiveCamera())

    motion_service.setStiffnesses("Body",1)

    image_collector = ImageCollector(video_service,video_client, set_of_joints=joints_in_RArm, dataset_name="dataset2")

    effector = "RArm"
    motion_service.setStiffnesses(effector, 1)

    right_arm_manager = ArmManager(motion_service, effector)

    left_arm_manager = ArmManager(motion_service, "LArm")

    starting_and_end_angles = [0.0583338737487793, 0.1088719367980957, 0.06592011451721191, 0.127363920211792, -0.05526590347290039, 0.39480000734329224]

    target_angles = [0.69187593, -0.45103788, 0.13955212, 0.87749004, -0.33905602, 0.38959998]

    print(f"goal_position: {target_angles}")

    #motion_service.setStiffnesses(effector, 0)

    collection_mode = False

    if collection_mode :
        image_collector.collect_images(100,"image(1,0)_without_grid", target_angles, add_to_dataset=True, for_training=False)
        return 0

    right_arm_manager.move_to_target_joints_angles(starting_and_end_angles)

    motion_service.openHand("RHand")

    right_arm_manager.grab_ball(target_angles)

    print(f"end position : {right_arm_manager.get_current_angles()}")

    time.sleep(1)
    right_arm_manager.move_to_target_joints_angles(starting_and_end_angles)

    return 0

if __name__ == '__main__':
    main()