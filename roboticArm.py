import win32gui
import threading
import time
import pyautogui


class RoboticArm:
    mhWindow = None

    def __init__(self):
        print("- RoboticArm: 初始化机器臂🙌 ...")

    def initMhWindow(self):
        self.mhWindow = MHWindow()
        print('- RoboticArm: 初始化梦幻窗口💕 ...')

    def start(self):
        self.mhWindow.start()

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
    userServices = []

    def __init__(self):
        self.getWindowInfo()
        threading.Thread.__init__(self)

    def run(self):
        for service in self.userServices:
            service(self)
        while True:
            self.getWindowInfo()
            self.getMousePosition()
            # self.checkpoint()
            if self.windowTitle == '':
                print('未找到游戏...')
                time.sleep(10)
                continue
            time.sleep(3)

    def addService(self, callback):
        self.userServices.append(callback)

    def getImagePosition(self):
        print('获取图片位置')

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

    def moveInWindow(self, x, y):
        pyautogui.moveTo(self.windowLeftLocation + x, self.windowTopLocation + y)

    def resetMove(self):
        self.moveInWindow(self.width / 2, self.height / 2)
        pyautogui.leftClick()

    def resetMove2(self):
        self.moveInWindow(self.width / 2, self.height / 3 * 2 )
        pyautogui.leftClick()

    def automaticPathfinding(self):
        self.resetMove()
        pyautogui.press('tab')

    def checkpoint(self):
        jiantou = pyautogui.locateOnScreen('./images/jiantou.png', region=(self.windowLeftLocation, self.windowTopLocation, self.width, self.height), confidence=0.8)
        if jiantou == None:
            self.resetMove()



