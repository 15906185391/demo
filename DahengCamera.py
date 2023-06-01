import gxipy as gx
import time
import threading

rawImageUpdateList = []
rawImageUpdate = None
num = 0


def capture_callback(raw_image):
    if raw_image.get_status() == gx.GxFrameStatusList.INCOMPLETE:
        print("incomplete frame")
    else:
        rgb_image = raw_image.convert("RGB")
        global rawImageUpdateList, num, rawImageUpdate
        rawImageUpdate = rgb_image.get_numpy_array()
        if len(rawImageUpdateList) == 0:
            rawImageUpdateList.append(rawImageUpdate)
        else:
            rawImageUpdateList.pop()
            rawImageUpdateList.append(rawImageUpdate)
        num += 1


class DahengCamera:
    def __init__(self):
        self.cam = None  # 相机对象
        self.dev_num = None
        self.dev_info_list = None
        self.device_manager = gx.DeviceManager()
        self.AcquisitionThread = None
        self.AcquisitionThreadNeedBeStop = False
        self.IsCameraOpened = False
        self.IsCameraStartAcq = False

    def UpdateCameraList(self):
        self.dev_num, self.dev_info_list = self.device_manager.update_device_list()
        if self.dev_num == 0:
            return False, '0'
        else:
            CameraNameList = []
            for info in self.dev_info_list:
                name = info['model_name']
                CameraNameList.append(name)
            return True, CameraNameList

    def OpenCamera(self, Index):
        if self.dev_num == 0:
            return False
        elif self.IsCameraOpened:
            return True
        else:
            self.cam = self.device_manager.open_device_by_index(Index)

        self.AcquisitionThread = threading.Thread(target=self.AcquisitionThreadFunc_CallBack, args=(), daemon=True)
        self.AcquisitionThread.start()
        self.IsCameraOpened = True
        self.AcquisitionThreadNeedBeStop = False

        return True

    def AcquisitionThreadFunc_CallBack(self):
        self.cam.data_stream[0].register_capture_callback(capture_callback)

        while not self.AcquisitionThreadNeedBeStop:
            time.sleep(1)

    def CloseCamera(self, Index):
        if not self.IsCameraOpened:
            return

        self.AcquisitionThreadNeedBeStop = True
        self.StopAcquisition()
        time.sleep(1)
        self.cam.data_stream[0].unregister_capture_callback()
        self.cam.close_device()

        self.IsCameraOpened = False

    def StartAcquisition(self):
        if self.IsCameraOpened and not self.IsCameraStartAcq:
            self.cam.stream_on()
            self.IsCameraStartAcq = True
        else:
            return

    def StopAcquisition(self):
        if self.IsCameraOpened and self.IsCameraStartAcq:
            self.cam.stream_off()
            self.IsCameraStartAcq = False
        else:
            return

    def GetFPS(self):
        return self.cam.CurrentAcquisitionFrameRate.get()
