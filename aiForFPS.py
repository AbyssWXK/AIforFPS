# -*- coding: utf-8 -*-
from getPicture import *
from hook import *
class AIforFPS(QObject):
    def __init__(self):
        super(AIforFPS, self).__init__()
        self.hook = Hook()
        self.getpicture = getPicture()

        self.threadMouse = QThread()
        self.threadGetPicture = QThread()
        self.hook.moveToThread(self.threadMouse)
        self.getpicture.moveToThread(self.threadGetPicture)

        self.hook.mouseSignal.connect(self.getpicture.centrePicture)
        self.hook.mouseSignal.connect(self.getSignal)
        self.hook.mouseSignal.connect(self.getpicture.getSignal)

        self.threadMouse.start()
        self.threadGetPicture.start()
        self.hook.start_my_mouse_hook(self.hook.mouse_get_pic)
    def getSignal(self):
        print('get')
trick = AIforFPS()

"""
@Time    :2021/8/21 17:11
@Author  :Administrator
@FileName:aiForFPS.py
@Software:PyCharm
"""