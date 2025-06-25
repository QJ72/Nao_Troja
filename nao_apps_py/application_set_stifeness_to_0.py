import qi
import utilities
from nao_classes.ArmManager import ArmManager

if __name__ == '__main__':
    #default url : tcp://127.0.0.1:9559
    session = qi.Session()
    session.connect("tcp://10.11.45.211:9559")
    motion_service = session.service("ALMotion")
    motion_service.setStiffnesses("RArm", 0)
    motion_service.setStiffnesses("LArm", 0)

    left_arm_manager = ArmManager(motion_service,"LArm")
    right_arm_manager = ArmManager(motion_service,"RArm")
    motion_service.setStiffnesses("LLeg",0)
    motion_service.setStiffnesses("RLeg",0)

    print(right_arm_manager.get_current_angles())

    print(left_arm_manager.effector)