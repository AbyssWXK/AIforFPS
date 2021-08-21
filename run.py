# -*- coding: utf-8 -*-
from getPicture import *
from hook import *
class AIforFPS(QObject):
    def __init__(self):
        super(AIforFPS, self).__init__()
        self.hook = Hook()
        self.getPicture = getPicture

"""
@Time    :2021/8/21 15:35
@Author  :Administrator
@FileName:run.py
@Software:PyCharm
"""