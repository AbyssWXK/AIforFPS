# -*- coding: utf-8 -*-
from getPicture import *
from hook import *
from PyQt5.Qt import QApplication
from aiForFPS import *
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AIforFPS()
    sys.exit(app.exec_())
"""
@Time    :2021/8/21 15:35
@Author  :Administrator
@FileName:run.py
@Software:PyCharm
"""