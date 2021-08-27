# -*- coding: utf-8 -*-
from PyQt5.Qt import QObject, QThread, pyqtSignal
import pyautogui
class Shot(QObject):
    def __init__(self):
        super(Shot, self).__init__()
        # self.box = []
        self.target = (100,100)
    def getBox(self, boxlist):
        boxs = []
        for x in boxlist:
            boxs.append(x["box"])
        self.updateBoxInfo(boxs)
    def updateBoxInfo(self, boxs):
        if len(boxs) == 0:
            return
        tempMin = 320
        for i in range(len(boxs)):
            centre = ((boxs[i][0]+boxs[i][2])/2, (boxs[i][1]+boxs[i][3])/2)
            if abs(centre[0] - 320) < tempMin:
                self.target = (centre[0] - 320, centre[1] - 320)

    def shot(self):
        # print('move')
        # 移动到屏幕中央 1080p
        pyautogui.moveTo(960, 540, duration=0.1)
        # 移动到目标像素
        pyautogui.moveRel(self.target[0], self.target[1], duration=0.1)
        # 点击左键
        pyautogui.click()# self.target[0], self.target[1]
        # pyautogui.moveRel(-self.target[0], -self.target[1], duration=1)
if __name__=="__main__":
    S = Shot()
    S.shot()
"""
@Time    :2021/8/26 16:25
@Author  :Administrator
@FileName:shot.py
@Software:PyCharm
"""