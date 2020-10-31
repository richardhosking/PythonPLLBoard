"""
# -*- coding: utf-8 -*-
# RF Generator Form implementation generated from reading ui file 'RFGenerator.ui'
#
# Created by: PyQt5 UI code generator 5.10.1 
# from UI created in XML using Qt Designer 
# Widgets, signal/slot definition, layouts and text properties set in Qt Designer
# 
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

# Thread Class
from RFGenThreadClass import Worker

# Class definition for main window object inherits from QMainWindow class 
class Ui_MainWindow(QMainWindow):
    # Class variable to indicate which data is being edited by Keypad
    currentData = []
    
    # error messages from data validation routine for status label
    errorMessage = ''
    
    # signal handlers (slots) abstracted to a separate file - not allowed to use * it seems
    from RFGenHandlers import keypadEnter, setFocus, keypadClear, keypadBack, updatePLLPower
    from RFGenHandlers import validateSingleFreq, validateSweep, manageSweep, keypadUpdate

    # Constructor for Ui_MainWindow class
    def __init__(self, *args, **kwargs):
        # super makes all the methods and attributes of the superclass QMainWindow available in Ui_MainWindow
        # the argument string (*args, **kwargs) allows any arbitrary arguments to be passed to the __init__ function 
        super(QMainWindow, self).__init__(*args, **kwargs)
        
        # Setup thread for sweep generator if required 
        self.sweepThread = Worker()

        # Setup GUI
        self.setupUi(self)
    
                   
    # Code generated from Qt Designer via Riverbank Computing XML => python tool
    # slightly modified
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(200, 120))
        font = QtGui.QFont()
        font.setPointSize(24)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(200, 150))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # Keypad frame 
        self.Keypad = QtWidgets.QFrame(self.centralwidget)
        self.Keypad.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Keypad.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Keypad.setObjectName("Keypad")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.Keypad)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.keyBack = QtWidgets.QPushButton(self.Keypad)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.keyBack.setFont(font)
        self.keyBack.setObjectName("keyBack")
        self.gridLayout_2.addWidget(self.keyBack, 3, 2, 1, 1)
        self.key5 = QtWidgets.QPushButton(self.Keypad)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key5.setFont(font)
        self.key5.setObjectName("key5")
        self.gridLayout_2.addWidget(self.key5, 1, 1, 1, 1)
        self.key3 = QtWidgets.QPushButton(self.Keypad)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setKerning(False)
        self.key3.setFont(font)
        self.key3.setObjectName("key3")
        self.gridLayout_2.addWidget(self.key3, 0, 2, 1, 1)
        self.key0 = QtWidgets.QPushButton(self.Keypad)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key0.setFont(font)
        self.key0.setObjectName("key0")
        self.gridLayout_2.addWidget(self.key0, 3, 1, 1, 1)
        self.key7 = QtWidgets.QPushButton(self.Keypad)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key7.setFont(font)
        self.key7.setObjectName("key7")
        self.gridLayout_2.addWidget(self.key7, 2, 0, 1, 1)
        self.key4 = QtWidgets.QPushButton(self.Keypad)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key4.setFont(font)
        self.key4.setObjectName("key4")
        self.gridLayout_2.addWidget(self.key4, 1, 0, 1, 1)
        self.keyUpdate = QtWidgets.QPushButton(self.Keypad)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.keyUpdate.setFont(font)
        self.keyUpdate.setObjectName("keyUpdate")
        self.gridLayout_2.addWidget(self.keyUpdate, 4, 0, 1, 3)
        self.key9 = QtWidgets.QPushButton(self.Keypad)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key9.setFont(font)
        self.key9.setObjectName("key9")
        self.gridLayout_2.addWidget(self.key9, 2, 2, 1, 1)
        self.key1 = QtWidgets.QPushButton(self.Keypad)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key1.setFont(font)
        self.key1.setObjectName("key1")
        self.gridLayout_2.addWidget(self.key1, 0, 0, 1, 1)
        self.key6 = QtWidgets.QPushButton(self.Keypad)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key6.setFont(font)
        self.key6.setObjectName("key6")
        self.gridLayout_2.addWidget(self.key6, 1, 2, 1, 1)
        self.key8 = QtWidgets.QPushButton(self.Keypad)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key8.setFont(font)
        self.key8.setObjectName("key8")
        self.gridLayout_2.addWidget(self.key8, 2, 1, 1, 1)
        self.key2 = QtWidgets.QPushButton(self.Keypad)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.key2.setFont(font)
        self.key2.setObjectName("key2")
        self.gridLayout_2.addWidget(self.key2, 0, 1, 1, 1)
        self.keyClear = QtWidgets.QPushButton(self.Keypad)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.keyClear.setFont(font)
        self.keyClear.setObjectName("keyClear")
        self.gridLayout_2.addWidget(self.keyClear, 3, 0, 1, 1)
        self.infoLabel = QtWidgets.QLabel(self.Keypad)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.infoLabel.setFont(font)
        self.infoLabel.setObjectName("infoLabel")
        #self.infoLabel.setText("Info")
        self.gridLayout_2.addWidget(self.infoLabel, 5, 0, 1, 3)        
       
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.Keypad)
        
        # Tabwidget for Generators 
        self.GeneratorTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.GeneratorTabs.setMinimumSize(QtCore.QSize(200, 120))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.GeneratorTabs.setFont(font)
        self.GeneratorTabs.setObjectName("GeneratorTabs")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(725, 14, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 3)
        
        # Generator 1 
        self.gen1Frequency = QtWidgets.QLineEdit(self.tab)
        self.gen1Frequency.setObjectName("gen1Frequency")
        self.gen1Frequency.setText('0')
        self.gridLayout_3.addWidget(self.gen1Frequency, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(17, 279, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setMidLineWidth(1)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(725, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 3, 0, 1, 3)
        self.gen1Power = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.gen1Power.setFont(font)
        self.gen1Power.setFlat(False)
        self.gen1Power.setObjectName("gen1Power")
        self.gridLayout_3.addWidget(self.gen1Power, 4, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(17, 279, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 4, 1, 1, 1)
        self.gen1PowerLabel = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.gen1PowerLabel.setFont(font)
        self.gen1PowerLabel.setObjectName("gen1PowerLabel")
        self.gridLayout_3.addWidget(self.gen1PowerLabel, 4, 2, 1, 1)
        
        # Generator 2 
        self.GeneratorTabs.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(725, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 1, 0, 1, 3)
        self.gen2Frequency = QtWidgets.QLineEdit(self.tab_2)
        self.gen2Frequency.setObjectName("gen2Frequency")
        self.gen2Frequency.setText('0')
        self.gridLayout_4.addWidget(self.gen2Frequency, 2, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 275, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem5, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 2, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(725, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 3, 0, 1, 3)
        self.gen2Power = QtWidgets.QPushButton(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.gen2Power.setFont(font)
        self.gen2Power.setObjectName("gen2Power")
        self.gridLayout_4.addWidget(self.gen2Power, 4, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 274, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem7, 4, 1, 1, 1)
        self.gen2PowerLabel = QtWidgets.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.gen2PowerLabel.setFont(font)
        self.gen2PowerLabel.setObjectName("gen2PowerLabel")
        self.gridLayout_4.addWidget(self.gen2PowerLabel, 4, 2, 1, 1)
        
        # Generator 3 
        self.GeneratorTabs.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem8, 1, 0, 1, 3)
        spacerItem9 = QtWidgets.QSpacerItem(20, 276, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem9, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 2, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(725, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem10, 3, 0, 1, 3)
        self.gen3Power = QtWidgets.QPushButton(self.tab_4)
        self.gen3Power.setObjectName("gen3Power")
        self.gridLayout_5.addWidget(self.gen3Power, 4, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 276, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem11, 4, 1, 1, 1)
        self.gen3PowerLabel = QtWidgets.QLabel(self.tab_4)
        self.gen3PowerLabel.setObjectName("gen3PowerLabel")
        self.gridLayout_5.addWidget(self.gen3PowerLabel, 4, 2, 1, 1)
        self.gen3Frequency = QtWidgets.QLineEdit(self.tab_4)
        self.gen3Frequency.setObjectName("gen3Frequency")
        self.gen3Frequency.setText('0')
        self.gridLayout_5.addWidget(self.gen3Frequency, 2, 0, 1, 1)
        self.GeneratorTabs.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 0, 0, 1, 1)
        
        # Sweep Generator Widgets
        self.sweepStart = QtWidgets.QLineEdit(self.tab_3)
        self.sweepStart.setObjectName("sweepStart")
        self.sweepStart.setText('0')
        self.gridLayout_7.addWidget(self.sweepStart, 1, 0, 1, 3)
        spacerItem12 = QtWidgets.QSpacerItem(20, 119, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem12, 1, 4, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_7.addWidget(self.label_11, 1, 5, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_7.addWidget(self.label_12, 2, 0, 1, 1)
        self.sweepStop = QtWidgets.QLineEdit(self.tab_3)
        self.sweepStop.setObjectName("sweepStop")
        self.sweepStop.setText('0')
        self.gridLayout_7.addWidget(self.sweepStop, 3, 0, 1, 3)
        spacerItem13 = QtWidgets.QSpacerItem(20, 118, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem13, 3, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_7.addWidget(self.label_13, 3, 5, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_7.addWidget(self.label_14, 4, 0, 1, 1)
        self.sweepStep = QtWidgets.QLineEdit(self.tab_3)
        self.sweepStep.setObjectName("sweepStep")
        self.sweepStep.setText('0')
        self.gridLayout_7.addWidget(self.sweepStep, 5, 0, 1, 3)
        spacerItem14 = QtWidgets.QSpacerItem(20, 119, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem14, 5, 4, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_7.addWidget(self.label_15, 5, 5, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(725, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem15, 6, 0, 1, 6)
        self.startStopSweep = QtWidgets.QPushButton(self.tab_3)
        self.startStopSweep.setObjectName("startStopSweep")
        self.gridLayout_7.addWidget(self.startStopSweep, 7, 0, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem16, 7, 1, 1, 1)
        self.sweepPower = QtWidgets.QPushButton(self.tab_3)
        self.sweepPower.setObjectName("sweepPower")
        self.gridLayout_7.addWidget(self.sweepPower, 7, 2, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem17, 7, 3, 1, 1)
        self.sweepPowerLabel = QtWidgets.QLabel(self.tab_3)
        self.sweepPowerLabel.setObjectName("sweepPowerLabel")
        self.gridLayout_7.addWidget(self.sweepPowerLabel, 7, 4, 1, 2)
        self.GeneratorTabs.addTab(self.tab_3, "")
        self.horizontalLayout.addWidget(self.GeneratorTabs)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # Add names/labels
        self.retranslateUi(MainWindow)
        
        # Set focus on generator 1 at startup
        self.GeneratorTabs.setCurrentIndex(0)
        self.currentData = self.gen1Frequency
        
        # Signal/Slot connectors 
        # Customize signals
        # use a lambda to send a different character to slot for each key
        # connect has no arguments otherwise
        self.key1.clicked.connect(lambda s: self.keypadEnter('1'))
        self.key2.clicked.connect(lambda s: self.keypadEnter('2'))
        self.key3.clicked.connect(lambda s: self.keypadEnter('3'))
        self.key4.clicked.connect(lambda s: self.keypadEnter('4'))
        self.key5.clicked.connect(lambda s: self.keypadEnter('5'))
        self.key6.clicked.connect(lambda s: self.keypadEnter('6'))
        self.key7.clicked.connect(lambda s: self.keypadEnter('7'))
        self.key8.clicked.connect(lambda s: self.keypadEnter('8'))
        self.key9.clicked.connect(lambda s: self.keypadEnter('9'))
        self.keyClear.clicked.connect(self.keypadClear)
        self.key0.clicked.connect(lambda s: self.keypadEnter('0'))
        self.keyBack.clicked.connect(self.keypadBack)
        self.keyUpdate.clicked.connect(self.keypadUpdate)
        
        # Set focus for Generator tabs so that keypad data is entered in correct Line Edit 
        self.GeneratorTabs.currentChanged.connect(self.setFocus) 
                            
        # Power set for each generator 
        self.gen1Power.clicked.connect(self.updatePLLPower)
        self.gen2Power.clicked.connect(self.updatePLLPower)
        self.gen3Power.clicked.connect(self.updatePLLPower)
        self.sweepPower.clicked.connect(self.updatePLLPower)
        
        # Start Sweep and when sweep is operating can stop with this key 
        # Sweep runs in a thread so GUI is not frozen 
        self.startStopSweep.clicked.connect(self.manageSweep)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Tab order - probably not relevant for touchscreen interface
        MainWindow.setTabOrder(self.gen1Frequency, self.gen2Frequency)
        MainWindow.setTabOrder(self.gen2Frequency, self.gen3Frequency)
        MainWindow.setTabOrder(self.gen3Frequency, self.sweepStart)
        MainWindow.setTabOrder(self.sweepStart, self.sweepStop)
        MainWindow.setTabOrder(self.sweepStop, self.sweepStep)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RF Generator"))
        self.keyBack.setText(_translate("MainWindow", "<"))
        self.key5.setText(_translate("MainWindow", "5"))
        self.key3.setText(_translate("MainWindow", "3"))
        self.key0.setText(_translate("MainWindow", "0"))
        self.key7.setText(_translate("MainWindow", "7"))
        self.key4.setText(_translate("MainWindow", "4"))
        self.keyUpdate.setText(_translate("MainWindow", "UPDATE"))
        self.key9.setText(_translate("MainWindow", "9"))
        self.key1.setText(_translate("MainWindow", "1"))
        self.key6.setText(_translate("MainWindow", "6"))
        self.key8.setText(_translate("MainWindow", "8"))
        self.key2.setText(_translate("MainWindow", "2"))
        self.keyClear.setText(_translate("MainWindow", "C"))
        self.label.setText(_translate("MainWindow", "Frequency"))
        self.label_2.setText(_translate("MainWindow", "KHz"))
        self.gen1Power.setText(_translate("MainWindow", "Power"))
        self.gen1PowerLabel.setText(_translate("MainWindow", "MUTED"))
        self.GeneratorTabs.setTabText(self.GeneratorTabs.indexOf(self.tab), _translate("MainWindow", "Gen 1"))
        self.label_4.setText(_translate("MainWindow", "Frequency"))
        self.label_5.setText(_translate("MainWindow", "KHz"))
        self.gen2Power.setText(_translate("MainWindow", "Power"))
        self.gen2PowerLabel.setText(_translate("MainWindow", "MUTED"))
        self.GeneratorTabs.setTabText(self.GeneratorTabs.indexOf(self.tab_2), _translate("MainWindow", "Gen 2"))
        self.label_7.setText(_translate("MainWindow", "Frequency"))
        self.label_8.setText(_translate("MainWindow", "KHz"))
        self.gen3Power.setText(_translate("MainWindow", "Power"))
        self.gen3PowerLabel.setText(_translate("MainWindow", "MUTED"))
        self.GeneratorTabs.setTabText(self.GeneratorTabs.indexOf(self.tab_4), _translate("MainWindow", "Gen 3"))
        self.label_10.setText(_translate("MainWindow", "Start"))
        self.label_11.setText(_translate("MainWindow", "KHz"))
        self.label_12.setText(_translate("MainWindow", "Stop"))
        self.label_13.setText(_translate("MainWindow", "KHz"))
        self.label_14.setText(_translate("MainWindow", "Step"))
        self.label_15.setText(_translate("MainWindow", "KHz"))
        self.startStopSweep.setText(_translate("MainWindow", "Start"))
        self.sweepPower.setText(_translate("MainWindow", "Power"))
        self.sweepPowerLabel.setText(_translate("MainWindow", "MUTED"))
        self.GeneratorTabs.setTabText(self.GeneratorTabs.indexOf(self.tab_3), _translate("MainWindow", "Sweep (Gen1)"))
        
