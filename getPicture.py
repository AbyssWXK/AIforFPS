# -*- coding: utf-8 -*-
from PIL import ImageGrab
import cv2
import numpy as np
from PyQt5.Qt import QObject, QThread, pyqtSignal
import time
class getPicture(QObject):
    imgSignal = pyqtSignal(np.ndarray)
    def __init__(self):
        super(getPicture,self).__init__()
        print('Pinit')
    def getSignal(self):
        print('Pget')
    def centrePictureStream(self, width = 640, height = 640):
        while(True):
            start = time.time()
            tempWidth = int(width / 2)
            tempHeight = int(height / 2)
            self.img = ImageGrab.grab(bbox=(960 - tempWidth, 540 - tempHeight, 960 + tempWidth, 540 + tempHeight))
            self.img = np.array(self.img)
            self.img = cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR)
            # cv2.imshow('centre', self.img)
            print(time.time()-start)
            cv2.waitKey(30)
            self.imgSignal.emit(self.img)
    def centrePicture(self, width = 640, height = 640):
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