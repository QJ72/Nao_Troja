# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setEnabled(True)
        Widget.resize(900, 715)
        self.gridLayoutWidget = QWidget(Widget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(50, 10, 241, 204))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.checkBoxConnection = QCheckBox(self.gridLayoutWidget)
        self.checkBoxConnection.setObjectName(u"checkBoxConnection")
        self.checkBoxConnection.setEnabled(False)
        self.checkBoxConnection.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout.addWidget(self.checkBoxConnection, 2, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.pushButtonConnectToNao = QPushButton(self.gridLayoutWidget)
        self.pushButtonConnectToNao.setObjectName(u"pushButtonConnectToNao")

        self.gridLayout.addWidget(self.pushButtonConnectToNao, 3, 0, 1, 1)

        self.plainTextEditHost = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEditHost.setObjectName(u"plainTextEditHost")

        self.gridLayout.addWidget(self.plainTextEditHost, 0, 1, 1, 1)

        self.plainTextEditPort = QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEditPort.setObjectName(u"plainTextEditPort")

        self.gridLayout.addWidget(self.plainTextEditPort, 1, 1, 1, 1)

        self.gridLayoutWidget_2 = QWidget(Widget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(440, 10, 357, 356))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.plainTextEditDatasetParentFolder = QPlainTextEdit(self.gridLayoutWidget_2)
        self.plainTextEditDatasetParentFolder.setObjectName(u"plainTextEditDatasetParentFolder")

        self.gridLayout_2.addWidget(self.plainTextEditDatasetParentFolder, 2, 1, 1, 1)

        self.pushButtonDataset = QPushButton(self.gridLayoutWidget_2)
        self.pushButtonDataset.setObjectName(u"pushButtonDataset")

        self.gridLayout_2.addWidget(self.pushButtonDataset, 5, 0, 1, 1)

        self.checkBoxDataset = QCheckBox(self.gridLayoutWidget_2)
        self.checkBoxDataset.setObjectName(u"checkBoxDataset")
        self.checkBoxDataset.setEnabled(False)

        self.gridLayout_2.addWidget(self.checkBoxDataset, 4, 1, 1, 1)

        self.plainTextEditDatasetName = QPlainTextEdit(self.gridLayoutWidget_2)
        self.plainTextEditDatasetName.setObjectName(u"plainTextEditDatasetName")

        self.gridLayout_2.addWidget(self.plainTextEditDatasetName, 0, 1, 1, 1)

        self.plainTextEditJsonFile = QPlainTextEdit(self.gridLayoutWidget_2)
        self.plainTextEditJsonFile.setObjectName(u"plainTextEditJsonFile")

        self.gridLayout_2.addWidget(self.plainTextEditJsonFile, 1, 1, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)

        self.plainTextEditSetOfJoints = QPlainTextEdit(self.gridLayoutWidget_2)
        self.plainTextEditSetOfJoints.setObjectName(u"plainTextEditSetOfJoints")

        self.gridLayout_2.addWidget(self.plainTextEditSetOfJoints, 3, 1, 1, 1)

        self.gridLayoutWidget_3 = QWidget(Widget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(40, 350, 361, 312))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.plainTextEditModelName = QPlainTextEdit(self.gridLayoutWidget_3)
        self.plainTextEditModelName.setObjectName(u"plainTextEditModelName")

        self.gridLayout_3.addWidget(self.plainTextEditModelName, 1, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 4, 0, 1, 1)

        self.plainTextEditNeuralNetworkDirectory = QPlainTextEdit(self.gridLayoutWidget_3)
        self.plainTextEditNeuralNetworkDirectory.setObjectName(u"plainTextEditNeuralNetworkDirectory")

        self.gridLayout_3.addWidget(self.plainTextEditNeuralNetworkDirectory, 0, 1, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)

        self.plainTextEditEpochs = QPlainTextEdit(self.gridLayoutWidget_3)
        self.plainTextEditEpochs.setObjectName(u"plainTextEditEpochs")

        self.gridLayout_3.addWidget(self.plainTextEditEpochs, 3, 1, 1, 1)

        self.pushButtonInitialisedTraining = QPushButton(self.gridLayoutWidget_3)
        self.pushButtonInitialisedTraining.setObjectName(u"pushButtonInitialisedTraining")
        self.pushButtonInitialisedTraining.setEnabled(False)

        self.gridLayout_3.addWidget(self.pushButtonInitialisedTraining, 5, 0, 1, 1)

        self.checkBoxTraining = QCheckBox(self.gridLayoutWidget_3)
        self.checkBoxTraining.setObjectName(u"checkBoxTraining")
        self.checkBoxTraining.setEnabled(False)

        self.gridLayout_3.addWidget(self.checkBoxTraining, 4, 1, 1, 1)

        self.pushButtonGrabBallWithModel = QPushButton(self.gridLayoutWidget_3)
        self.pushButtonGrabBallWithModel.setObjectName(u"pushButtonGrabBallWithModel")
        self.pushButtonGrabBallWithModel.setEnabled(False)

        self.gridLayout_3.addWidget(self.pushButtonGrabBallWithModel, 2, 0, 1, 1)

        self.gridLayoutWidget_4 = QWidget(Widget)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 220, 203, 80))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.comboBoxSelectAction = QComboBox(self.gridLayoutWidget_4)
        self.comboBoxSelectAction.addItem("")
        self.comboBoxSelectAction.addItem("")
        self.comboBoxSelectAction.addItem("")
        self.comboBoxSelectAction.addItem("")
        self.comboBoxSelectAction.addItem("")
        self.comboBoxSelectAction.addItem("")
        self.comboBoxSelectAction.addItem("")
        self.comboBoxSelectAction.addItem("")
        self.comboBoxSelectAction.setObjectName(u"comboBoxSelectAction")

        self.gridLayout_4.addWidget(self.comboBoxSelectAction, 0, 0, 1, 1)

        self.pushButtonAction = QPushButton(self.gridLayoutWidget_4)
        self.pushButtonAction.setObjectName(u"pushButtonAction")
        self.pushButtonAction.setEnabled(False)

        self.gridLayout_4.addWidget(self.pushButtonAction, 1, 0, 1, 1)

        self.gridLayoutWidget_5 = QWidget(Widget)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(520, 435, 281, 280))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.plainTextEditImageName = QPlainTextEdit(self.gridLayoutWidget_5)
        self.plainTextEditImageName.setObjectName(u"plainTextEditImageName")

        self.gridLayout_5.addWidget(self.plainTextEditImageName, 2, 1, 1, 1)

        self.pushButtonCollectImages = QPushButton(self.gridLayoutWidget_5)
        self.pushButtonCollectImages.setObjectName(u"pushButtonCollectImages")
        self.pushButtonCollectImages.setEnabled(False)

        self.gridLayout_5.addWidget(self.pushButtonCollectImages, 5, 0, 1, 1)

        self.checkBoxCollectImage = QCheckBox(self.gridLayoutWidget_5)
        self.checkBoxCollectImage.setObjectName(u"checkBoxCollectImage")
        self.checkBoxCollectImage.setAutoFillBackground(False)
        self.checkBoxCollectImage.setChecked(True)

        self.gridLayout_5.addWidget(self.checkBoxCollectImage, 4, 1, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_5)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_5.addWidget(self.label_13, 2, 0, 1, 1)

        self.plainTextEditNumberOfImages = QPlainTextEdit(self.gridLayoutWidget_5)
        self.plainTextEditNumberOfImages.setObjectName(u"plainTextEditNumberOfImages")

        self.gridLayout_5.addWidget(self.plainTextEditNumberOfImages, 1, 1, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_5)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_5.addWidget(self.label_14, 4, 0, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_5)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_5.addWidget(self.label_12, 1, 0, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_5)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_5.addWidget(self.label_15, 3, 0, 1, 1)

        self.plainTextEditTargetAngles = QPlainTextEdit(self.gridLayoutWidget_5)
        self.plainTextEditTargetAngles.setObjectName(u"plainTextEditTargetAngles")

        self.gridLayout_5.addWidget(self.plainTextEditTargetAngles, 3, 1, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"HOST :", None))
        self.checkBoxConnection.setText("")
        self.label_2.setText(QCoreApplication.translate("Widget", u"PORT :", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Connexion to Nao :", None))
        self.pushButtonConnectToNao.setText(QCoreApplication.translate("Widget", u"Connect to Nao", None))
        self.plainTextEditHost.setPlainText(QCoreApplication.translate("Widget", u"10.11.45.211", None))
        self.plainTextEditPort.setPlainText(QCoreApplication.translate("Widget", u"9559", None))
        self.plainTextEditDatasetParentFolder.setPlainText(QCoreApplication.translate("Widget", u"datasets", None))
        self.pushButtonDataset.setText(QCoreApplication.translate("Widget", u"Create/Load", None))
        self.checkBoxDataset.setText("")
        self.plainTextEditDatasetName.setPlainText(QCoreApplication.translate("Widget", u"dummy dataset", None))
        self.plainTextEditJsonFile.setPlainText(QCoreApplication.translate("Widget", u"annotations.json", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Json file :", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Name of Dataset :", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Dataset ready :", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"Dataset Parent Directory :", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"Set of joints :", None))
        self.plainTextEditSetOfJoints.setPlainText(QCoreApplication.translate("Widget", u"RArm", None))
        self.plainTextEditModelName.setPlainText(QCoreApplication.translate("Widget", u"dummy_model.pth", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"Training :", None))
        self.plainTextEditNeuralNetworkDirectory.setPlainText(QCoreApplication.translate("Widget", u"neural_network", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"Neural Network Directory : ", None))
        self.label_16.setText(QCoreApplication.translate("Widget", u"Model Name :", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"Number of epoch :", None))
        self.plainTextEditEpochs.setPlainText(QCoreApplication.translate("Widget", u"10", None))
        self.pushButtonInitialisedTraining.setText(QCoreApplication.translate("Widget", u"Start training", None))
        self.checkBoxTraining.setText("")
        self.pushButtonGrabBallWithModel.setText(QCoreApplication.translate("Widget", u"Grab Ball with Model", None))
        self.comboBoxSelectAction.setItemText(0, QCoreApplication.translate("Widget", u"First Set Up", None))
        self.comboBoxSelectAction.setItemText(1, QCoreApplication.translate("Widget", u"Calibrate Nao", None))
        self.comboBoxSelectAction.setItemText(2, QCoreApplication.translate("Widget", u"Relax Nao", None))
        self.comboBoxSelectAction.setItemText(3, QCoreApplication.translate("Widget", u"Get positions of the joints", None))
        self.comboBoxSelectAction.setItemText(4, QCoreApplication.translate("Widget", u"Relax Current Joints", None))
        self.comboBoxSelectAction.setItemText(5, QCoreApplication.translate("Widget", u"Set Up", None))
        self.comboBoxSelectAction.setItemText(6, QCoreApplication.translate("Widget", u"Get Positions current joints", None))
        self.comboBoxSelectAction.setItemText(7, QCoreApplication.translate("Widget", u"Grab Ball", None))

        self.pushButtonAction.setText(QCoreApplication.translate("Widget", u"Execute Action", None))
        self.plainTextEditImageName.setPlainText(QCoreApplication.translate("Widget", u"dummy_image", None))
        self.pushButtonCollectImages.setText(QCoreApplication.translate("Widget", u"Collect Images", None))
        self.checkBoxCollectImage.setText("")
        self.label_13.setText(QCoreApplication.translate("Widget", u"Image Name", None))
        self.plainTextEditNumberOfImages.setPlainText(QCoreApplication.translate("Widget", u"100", None))
        self.label_14.setText(QCoreApplication.translate("Widget", u"For Training", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"Number of Images :", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"Target Angles", None))
    # retranslateUi

