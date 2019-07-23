# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os

TRAINED_MODELS_PATH = "./resources/trained_models"

class TrackNPredView(object):

    def __init__(self):
        self.trainThread = None

    def setTrainThread(self, trainThread):
        self.trainThread = trainThread


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(1200, 750))
        Dialog.setSizeIncrement(QtCore.QSize(0, 0))
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftLayoyt = QtWidgets.QVBoxLayout()
        self.leftLayoyt.setContentsMargins(5, -1, 5, -1)
        self.leftLayoyt.setSpacing(1)
        self.leftLayoyt.setObjectName("leftLayoyt")
        self.dataset_box = QtWidgets.QGroupBox(Dialog)
        self.dataset_box.setMinimumSize(QtCore.QSize(0, 0))
        self.dataset_box.setMaximumSize(QtCore.QSize(228, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.dataset_box.setFont(font)
        self.dataset_box.setObjectName("dataset_box")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dataset_box)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_13 = QtWidgets.QLabel(self.dataset_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.dataDir = QtWidgets.QLineEdit(self.dataset_box)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.dataDir.setFont(font)
        self.dataDir.setObjectName("dataDir")
        self.verticalLayout_4.addWidget(self.dataDir)
        self.label_14 = QtWidgets.QLabel(self.dataset_box)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_4.addWidget(self.label_14)
        self.framesDir = QtWidgets.QLineEdit(self.dataset_box)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.framesDir.setFont(font)
        self.framesDir.setObjectName("framesDir")
        self.verticalLayout_4.addWidget(self.framesDir)
        self.leftLayoyt.addWidget(self.dataset_box)
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(228, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.trackingFlag = QtWidgets.QCheckBox(self.frame_3)
        self.trackingFlag.setEnabled(True)
        self.trackingFlag.setGeometry(QtCore.QRect(120, 0, 21, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trackingFlag.sizePolicy().hasHeightForWidth())
        self.trackingFlag.setSizePolicy(sizePolicy)
        self.trackingFlag.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.trackingFlag.setFont(font)
        self.trackingFlag.setStyleSheet("QCheckBox::indicator { width:20px; height: 20px; }")
        self.trackingFlag.setIconSize(QtCore.QSize(7, 1))
        self.trackingFlag.setChecked(True)
        self.trackingFlag.setObjectName("trackingFlag")
        self.tracking_box = QtWidgets.QGroupBox(self.frame_3)
        self.tracking_box.setEnabled(True)
        self.tracking_box.setGeometry(QtCore.QRect(0, 0, 233, 171))
        self.tracking_box.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.tracking_box.setFont(font)
        self.tracking_box.setCheckable(False)
        self.tracking_box.setObjectName("tracking_box")
        self.detectionSelector = QtWidgets.QComboBox(self.tracking_box)
        self.detectionSelector.setGeometry(QtCore.QRect(10, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.detectionSelector.setFont(font)
        self.detectionSelector.setObjectName("detectionSelector")
        self.detectionSelector.addItem("")
        self.detectionSelector.addItem("")
        self.label_3 = QtWidgets.QLabel(self.tracking_box)
        self.label_3.setGeometry(QtCore.QRect(20, 75, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.detConfidence = QtWidgets.QLineEdit(self.tracking_box)
        self.detConfidence.setGeometry(QtCore.QRect(140, 75, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.detConfidence.setFont(font)
        self.detConfidence.setObjectName("detConfidence")
        self.nonmaxsupreesionlabel = QtWidgets.QLabel(self.tracking_box)
        self.nonmaxsupreesionlabel.setGeometry(QtCore.QRect(20, 110, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nonmaxsupreesionlabel.setFont(font)
        self.nonmaxsupreesionlabel.setObjectName("nonmaxsupreesionlabel")
        self.nmsInput = QtWidgets.QLineEdit(self.tracking_box)
        self.nmsInput.setGeometry(QtCore.QRect(140, 110, 41, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.nmsInput.setFont(font)
        self.nmsInput.setObjectName("nmsInput")
        self.display = QtWidgets.QCheckBox(self.tracking_box)
        self.display.setGeometry(QtCore.QRect(20, 140, 131, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display.sizePolicy().hasHeightForWidth())
        self.display.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.display.setFont(font)
        self.display.setChecked(True)
        self.display.setObjectName("display")
        self.tracking_box.raise_()
        self.trackingFlag.raise_()
        self.leftLayoyt.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setMaximumSize(QtCore.QSize(228, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.prediction_box1 = QtWidgets.QGroupBox(self.frame)
        self.prediction_box1.setGeometry(QtCore.QRect(0, 30, 231, 134))
        self.prediction_box1.setMinimumSize(QtCore.QSize(0, 0))
        self.prediction_box1.setTitle("")
        self.prediction_box1.setCheckable(False)
        self.prediction_box1.setObjectName("prediction_box1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.prediction_box1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.predictionSelect = QtWidgets.QComboBox(self.prediction_box1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.predictionSelect.setFont(font)
        self.predictionSelect.setObjectName("predictionSelect")
        self.predictionSelect.addItem("")
        self.predictionSelect.addItem("")
        self.predictionSelect.addItem("")
        self.predictionSelect.addItem("")
        self.verticalLayout_5.addWidget(self.predictionSelect)
        self.label_18 = QtWidgets.QLabel(self.prediction_box1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_5.addWidget(self.label_18)

        # self.prediction_box1 = QtWidgets.QGroupBox(self.frame)
        # self.prediction_box1.setGeometry(QtCore.QRect(0, 30, 231, 134))
        # self.prediction_box1.setMinimumSize(QtCore.QSize(0, 0))
        # self.prediction_box1.setTitle("")
        # self.prediction_box1.setCheckable(False)
        # self.prediction_box1.setObjectName("prediction_box1")
        # self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.prediction_box1)
        # self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.modelLoc = QtWidgets.QComboBox(self.prediction_box1)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.modelLoc.setFont(font)
        self.modelLoc.setObjectName("modelLoc")

        # n_models = len(os.listdir("resources/trained_models"))

        if not os.path.exists(TRAINED_MODELS_PATH):
            os.makedirs(TRAINED_MODELS_PATH)

        for model in os.listdir(TRAINED_MODELS_PATH):
            self.modelLoc.addItem(os.path.join(TRAINED_MODELS_PATH, model))

        self.verticalLayout_5.addWidget(self.modelLoc)


        # self.label_18 = QtWidgets.QLabel(self.prediction_box1)
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # self.label_18.setFont(font)
        # self.label_18.setObjectName("label_18")
        # self.verticalLayout_5.addWidget(self.label_18)

        # self.modelLoc = QtWidgets.QLineEdit(self.prediction_box1)
        # self.modelLoc.setObjectName("modelLoc")
        self.verticalLayout_5.addWidget(self.modelLoc)

        self.maneuvers = QtWidgets.QCheckBox(self.prediction_box1)
        self.maneuvers.setObjectName("maneuvers")
        self.verticalLayout_5.addWidget(self.maneuvers)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 231, 28))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(10, 25, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.predictionFlag = QtWidgets.QCheckBox(self.frame)
        self.predictionFlag.setEnabled(True)
        self.predictionFlag.setGeometry(QtCore.QRect(140, 10, 21, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.predictionFlag.sizePolicy().hasHeightForWidth())
        self.predictionFlag.setSizePolicy(sizePolicy)
        self.predictionFlag.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.predictionFlag.setFont(font)
        self.predictionFlag.setStyleSheet("QCheckBox::indicator { width:20px; height: 20px; }")
        self.predictionFlag.setIconSize(QtCore.QSize(7, 1))
        self.predictionFlag.setChecked(True)
        self.predictionFlag.setObjectName("predictionFlag")
        self.leftLayoyt.addWidget(self.frame)
        self.horizontalLayout.addLayout(self.leftLayoyt)
        self.rightLayout = QtWidgets.QVBoxLayout()
        self.rightLayout.setContentsMargins(5, -1, 1, -1)
        self.rightLayout.setSpacing(1)
        self.rightLayout.setObjectName("rightLayout")
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.prediction_box2 = QtWidgets.QGroupBox(self.frame_4)
        self.prediction_box2.setGeometry(QtCore.QRect(0, 20, 231, 335))
        self.prediction_box2.setMinimumSize(QtCore.QSize(0, 0))
        self.prediction_box2.setTitle("")
        self.prediction_box2.setObjectName("prediction_box2")
        self.label_17 = QtWidgets.QLabel(self.prediction_box2)
        self.label_17.setGeometry(QtCore.QRect(10, 300, 91, 21))
        self.label_17.setObjectName("label_17")
        self.learningRate = QtWidgets.QLineEdit(self.prediction_box2)
        self.learningRate.setGeometry(QtCore.QRect(130, 300, 41, 23))
        self.learningRate.setObjectName("learningRate")
        self.trainEpochs = QtWidgets.QLineEdit(self.prediction_box2)
        self.trainEpochs.setGeometry(QtCore.QRect(140, 60, 41, 23))
        self.trainEpochs.setObjectName("trainEpochs")
        self.batchSize = QtWidgets.QLineEdit(self.prediction_box2)
        self.batchSize.setGeometry(QtCore.QRect(140, 90, 41, 23))
        self.batchSize.setObjectName("batchSize")
        self.optimizer = QtWidgets.QComboBox(self.prediction_box2)
        self.optimizer.setGeometry(QtCore.QRect(10, 170, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.optimizer.setFont(font)
        self.optimizer.setObjectName("optimizer")
        self.optimizer.addItem("")
        self.optimizer.addItem("")
        self.optimizer.addItem("")
        self.label_16 = QtWidgets.QLabel(self.prediction_box2)
        self.label_16.setGeometry(QtCore.QRect(10, 150, 81, 21))
        self.label_16.setObjectName("label_16")
        self.pretrainEpochs = QtWidgets.QLineEdit(self.prediction_box2)
        self.pretrainEpochs.setGeometry(QtCore.QRect(140, 30, 41, 23))
        self.pretrainEpochs.setObjectName("pretrainEpochs")
        self.label_8 = QtWidgets.QLabel(self.prediction_box2)
        self.label_8.setGeometry(QtCore.QRect(10, 120, 81, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.prediction_box2)
        self.label_9.setGeometry(QtCore.QRect(10, 90, 101, 20))
        self.label_9.setObjectName("label_9")
        self.dropout = QtWidgets.QLineEdit(self.prediction_box2)
        self.dropout.setGeometry(QtCore.QRect(140, 120, 41, 23))
        self.dropout.setObjectName("dropout")
        self.label_6 = QtWidgets.QLabel(self.prediction_box2)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 101, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.prediction_box2)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 101, 20))
        self.label_7.setObjectName("label_7")
        self.pretrainLoss = QtWidgets.QComboBox(self.prediction_box2)
        self.pretrainLoss.setGeometry(QtCore.QRect(10, 220, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pretrainLoss.setFont(font)
        self.pretrainLoss.setObjectName("pretrainLoss")
        self.pretrainLoss.addItem("")
        self.pretrainLoss.addItem("")
        self.label_19 = QtWidgets.QLabel(self.prediction_box2)
        self.label_19.setGeometry(QtCore.QRect(10, 200, 81, 21))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.prediction_box2)
        self.label_20.setGeometry(QtCore.QRect(10, 250, 81, 21))
        self.label_20.setObjectName("label_20")
        self.trainLoss = QtWidgets.QComboBox(self.prediction_box2)
        self.trainLoss.setGeometry(QtCore.QRect(10, 270, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.trainLoss.setFont(font)
        self.trainLoss.setObjectName("trainLoss")
        self.trainLoss.addItem("")
        self.trainLoss.addItem("")
        self.label_5 = QtWidgets.QLabel(self.prediction_box2)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.rightLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(Dialog)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setObjectName("frame_5")
        self.rightLayout.addWidget(self.frame_5)
        self.rightLayout.setStretch(0, 2)
        self.rightLayout.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.rightLayout)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ProgressBox = QtWidgets.QGroupBox(Dialog)
        self.ProgressBox.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.ProgressBox.setFont(font)
        self.ProgressBox.setTitle("")
        self.ProgressBox.setFlat(True)
        self.ProgressBox.setCheckable(False)
        self.ProgressBox.setChecked(False)
        self.ProgressBox.setObjectName("ProgressBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ProgressBox)
        self.verticalLayout_3.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.ProgressBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.frame_2 = QtWidgets.QFrame(self.ProgressBox)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3.addWidget(self.frame_2)
        self.cuda = QtWidgets.QCheckBox(self.ProgressBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cuda.setFont(font)
        self.cuda.setStyleSheet("QCheckBox::indicator { width:20px; height: 20px; }")
        self.cuda.setChecked(True)
        self.cuda.setObjectName("cuda")
        self.horizontalLayout_3.addWidget(self.cuda)
        self.trainButton = QtWidgets.QPushButton(self.ProgressBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.trainButton.setFont(font)
        self.trainButton.setDefault(True)
        self.trainButton.setObjectName("trainButton")
        self.horizontalLayout_3.addWidget(self.trainButton)
        self.evalButton = QtWidgets.QPushButton(self.ProgressBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.evalButton.setFont(font)
        self.evalButton.setAutoDefault(False)
        self.evalButton.setObjectName("evalButton")
        self.horizontalLayout_3.addWidget(self.evalButton)
        self.clearButton = QtWidgets.QPushButton(self.ProgressBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clearButton.setFont(font)
        self.clearButton.setAutoDefault(False)
        self.clearButton.setObjectName("clearButton")
        self.horizontalLayout_3.addWidget(self.clearButton)
        self.stopButton = QtWidgets.QPushButton(self.ProgressBox)
        self.stopButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stopButton.setFont(font)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_3.addWidget(self.stopButton)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(3, 2)
        self.horizontalLayout_3.setStretch(4, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topBarLabel = QtWidgets.QLabel(self.ProgressBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.topBarLabel.setFont(font)
        self.topBarLabel.setText("")
        self.topBarLabel.setObjectName("topBarLabel")
        self.verticalLayout_2.addWidget(self.topBarLabel)
        self.topBar = QtWidgets.QProgressBar(self.ProgressBox)
        self.topBar.setProperty("value", 0)
        self.topBar.setObjectName("topBar")
        self.verticalLayout_2.addWidget(self.topBar)
        self.botBarLabel = QtWidgets.QLabel(self.ProgressBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.botBarLabel.setFont(font)
        self.botBarLabel.setText("")
        self.botBarLabel.setObjectName("botBarLabel")
        self.verticalLayout_2.addWidget(self.botBarLabel)
        self.botBar = QtWidgets.QProgressBar(self.ProgressBox)
        self.botBar.setProperty("value", 0)
        self.botBar.setObjectName("botBar")
        self.verticalLayout_2.addWidget(self.botBar)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 2)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 5)
        self.verticalLayout.addWidget(self.ProgressBox)
        self.verticalLayout.setStretch(0, 9)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.canvaslLayout = QtWidgets.QVBoxLayout()
        self.canvaslLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.canvaslLayout.setSpacing(5)
        self.canvaslLayout.setObjectName("canvaslLayout")
        self.canvas = QtWidgets.QTextBrowser(Dialog)
        self.canvas.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.canvas.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.canvas.setProperty("tabletTracking", False)
        self.canvas.setObjectName("canvas")
        self.canvaslLayout.addWidget(self.canvas)
        self.imgDisplay = QtWidgets.QLabel(Dialog)
        self.imgDisplay.setText("")
        self.imgDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.imgDisplay.setObjectName("imgDisplay")
        self.canvaslLayout.addWidget(self.imgDisplay)
        self.canvaslLayout.setStretch(0, 4)
        self.canvaslLayout.setStretch(1, 7)
        self.horizontalLayout_2.addLayout(self.canvaslLayout)
        self.horizontalLayout_2.setStretch(0, 18)
        self.horizontalLayout_2.setStretch(1, 25)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TrackNPred"))
        self.dataset_box.setTitle(_translate("Dialog", "Dataset"))
        self.label_13.setText(_translate("Dialog", "Dir"))
        self.dataDir.setText(_translate("Dialog", "resources/data/TRAF"))
        self.label_14.setText(_translate("Dialog", "Frames Dir"))
        self.framesDir.setText(_translate("Dialog", "frames"))
        self.trackingFlag.setText(_translate("Dialog", "CheckBox"))
        self.tracking_box.setTitle(_translate("Dialog", "Tracking "))
        self.detectionSelector.setItemText(0, _translate("Dialog", "YOLO")) # self.detectionSelector.setItemText(1, _translate("Dialog", "Mask r-cnn"))
        self.detectionSelector.setItemText(1, _translate("Dialog", "MASK")) # self.detectionSelector.setItemText(1, _translate("Dialog", "Mask r-cnn"))
        self.label_3.setText(_translate("Dialog", "Confidence"))
        self.detConfidence.setText(_translate("Dialog", ".8"))
        self.nonmaxsupreesionlabel.setText(_translate("Dialog", "NMS"))
        self.nmsInput.setText(_translate("Dialog", ".4"))
        self.display.setText(_translate("Dialog", "Display"))
        self.predictionSelect.setItemText(0, _translate("Dialog", "Traphic"))
        self.predictionSelect.setItemText(1, _translate("Dialog", "Social GAN"))
        self.predictionSelect.setItemText(2, _translate("Dialog", "Social-LSTM"))
        self.predictionSelect.setItemText(3, _translate("Dialog", "Social Conv"))
        self.label_18.setText(_translate("Dialog", "Model location"))
        # self.modelLoc.setText(_translate("Dialog", "model/Prediction/trained_models"))
        self.maneuvers.setText(_translate("Dialog", "Maneuvers"))
        self.label_2.setText(_translate("Dialog", "Trajectory"))
        self.label_10.setText(_translate("Dialog", "Prediction"))
        self.predictionFlag.setText(_translate("Dialog", "CheckBox"))
        self.label_4.setText(_translate("Dialog", "Trajectory Prediction"))
        self.label_17.setText(_translate("Dialog", "Learning Rate:"))
        self.learningRate.setText(_translate("Dialog", "1e-3"))
        self.trainEpochs.setText(_translate("Dialog", "10"))
        self.batchSize.setText(_translate("Dialog", "128"))
        self.optimizer.setItemText(0, _translate("Dialog", "Adam"))
        self.optimizer.setItemText(1, _translate("Dialog", "Adagrad"))
        self.optimizer.setItemText(2, _translate("Dialog", "SGD"))
        self.label_16.setText(_translate("Dialog", "Optimizer"))
        self.pretrainEpochs.setText(_translate("Dialog", "6"))
        self.label_8.setText(_translate("Dialog", "Dropout"))
        self.label_9.setText(_translate("Dialog", "Batch size"))
        self.dropout.setText(_translate("Dialog", ".5"))
        self.label_6.setText(_translate("Dialog", "train epochs"))
        self.label_7.setText(_translate("Dialog", "Pre-train epochs"))
        self.pretrainLoss.setItemText(0, _translate("Dialog", "MSE"))
        self.pretrainLoss.setItemText(1, _translate("Dialog", "NLL"))
        self.label_19.setText(_translate("Dialog", "Pretrain loss"))
        self.label_20.setText(_translate("Dialog", "Train loss"))
        self.trainLoss.setItemText(0, _translate("Dialog", "NLL"))
        self.trainLoss.setItemText(1, _translate("Dialog", "MSE"))
        self.label_5.setText(_translate("Dialog", "Training settings"))
        self.label_11.setText(_translate("Dialog", "Progress"))
        self.cuda.setText(_translate("Dialog", "GPU"))
        self.trainButton.setText(_translate("Dialog", "Train"))
        self.evalButton.setText(_translate("Dialog", "Evaluate"))
        self.clearButton.setText(_translate("Dialog", "Clear"))
        self.stopButton.setText(_translate("Dialog", "Stop"))
        self.canvas.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.SF NS Text\'; font-size:13pt;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = TrackNPredView()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

