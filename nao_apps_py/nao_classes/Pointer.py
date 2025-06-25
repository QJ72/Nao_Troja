class Pointer(object):
    def __init__(self, motion_service):
        self.motion_service = motion_service
        set_joins = ["RShoulderPitch", "RShoulderRoll", "RElbowRoll", "RElbowYaw", "RWristYaw"]
        set_coords = [0.2, -0.3, 0.0, 0.0, 0.0]
        motion_service.setAngles(set_joins, set_coords, 0.2)


    def point_in_gaze_direction(self):
        print("point in gaze direction")
        head_yaw = self.motion_service.getAngles("HeadYaw", True)[0]
        head_pitch = self.motion_service.getAngles("HeadPitch", True)[0]

        self.motion_service.setAngles("RShoulderPitch", head_pitch, 0.2)
        self.motion_service.setAngles("RShoulderRoll", head_yaw, 0.2)

        self.motion_service.openHand("RHand")