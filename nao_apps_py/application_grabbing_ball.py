import qi
import cv2

from nao_apps_py.clients.utilities import send_request_to_server_vision, save_image_from_remote, accurate_move, \
    grab_all_balls, grab_one_ball
from nao_classes import *
import time
import numpy as np

FRAME_TORSO = 0
FRAME_WORLD = 1
FRAME_ROBOT = 2

MASK_X = 1
MASK_Y = 2
MASK_Z = 4
MASK_WX = 8
MASK_WY = 16
MASK_WZ = 32

X = 0
Y = 1
Z = 2
WX = 3
WY = 4
WZ = 5

AXIS_MASK_POSITION = 7
AXIS_MASK_ROTATION = 56
AXIS_MASK_BOTH = 63

if __name__ == '__main__':
    #default url : tcp://127.0.0.1:9559
    session = qi.Session()
    session.connect("tcp://10.11.45.211:9559")

    posture = session.service("ALRobotPosture")
    video_service = session.service("ALVideoDevice")
    motion_service = session.service("ALMotion")
    videoClient = video_service.subscribe("video_client", 2, 11, 5)

    motion_service.wakeUp()

    should_be_grabbing = False

    if posture.getPosture() != "Sit":
        posture.goToPosture("Sit", 0.2)

    effector = "RArm"
    space = FRAME_TORSO
    position = [0.2,0,0,0,0,0]
    axisMask = AXIS_MASK_BOTH
    speed = 0.2
    isAbsolute = True

    arm_manager = ArmManager(motion_service, effector, space)
    print("position hand : ", arm_manager.get_current_position())

    motion_service.setStiffnesses("Head", 1)
    motion_service.setAngles("HeadPitch", np.pi/12,0.2)
    time.sleep(1)

    video_service.setActiveCamera(videoClient, 1)

    time.sleep(1)
    #save_image_from_remote(video_service,videoClient)

    #send_request_to_server_vision("nao_screenshot.jpg")
    list_joints_right_arm = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll", "RWristYaw", "RHand"]    
    list_angles_1 = [0.22400593757629395, -1.132133960723877, -0.18719005584716797, 1.5217700004577637, 0.6963939666748047, 0.9783999919891357]
    list_angles_2 = [0.21480202674865723, -0.15497589111328125, 0.013764142990112305, 0.03490658476948738, 1.4173741340637207, 0.9779999852180481]
    list_angles_3 = [0.18105387687683105, -0.3789398670196533, -0.14730596542358398, 1.1766200065612793, 1.1842060089111328, 0.9779999852180481]
    list_angles_4 = [0.4356980323791504, -0.013848066329956055, 0.23466014862060547, 1.018618106842041, 0.6549761295318604, 0.9779999852180481]
    list_angles_5 = [0.21940398216247559, 0.04137611389160156, 0.0030260086059570312, 0.31297802925109863, 1.047680139541626, 0.9779999852180481]
    list_angles_6 = [0.1963939666748047, 0.29141807556152344, -0.26389002799987793, 1.04929780960083, 0.8160459995269775, 0.9779999852180481]

    start_angles = [-0.3543119430541992, -0.0353238582611084, 1.3544800281524658, 0.9357819557189941, -0.8811380386352539, 0.013599991798400879]

    list_of_all = [list_angles_1, list_angles_2, list_angles_3, list_angles_4, list_angles_5, list_angles_6]

    end_angles = [0, -np.pi , 0, 0, 0, 0]

    grab_all_balls(motion_service, list_of_all, list_joints_right_arm, start_angles, end_angles)

    #print("real position : ",motion_service.getAngles(list_joints_right_arm, True))

    #grab_one_ball(motion_service,start_angles, end_angles, list_joints_right_arm, list_angles_6)

    if should_be_grabbing:
        motion_service.openHand("RHand")

        current_position = arm_manager.get_current_position()

        arm_manager.move_with_trajectory_planning(position,speed,axisMask)

        current_position = arm_manager.get_current_position()
        print("current position : ", current_position)

        new_position = current_position
        new_position[Y]     += 0.1
        print("new_position : ", new_position)

        arm_manager.move_with_trajectory_planning(new_position,speed,axisMask)

        motion_service.closeHand("RHand")


    motion_service.setStiffnesses("Body",1)
    video_service.unsubscribe("video_client")
    session.close()