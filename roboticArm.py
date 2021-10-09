import win32gui
import threading
import time
import pyautogui


class RoboticArm:
    mhWindow = None

    def __init__(self):
        print("- RoboticArm: 初始化机器臂🙌 ...")
        self.initMhWindow()

    def initMhWindow(self):
        self.mhWindow = MHWindow()
        print('- RoboticArm: 初始化梦幻窗口💕 ...')
        self.mhWindow.run()


class MHWindow(threading.Thread):
    hwnd = None
    width = 0
    width = 0
    height = 0
    windowTitle = ''
    windowLeftLocation = 0
    windowTopLocation = 0
    mouseX = 0
    mouseY = 0
    isMouseOut = False

    def __init__(self):
        self.getWindowInfo()
        threading.Thread.__init__(self)

    def run(self):
        while True:
            if self.windowTitle == '':
                print('未找到游戏...')
                time.sleep(10)
                continue
            print("窗口：", self.windowTitle, '位置：', self.windowLeftLocation, self.windowTopLocation, '分辨率：',  self.width,
                  self.height)
            time.sleep(1)
            self.getWindowInfo()
            self.getMousePosition()

    def getMousePosition(self):
        x, y = pyautogui.position()
        self.mouseX = x
        self.mouseY = y
        if self.mouseX < self.windowLeftLocation or self.mouseX > self.windowLeftLocation + self.width\
                or self.mouseY < self.windowTopLocation or self.mouseY > self.windowTopLocation + self.height:
            self.isMouseOut = False
            print('警告：鼠标未在游戏窗口')
        else:
            self.isMouseOut = True

    def getWindowInfo(self):
        def get_all_hwnd(hwnd, mouse):
            if self.hwnd is None:
                if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                    title = win32gui.GetWindowText(hwnd)
                    if '梦幻西游' in title:
                        win32gui.SetForegroundWindow(hwnd)
                        self.hwnd = hwnd
                        self.windowTitle = title

            if self.hwnd:
                win32gui.SetForegroundWindow(self.hwnd)
                left, top, right, bottom = win32gui.GetWindowRect(self.hwnd)
                self.width = right - left
                self.height = bottom - top
                self.windowTopLocation = top
                self.windowLeftLocation = left

        win32gui.EnumWindows(get_all_hwnd, 0)
