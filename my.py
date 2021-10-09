import time

import win32gui
import win32con
import win32api
time.sleep(3)
title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
if '梦幻西游' in title:
    hwnd = win32gui.FindWindow(None, title)
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width = right - left
    height = bottom - top
    print(width, height)



# win32api.SendMessage(handle, win32con.WM_KEYUP, 0x41)
# time.sleep(0.1)
# lparam = 40 << 16 | 38
# win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, 0, lparam)
# time.sleep(0.1)
# win32api.SendMessage(handle, win32con.WM_LBUTTONUP, 0, lparam)
# b = win32api.SendMessage(handle, win32con.WM_SETTEXT, None, '消息')
# tmp = win32api.MAKELONG(38, 40)
# a = win32api.SendMessage(handle, win32con.WM_LBUTTONUP, 0, tmp)
# print(b, a)
# win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
# a = win32gui.SendMessage(handle,win32con.WM_CLOSE, 0, 0)
# b = win32gui.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)
# print(a)
# win32api.PostMessage(handle, win32con.WM_KEYDOWN, win32con.VK_F5, 0)#发送F9键
# win32api.PostMessage(handle, win32con.WM_KEYUP, win32con.VK_F5, 0)
# long_position = win32api.MAKELONG(100, 100)
# win32api.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)
# win32api.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)
input("Press Enter to continue..." )