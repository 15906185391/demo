import sys

from PySide6 import QtWidgets
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from MainWindow import Ui_MainWindow
import cv2.cv2 as cv
import DahengCamera


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.cap = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.Camera = DahengCamera.DahengCamera()
        self.TimerForShowImageInGraphicsView = QTimer()
        self.ImageWidthInGraphicsView = 600
        self.scene = QGraphicsScene()

        self.SlotInit()
        self.UpdateUI()

    """ 初始化槽信号函数"""

    def SlotInit(self):
        self.ui.pushButton_OpenCamera.clicked.connect(self.PB_OpenCamera_clicked)
        self.ui.pushButton_CloseCamera.clicked.connect(self.PB_CloseCamera_clicked)
        self.TimerForShowImageInGraphicsView.timeout.connect(self.SlotForShowImageInGraphicsView)

    """ 更新UI界面"""

    def UpdateUI(self):
        self.ui.pushButton_OpenCamera.setDisabled(self.Camera.IsCameraOpened)
        self.ui.pushButton_CloseCamera.setDisabled(not self.Camera.IsCameraOpened)

    """ 点击OpenCamera"""

    def PB_OpenCamera_clicked(self):
        self.Camera.OpenCamera(1)
        self.Camera.StartAcquisition()
        self.TimerForShowImageInGraphicsView.start(33)
        self.UpdateUI()

    """ 点击CloseCamera"""

    def PB_CloseCamera_clicked(self):
        DahengCamera.Save_img()
        self.Camera.CloseCamera(1)
        if self.TimerForShowImageInGraphicsView.isActive():
            self.TimerForShowImageInGraphicsView.stop()
        DahengCamera.num = 0
        self.cap = True
        self.UpdateUI()

    def PB_Save_clicked(self):
        DahengCamera.Save_img()

    """ 图像显示回调函数"""

    def SlotForShowImageInGraphicsView(self):
        if DahengCamera.rawImageUpdate is None:
            return
        else:
            self.ImageShow = DahengCamera.rawImageUpdateList[0]
            ImageRatio = float(self.ImageShow.shape[0] / self.ImageShow.shape[1])
            image_width = self.ImageWidthInGraphicsView
            show = cv.resize(self.ImageShow, (image_width, int(image_width * ImageRatio)))
            # show = cv.cvtColor(show, cv.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色
            self.showImage = QImage(show.data, show.shape[1], show.shape[0],
                                    QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
            item = QGraphicsPixmapItem(QPixmap.fromImage(self.showImage))
            self.scene.clear()
            self.scene.addItem(item)
            self.scene.setSceneRect(0, 0, image_width + 1, image_width * ImageRatio + 1)
            self.ui.graphicsView.setScene(self.scene)
            self.ui.graphicsView.show()
            self.ui.label_FPS.setText(str(self.Camera.GetFPS()))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())
