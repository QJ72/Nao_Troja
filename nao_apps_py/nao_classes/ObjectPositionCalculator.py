import numpy as np

FRAME_TORSO = 0

class ObjectPositionCalculator:
    def __init__(self, motion_service, video_service, space_frame = FRAME_TORSO):
        self.motion_service = motion_service
        self.video_service = video_service
        self.space = space_frame
    
    def getCurrentCamera(self):
        current_camera = self.video_service.getActiveCamera()

        if current_camera == 0 :
            return "CameraTop"
        elif current_camera == 1 :
            return "CameraBottom"

        return "exit"

    def getPositionObject(self, depth):

        theta = self.motion_service.getAngles("HeadPitch",True)[0]
        phi = self.motion_service.getAngles("HeadYaw", True)[0]

        current_camera = self.getCurrentCamera()

        head_position = self.motion_service.getPosition(self.currentCamera, self.space, True)

        x = depth*np.sin(theta)*np.cos(phi) + head_position[0]
        y = depth*np.sin(theta)*np.sin(phi) + head_position[1]
        z = depth*np.cos(theta) + head_position[2]