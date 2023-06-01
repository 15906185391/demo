from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(932, 651)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 40, 683, 512))
        self.graphicsView.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.graphicsView.setObjectName("graphicsView")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(700, 0, 221, 171))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_OpenCamera = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_OpenCamera.setGeometry(QtCore.QRect(10, 110, 101, 28))
        self.pushButton_OpenCamera.setObjectName("pushButton_OpenCamera")
        self.pushButton_CloseCamera = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_CloseCamera.setGeometry(QtCore.QRect(110, 110, 101, 28))
        self.pushButton_CloseCamera.setObjectName("pushButton_CloseCamera")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(180, 560, 41, 16))
        self.label_5.setObjectName("label_5")
        self.label_FPS = QtWidgets.QLabel(self.centralwidget)
        self.label_FPS.setGeometry(QtCore.QRect(220, 560, 41, 16))
        self.label_FPS.setObjectName("label_FPS")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "CameraControl"))
        self.pushButton_OpenCamera.setText(_translate("MainWindow", "OpenCamera"))
        self.pushButton_CloseCamera.setText(_translate("MainWindow", "CloseCamera"))
        self.label_5.setText(_translate("MainWindow", "FPS:"))
        self.label_FPS.setText(_translate("MainWindow", "0"))