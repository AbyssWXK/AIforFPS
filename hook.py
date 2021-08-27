# -*- coding: utf-8 -*-
# coding=utf-8
import time
import win32gui, win32ui, win32con, win32api
from ctypes import *
from ctypes import wintypes
import win32con
from PyQt5.Qt import QObject, QThread, pyqtSignal

class KBDLLHOOKSTRUCT(Structure):
    _fields_ = [('vkCode', c_int), ('scanCode', c_int), ('flags', c_int), ('time', c_int),
                ('dwExtraInfo', c_uint), ('', c_void_p)]
class POINT(Structure):
    _fields_ = [('x', c_long), ('y', c_long)]
class MSLLHOOKSTRUCT(Structure):
    _fields_ = [('pt', POINT), ('hwnd', c_int), ('wHitTestCode', c_uint), ('dwExtraInfo', c_uint), ]
class Hook(QObject):
    mouseSignal = pyqtSignal()
    def __init__(self):
        super(Hook, self).__init__()
        self.SetWindowsHookEx = windll.user32.SetWindowsHookExA
        self.UnhookWindowsHookEx = windll.user32.UnhookWindowsHookEx
        self.CallNextHookEx = windll.user32.CallNextHookEx
        self.GetMessage = windll.user32.GetMessageA
        self.GetModuleHandle = windll.kernel32.GetModuleHandleW
        # 保存键盘钩子函数句柄
        self.keyboard_hd = None
        # 保存鼠标钩子函数句柄
        self.mouse_hd = None
        count = 0


    def wait_for_msg(self):
        msg = wintypes.MSG()
        self.GetMessage(msg, 0, 0, 0)

    def keyboard_pro(self, nCode, wParam, lParam):
            # """    函数功能：键盘钩子函数，当有按键按下时此函数被回调    """
        if nCode == win32con.HC_ACTION:
            KBDLLHOOKSTRUCT_p = POINTER(KBDLLHOOKSTRUCT)
        param = cast(lParam, KBDLLHOOKSTRUCT_p)
        print(param.contents.vkCode)
        return self.CallNextHookEx(self.keyboard_hd, nCode, wParam, lParam)

    def start_keyboard_hook(self):
        # """    函数功能：启动键盘监听    """
        HOOKPROTYPE = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
        pointer = HOOKPROTYPE(self.keyboard_pro)
        keyboard_hd = self.SetWindowsHookEx(win32con.WH_KEYBOARD_LL, pointer, self.GetModuleHandle(None), 0)
        self.wait_for_msg()

    def stop_keyboard_hook(self):
        # """    函数功能：停止键盘监听    """
        self.UnhookWindowsHookEx(self.keyboard_hd)

    def mouse_get_pic(self, nCode, wParam, lParam):

        if nCode == win32con.HC_ACTION:
            MSLLHOOKSTRUCT_p = POINTER(MSLLHOOKSTRUCT)
            param = cast(lParam, MSLLHOOKSTRUCT_p)
        # 鼠标左键点击
        if wParam == win32con.WM_RBUTTONDOWN:
            # print("左键点击，坐标：x:%d,y:%d" % (param.contents.pt.x, param.contents.pt.y))
            self.mouseSignal.emit()
            # print('emit')
        return self.CallNextHookEx(self.mouse_hd, nCode, wParam, lParam)

    def mouse_pro(self, nCode, wParam, lParam):
        # ''' 函数功能：鼠标钩子函数，当有鼠标事件，此函数被回调    '''
        if nCode == win32con.HC_ACTION:
            MSLLHOOKSTRUCT_p = POINTER(self.MSLLHOOKSTRUCT)
            param = cast(lParam, MSLLHOOKSTRUCT_p)
        # 鼠标左键点击
        if wParam == win32con.WM_LBUTTONDOWN:
            print("左键点击，坐标：x:%d,y:%d" % (param.contents.pt.x, param.contents.pt.y))
        elif wParam == win32con.WM_LBUTTONUP:
            print("左键抬起，坐标：x:%d,y:%d" % (param.contents.pt.x, param.contents.pt.y))
        elif wParam == win32con.WM_MOUSEMOVE:
            print("鼠标移动，坐标：x:%d,y:%d" % (param.contents.pt.x, param.contents.pt.y))
        elif wParam == win32con.WM_RBUTTONDOWN:
            print("右键点击，坐标：x:%d,y:%d" % (param.contents.pt.x, param.contents.pt.y))
        elif wParam == win32con.WM_RBUTTONUP:
            print("右键抬起，坐标：x:%d,y:%d" % (param.contents.pt.x, param.contents.pt.y))
        return self.CallNextHookEx(self.mouse_hd, nCode, wParam, lParam)

    def start_mouse_hook(self):
            # """    函数功能：启动鼠标监听    """
        HOOKPROTYPE = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
        pointer = HOOKPROTYPE(self.mouse_get_pic)
        mouse_hd = self.SetWindowsHookEx(win32con.WH_MOUSE_LL, pointer, self.GetModuleHandle(None), 0)
        self.wait_for_msg()

    def start_my_mouse_hook(self,function):
        HOOKPROTYPE = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
        pointer = HOOKPROTYPE(function)
        self.mouse_hd = self.SetWindowsHookEx(win32con.WH_MOUSE_LL, pointer, self.GetModuleHandle(None), 0)
        self.wait_for_msg()

    def stop_mouse_hook(self):
        # """    函数功能：停止鼠标监听    """
        self.UnhookWindowsHookEx(self.mouse_hd)
# hook = Hook()
# hook.start_my_mouse_hook(hook.mouse_get_pic)

"""
@Time    :2021/8/21 15:22
@Author  :Administrator
@FileName:hook.py
@Software:PyCharm
"""