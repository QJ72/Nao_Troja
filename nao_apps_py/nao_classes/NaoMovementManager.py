import qi
import time

from nao_apps_py.nao_classes.NaoConstants import *

from nao_apps_py.nao_classes.ArmManager import ArmManager

starting_and_end_angles = [0.0583338737487793, 0.1088719367980957, 0.06592011451721191, 0.127363920211792,
                               -0.05526590347290039, 0.39480000734329224]

class NaoMovementManager:
    def __init__(self, session: qi.Session):
        self.motion_service = session.service("ALMotion")
        self.posture_service = session.service("ALRobotPosture")

        self.right_arm_manager = ArmManager(self.motion_service, "RArm")
        self.left_arm_manager = ArmManager(self.motion_service, "LArm")

    def give_joints_positions(self):
        joint_names = self.motion_service.getBodyNames("Body")
        joint_angles = self.motion_service.getAngles(joint_names, True)
        for name, angle in zip(joint_names, joint_angles):
            print(f"joints : {name}, angle : {angle}")

    def relax_nao(self):
        self.motion_service.setStiffnesses("Body",0)

    def current_position(self):
        return self.motion_service.getAngles("Body", True)

    def grab_ball_and_return(self, list_of_joints, target_angles):
        saved_position = self.current_position()

        half_move = [ angle/2 for angle in target_angles]

        self.motion_service.openHand("RHand")
        self.motion_service.setAngles(list_of_joints, half_move,0.1)
        time.sleep(0.5)
        self.motion_service.setAngles(list_of_joints, target_angles,0.1)
        time.sleep(0.5)
        self.motion_service.closeHand("RHand")
        time.sleep(0.5)

        self.motion_service.setAngles("Body", saved_position,0.1)


    def grab_ball_and_return_with_right_arm(self,target_angles, speed = 0.1):
        self.right_arm_manager.move_to_target_joints_angles(starting_and_end_angles, speed)
        time.sleep(0.5)
        self.left_arm_manager.grab_ball(target_angles, speed)
        time.sleep(0.5)
        self.left_arm_manager.move_to_target_joints_angles(starting_and_end_angles, speed)

    def first_set_up_nao_for_grabbing_ball(self):
        self.posture_service.goToPosture("Crouch", 0.2)

        self.right_arm_manager.move_to_target_joints_angles(starting_and_end_angles)
        self.left_arm_manager.move_to_target_joints_angles([1.5, 0.15, 0, 0, 0, 0])
        self.motion_service.setStiffnesses("LArm", 0)

    def set_up_nao_for_grabbing_ball(self):
        self.motion_service.setStiffnesses("LHipPitch", 1)
        self.motion_service.setStiffnesses("RHipPitch", 1)
        self.motion_service.setStiffnesses("RArm", 1)
        self.motion_service.setAngles("LHipPitch", -0.6994619369506836, 0.1)
        self.motion_service.setAngles("RHipPitch", -0.6995458602905273, 0.1)
        self.right_arm_manager.move_to_target_joints_angles(starting_and_end_angles)
        print("inside set_up_nao_for_grabbing_ball")


    def relax_joints(self, joints):
        for joint in joints :
            self.motion_service.setStiffnesses(joint,0)

    def get_current_joints_positions(self, joints):
        joint_positions = self.motion_service.getAngles(joints, True)
        print(joint_positions)
        return joint_positions

    def calibrate_nao(self):
        """
        Nao grab a ball on a predeterminate position in order to make sure
        that everything is in the right place
        """

        #(5.0)
        target_angles = [
            0.6075060367584229,
            0.2868161201477051,
            -0.22093796730041504,
            0.6121079921722412,
            -0.27616190910339355,
            0.9779999852180481
        ]

        print(f"goal_position: {target_angles}")

        self.right_arm_manager.move_to_target_joints_angles(starting_and_end_angles)

        self.motion_service.openHand("RHand")

        self.right_arm_manager.grab_ball(target_angles)

        print(f"end position : {self.right_arm_manager.get_current_angles()}")

        time.sleep(1)
        self.right_arm_manager.move_to_target_joints_angles(starting_and_end_angles)