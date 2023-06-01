# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerKMNLXw.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGroupBox, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(10, 40, 700, 500))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(760, 20, 200, 200))
        self.pushButton_OpenCamera = QPushButton(self.groupBox)
        self.pushButton_OpenCamera.setObjectName(u"pushButton_OpenCamera")
        self.pushButton_OpenCamera.setGeometry(QRect(10, 30, 75, 30))
        self.pushButton_CloseCamera = QPushButton(self.groupBox)
        self.pushButton_CloseCamera.setObjectName(u"pushButton_CloseCamera")
        self.pushButton_CloseCamera.setGeometry(QRect(110, 30, 75, 30))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(180, 600, 53, 15))
        self.label_FPS = QLabel(self.centralwidget)
        self.label_FPS.setObjectName(u"label_FPS")
        self.label_FPS.setGeometry(QRect(250, 600, 53, 15))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u63a7\u5236", None))
        self.pushButton_OpenCamera.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u76f8\u673a", None))
        self.pushButton_CloseCamera.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u7167\u7247", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"FPS:", None))
        self.label_FPS.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

