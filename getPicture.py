# -*- coding: utf-8 -*-
from PIL import ImageGrab
import cv2
import numpy as np
from PyQt5.Qt import QObject, QThread, pyqtSignal
class getPicture(QObject):
    imgSignal = pyqtSignal(np.ndarray)
    def __init__(self):
        super(getPicture,self).__init__()
        print('Pinit')
    def getSignal(self):
        print('Pget')
    def centrePicture(self, width, height):
        print('getPicture')
        width = int(width/2)
        height = int(height/2)
        self.img = ImageGrab.grab(bbox = (960-width, 540-height, 960+width, 540+height))
        self.img = np.array(self.img)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR)
        cv2.imshow('centre', self.img)
        cv2.waitKey(5000)
        self.imgSignal.emit(self.img)
"""
@Time    :2021/8/21 16:39
@Author  :Administrator
@FileName:getPicture.py
@Software:PyCharm
"""