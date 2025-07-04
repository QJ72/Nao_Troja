

joints_in_RArm = ["RShoulderPitch", "RShoulderRoll", "RElbowYaw" ,"RElbowRoll", "RWristYaw", "RHand"]
joints_in_LArm = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand"]

number_of_joints_in_RArm = len(joints_in_RArm)

starting_and_end_angles = [0.0583338737487793, 0.1088719367980957, 0.06592011451721191, 0.127363920211792, -0.05526590347290039, 0.39480000734329224]



NaoJointsNamesDictionary = {
    "Head" : ["HeadYaw", "HeadPitch"],
    "HeadPitch" : ["HeadPitch"],
    "HeadYaw" : ["HeadYaw"],
    "LArm" : ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll", "LWristYaw", "LHand"],
    "LShoulderPitch" : ["LShoulderPitch"],
    "LShoulderRoll" : ["LShoulderRoll"],
    "LElbowYaw" : ["LElbowYaw"],
    "LElbowRoll" : ["LElbowRoll"],
    "LWristYaw" : ["LWristYaw"],
    "LHand" : ["LHand"],
    "RArm" : ["RShoulderPitch", "RShoulderRoll", "RElbowYaw" ,"RElbowRoll", "RWristYaw", "RHand"],
    "RShoulderPitch" : ["RShoulderPitch"],
    "RShoulderRoll" : ["RShoulderRoll"],
    "RElbowYaw" : ["RElbowYaw"],
    "RElbowRoll" : ["RElbowRoll"],
    "RWristYaw" : ["RWristYaw"],
    "RHand" : ["RHand"],
    "LHipYawPitch" : ["LHipYawPitch"],
    "RHipYawPitch" : ["RHipYawPitch"],
    "LLeg" : ["LHipRoll", "LHipPitch", "LKneePitch", "LAnklePitch", "LAnkleRoll"],
    "LHipPitch" : ["LHipPitch"],
    "LHipRoll" : ["LHipRoll"],
    "LKneePitch" : ["LKneePitch"],
    "LAnklePitch" : ["LAnklePitch"],
    "LAnkleRoll" : ["LAnkleRoll"],
    "RLeg" : ["RHipRoll", "RHipPitch", "RKneePitch", "RAnklePitch", "RAnkleRoll"],
    "RHipPitch": ["RHipPitch"],
    "RHipRoll" : ["RHipRoll"],
    "RKneePitch" : ["RKneePitch"],
    "RAnklePitch" : ["RAnklePitch"],
    "RAnkleRoll" : ["RAnkleRoll"],
}