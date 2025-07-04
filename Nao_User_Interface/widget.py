# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir("../nao_apps_py/")

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from ui_form import Ui_Widget

from itertools import chain
from decimal import Decimal
import torch

from nao_apps_py.nao_classes.ConnectionToNaoManager import ConnectionToNaoManager
from nao_apps_py.nao_classes.NaoDatasetGenerator import NaoDatasetGenerator
from nao_apps_py.nao_classes.NaoTrainer import NaoTrainer
from nao_apps_py.nao_classes.NaoMovementManager import NaoMovementManager
from nao_apps_py.nao_classes.ImageCollector import ImageCollector
from nao_apps_py.nao_classes.NaoVisionManager import NaoVisionManager
from nao_apps_py.nao_classes.JointAnglesPredictor import JointAnglesPredictor
from nao_apps_py.nao_classes.NaoConstants import *

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.session = None
        self.dataset_generator = None
        self.trainer = None
        self.nao_movement_manager = None
        self.nao_vision_manager = None
        self.image_collector = None
        self.model = JointAnglesPredictor()

        self.connection_manager = ConnectionToNaoManager()

        self.ui.pushButtonConnectToNao.clicked.connect(self.connection_button_clicked)
        self.ui.pushButtonDataset.clicked.connect(self.dataset_button_clicked)
        self.ui.pushButtonInitialisedTraining.clicked.connect(self.start_training_clicked)
        self.ui.pushButtonAction.clicked.connect(self.execute_action)
        self.ui.pushButtonGrabBallWithModel.clicked.connect(self.on_grab_ball_with_model_clicked)
        self.ui.pushButtonCollectImages.clicked.connect(self.collect_image_clicked)


    def connection_button_clicked(self):
        self.session = self.connection_manager.connection_to_nao(self.ui.plainTextEditHost.toPlainText(),self.ui.plainTextEditPort.toPlainText())
        if self.session is not None :
            self.ui.checkBoxConnection.setChecked(True)
            self.nao_movement_manager = NaoMovementManager(self.session)
            self.nao_vision_manager = NaoVisionManager(self.session)
            self.ui.pushButtonAction.setEnabled(True)
            self.enable_when_connection_and_dataset_ready()
            self.nao_vision_manager.get_video_service().setActiveCamera(self.nao_vision_manager.get_video_client(), 1)
            return True
        self.ui.checkBoxConnection.setChecked(False)
        self.ui.pushButtonAction.setEnabled(False)
        self.enable_when_connection_and_dataset_ready()

        return False

    def dataset_button_clicked(self):
        self.dataset_generator = NaoDatasetGenerator(
            self.ui.plainTextEditDatasetName.toPlainText(),
            self.ui.plainTextEditJsonFile.toPlainText(),
            self.ui.plainTextEditDatasetParentFolder.toPlainText(),
            self.joints_lists()
        )

        self.ui.checkBoxDataset.setChecked(True)
        self.ui.pushButtonInitialisedTraining.setEnabled(True)

        self.enable_when_connection_and_dataset_ready()

        self.ui.plainTextEditSetOfJoints.setPlainText( ",".join(self.dataset_generator.get_joints_names()) )

        return self.dataset_generator

    def start_training_clicked(self):
        self.trainer = NaoTrainer(
            dataset_name = self.ui.plainTextEditDatasetName.toPlainText(),
            json_file = self.ui.plainTextEditJsonFile.toPlainText(),
            neural_network_dir = self.ui.plainTextEditNeuralNetworkDirectory.toPlainText(),
            dataset_parent_folder = self.ui.plainTextEditDatasetParentFolder.toPlainText()
        )
        self.trainer.set_model_name(self.ui.plainTextEditModelName.toPlainText())
        self.trainer.load_data()

        print(f"number_of_joints {self.dataset_generator.get_number_of_joints()}")
        self.trainer.create_model(self.dataset_generator.get_number_of_joints())

        self.ui.checkBoxTraining.setChecked(True)

        try :
            self.trainer.train( int(self.ui.plainTextEditEpochs.toPlainText()) )
        except Exception as e:
            print(f"error : {e}")
            self.ui.checkBoxTraining.setChecked(False)

        return self.trainer

    def execute_action(self):
        match self.ui.comboBoxSelectAction.currentIndex():
            case 0:
                self.nao_movement_manager.first_set_up_nao_for_grabbing_ball()
            case 1:
                self.nao_movement_manager.calibrate_nao()
            case 2:
                self.nao_movement_manager.relax_nao()
            case 3:
                self.nao_movement_manager.give_joints_positions()
            case 4:
                self.nao_movement_manager.relax_joints(self.joints_lists())
            case 5:
                self.nao_movement_manager.set_up_nao_for_grabbing_ball()
            case 6:
                self.nao_movement_manager.get_current_joints_positions(self.joints_lists())
            case 7:
                self.nao_movement_manager.grab_ball_and_return(self.joints_lists(), self.target_angles())


    def enable_when_connection_and_dataset_ready(self):
        if self.ui.checkBoxConnection.isChecked() and self.ui.checkBoxDataset.isChecked():
            self.ui.pushButtonCollectImages.setEnabled(True)
            self.ui.pushButtonGrabBallWithModel.setEnabled(True)
            return True
        self.ui.pushButtonCollectImages.setEnabled(False)
        self.ui.pushButtonGrabBallWithModel.setEnabled(False)
        return False

    def joints_lists(self):
        joints_list = self.ui.plainTextEditSetOfJoints.toPlainText().strip()
        joints_list = joints_list.split(",")
        joints_list = [NaoJointsNamesDictionary[joint] for joint in joints_list ]
        joints_list = list(chain.from_iterable(joints_list))

        return joints_list

    def target_angles(self):
        target_angles = self.ui.plainTextEditTargetAngles.toPlainText().strip()
        target_angles = target_angles.split(",")
        target_angles = [float(Decimal(angle)) for angle in target_angles]

        return target_angles


    def collect_image_clicked(self):
        try :
            target_angles = self.target_angles()

            self.image_collector = ImageCollector(
                self.nao_vision_manager.get_video_service(),
                self.nao_vision_manager.get_video_client(),
               self.joints_lists(),
                self.ui.plainTextEditDatasetName.toPlainText()
            )

            if len(target_angles) != len(self.joints_lists()) :
                print("error : target must be the same value as the joints)")
                return None


            self.image_collector.collect_images(
                int(self.ui.plainTextEditNumberOfImages.toPlainText()),
                self.ui.plainTextEditImageName.toPlainText(),
                target_angles,
                for_training = self.ui.checkBoxCollectImage.isChecked()
            )
            return True
        except Exception as e :
            print(f"error : {e}")
            return None

    def on_grab_ball_with_model_clicked(self):
        self.model = JointAnglesPredictor()
        self.model.load_state_dict(torch.load(f"{self.ui.plainTextEditNeuralNetworkDirectory.toPlainText()}/{self.ui.plainTextEditModelName.toPlainText()}"))
        print(f"model : {self.model}")
        self.model.eval()

        image = self.image_collector.get_new_image_from_nao()
        if image is None :
            print("Error : image not taken by the camera")
            return False

        target_angles = self.model.predict_joints(image).tolist()
        self.nao_movement_manager.grab_ball_and_return(self.joints_lists(),target_angles)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
