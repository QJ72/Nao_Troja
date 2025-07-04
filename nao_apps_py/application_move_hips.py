import qi
import utilities
from nao_apps_py.nao_classes.ConnectionToNaoManager import ConnectionToNaoManager

if __name__ == '__main__':
    #default url : tcp://127.0.0.1:9559
    connection = ConnectionToNaoManager()
    session = connection.connection_to_nao("10.11.45.211","9559")
    motion_service = session.service("ALMotion")
    posture = session.service("ALRobotPosture")

    hip_joints = ["LHipPitch","RHipPitch"]
    joint_values = [-1.3,-1.3]

    motion_service.setAngles(hip_joints, joint_values,0.1)