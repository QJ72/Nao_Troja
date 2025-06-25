import time

import qi
import torch

from nao_apps_py.nao_classes.ArmManager import ArmManager
from nao_apps_py.nao_classes.ImageCollector import ImageCollector
from nao_apps_py.nao_classes.JointAnglesPredictor import JointAnglesPredictor


number_of_joints_in_arm = 6
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
    motion_service.setStiffnesses("Body",1)

    effector = "RArm"
    motion_service.setStiffnesses(effector, 1)

    right_arm_manager = ArmManager(motion_service, effector)
    image_collector = ImageCollector(video_service,video_client, set_of_joints=joints_in_RArm,dataset_name="dataset2")

    neural_network_dir = "neural_network"
    neural_network_name = "best_nao_model6.pth"

    model = JointAnglesPredictor(num_joints=6)
    model.load_state_dict(torch.load(f'{neural_network_dir}/{neural_network_name}'))
    model.eval()

    starting_and_end_angles = [0.0583338737487793, 0.1088719367980957, 0.06592011451721191, 0.127363920211792, -0.05526590347290039, 0.39480000734329224]

    image = image_collector.get_new_image_from_nao()
    if image is None :
        return 0

    target_angles = model.predict_joints(image).tolist()
    print("target_angles: ", target_angles)
    #motion_service.setStiffnesses(effector, 0)[0.7164199352264404, -0.28229808807373047, 0.11961007118225098, 0.9986758232116699, -0.4019498825073242, 0.4336000084877014]

    right_arm_manager.move_to_target_joints_angles(starting_and_end_angles)

    motion_service.openHand("RHand")

    right_arm_manager.grab_ball(target_angles)
    time.sleep(1)
    right_arm_manager.move_to_target_joints_angles(starting_and_end_angles)

if __name__ == '__main__':
    main()