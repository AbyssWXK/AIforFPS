# -*- coding: utf-8 -*-
from getPicture import *
from hook import *
from PeopleDetect import *
from shot import *
import torch
class AIforFPS(QObject):
    def __init__(self):
        super(AIforFPS, self).__init__()
        self.hook = Hook()
        self.getpicture = getPicture()
        self.facedetect = YOLOv5Detector()
        self.shotTarget = Shot()

        # model = torch.hub.load('yolov5-master/preTrainedModel/yolov5s.pt','yolov5s')
        self.threadMouse = QThread()
        self.threadGetPicture = QThread()
        self.threadDetect = QThread()
        self.threadShot = QThread()

        self.shotTarget.moveToThread(self.threadShot)
        self.hook.moveToThread(self.threadMouse)
        self.getpicture.moveToThread(self.threadGetPicture)
        self.facedetect.moveToThread(self.threadDetect)
        # self.hook.mouseSignal.connect(self.getpicture.centrePicture)
        # self.hook.mouseSignal.connect(self.getSignal)
        # self.hook.mouseSignal.connect(self.getpicture.getSignal)
        self.getpicture.imgSignal.connect(self.facedetect.detectFrame)
        self.threadGetPicture.started.connect(self.getpicture.centrePictureStream)
        self.facedetect.detectedBox.connect(self.shotTarget.getBox)
        self.hook.mouseSignal.connect(self.shotTarget.shot)

        self.threadMouse.start()
        self.threadGetPicture.start()
        self.threadDetect.start()
        self.threadShot.start()
        self.hook.start_my_mouse_hook(self.hook.mouse_get_pic)
    def getSignal(self):
        print('get')

"""
@Time    :2021/8/21 17:11
@Author  :Administrator
@FileName:aiForFPS.py
@Software:PyCharm
"""