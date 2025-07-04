import time
from nao_apps_py.nao_classes.NaoConstants import *

FRAME_TORSO = 0

joints_in_RArm = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw" ,"RElbowRoll", "RWristYaw", "RHand"]
joints_in_LArm = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand"]

class ArmManager:
    def __init__(self,motion_service, effector, space = FRAME_TORSO):
        self.motion_service = motion_service
        self.effector = effector
        self.space = space
        self.counter = 0

    def get_current_position(self):
        return self.motion_service.getPosition(self.effector,self.space, True)

    def get_current_angles(self):
        return self.motion_service.getAngles(self.effector, True)

    def move_to_target_joints_angles(self, angles, speed = 0.1, mirror = False):
        if mirror:
            angles[1] = -angles[1]
            angles[2] = -angles[2]
            angles[4] = -angles[4]
        half_move = [angle*0.5 for angle in angles]
        set_of_joints = None
        if self.effector == "RArm":
            set_of_joints = joints_in_RArm
        elif self.effector == "LArm":
            set_of_joints = joints_in_LArm
        self.motion_service.setAngles(set_of_joints, half_move, speed)
        time.sleep(0.5)
        self.motion_service.setAngles(set_of_joints, angles, speed)
        time.sleep(0.5)

        return self.get_current_angles()

    def grab_ball(self,angles, speed=0.2, mirror = False ):
        hand = "RHand"
        if self.effector == "LArm" :
            hand = "LHand"
        self.motion_service.openHand(hand)
        self.move_to_target_joints_angles(angles, speed, mirror)
        time.sleep(0.5)
        self.motion_service.closeHand(hand)
        return self.get_current_angles()

    def move_to_position(self,target_position, speed,axisMask, mirror = False):
        if mirror :
            target_position[1] = -target_position[1]
            target_position[2] = -target_position[2]
            target_position[4] = -target_position[4]
        print("target position is :", target_position)
        self.motion_service.setPosition(self.effector, self.space,target_position, speed, axisMask)
        time.sleep(1)
        print("move : ", self.counter ,"new position after moving :", self.get_current_position())
        self.counter += 1