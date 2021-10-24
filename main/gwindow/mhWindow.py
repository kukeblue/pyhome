import win32gui
import threading
import time
import pyautogui
import os

filePath = os.path.split(os.path.realpath(__file__))[0]
imageDir = filePath + '\\..\\..\\images\\'


def mhWindowLog(content):
    print('MHWindow: ', content)


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
    userServices = {}
    userEvent = {}
    runTime = 0
    currentShot = None  # 当前快照
    region = None

    def __init__(self):
        self.getWindowInfo()
        threading.Thread.__init__(self)

    def run(self):
        while True:
            self.runTime = self.runTime + 1
            self.getWindowInfo()
            if self.windowTitle == '':
                mhWindowLog('错误 - 未找到游戏窗口，进程休眠10秒')
                time.sleep(10)
                continue
            # 循环执行注册服务
            for k, v in self.userServices.items():
                if v.status == 1:
                    print('注册' + v.name + '服务')
                    v.status = 2
                if v.status == 2:
                    v.call(self)
            # 循环事件
            for k, v in self.userEvent.items():
                if v.instance is not None and v.instance.status == 2:
                    v.instance.raise_exception()
                    v.instance.join()
                    v.instance = None
                    v.EventThread.status = 0

            time.sleep(1)

    # 注册服务
    def addService(self, name, service):
        self.userServices[name] = service

    # 停止服务
    def stopService(self, name):
        self.userServices[name].status = 0

    # 启动服务
    def startService(self, name):
        self.userServices[name].status = 1

    # 注册事件
    def addEvent(self, name, event):
        event.mhWindow = self
        self.userEvent[name] = event

    def doEvent(self, name):
        event = self.userEvent[name]
        if event.EventThread.status == 0:
            mhWindowLog('开始执行任务：' + event.EventThread.name)
            event.instance = event.EventThread(self)
            event.instance.start()
            event.EventThread.status = 1

    def stopEvent(self, name):
        event = self.userEvent[name]
        event.instance.status = 2

    def getMousePosition(self):
        x, y = pyautogui.position()
        self.mouseX = x
        self.mouseY = y
        if self.mouseX < self.windowLeftLocation or self.mouseX > self.windowLeftLocation + self.width \
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
                left, top, right, bottom = win32gui.GetWindowRect(self.hwnd)
                self.width = right - left
                self.height = bottom - top
                self.windowTopLocation = top
                self.windowLeftLocation = left
                self.region = (left, top, self.width,
                               self.height)

        win32gui.EnumWindows(get_all_hwnd, 0)

    def moveInWindow(self, x, y):
        pyautogui.moveTo(self.windowLeftLocation + x, self.windowTopLocation + y)

    def resetMove(self):
        self.moveInWindow(self.width / 2, self.height / 2)
        time.sleep(0.3)
        pyautogui.leftClick()

    def resetMove2(self):
        self.moveInWindow(self.width / 2, self.height / 3 * 2)
        time.sleep(0.3)
        pyautogui.leftClick()
        time.sleep(0.1)
        pyautogui.leftClick()

    def automaticPathfinding(self):
        self.resetMove()
        pyautogui.press('tab')

    def windowShot(self):
        self.currentShot = pyautogui.screenshot(filePath + '\\..\\temp\\mh_window.png', self.region)

    def findImgInWindow(self, path, confidence=0.75):
        location = pyautogui.locateOnScreen(imageDir + path, region=self.region, confidence=confidence)
        return location

    def findImgInWindowMultiple(self, path):
        errorCounter = 0
        image = None
        while image is None:
            image = self.findImgInWindow(path, confidence=0.7)
            if image is None:
                print('图片查找失败， 进入异常倒计时！！！', errorCounter)
                time.sleep(0.3)
                errorCounter = errorCounter + 1
                if errorCounter == 10:
                    return image
            else:
                self.pointMove(image.left, image.top)
                return image

    def checkpoint(self):
        point = self.findImgInWindow('jiantou.png')
        if point is None:
            self.resetMove()
            point = self.findImgInWindow('jiantou.png')
        if point is None:
            self.resetMove()
            point = self.findImgInWindow('jiantou.png')
        return point

    def pointMove(self, mx, my):
        finished = False
        while not finished:
            point = self.checkpoint()
            dx = point.left - 30
            dy = point.top - 27
            if mx - dx > 2 or mx - dx < -2 or my - dy > 2 or my - dy < -2:
                cx = mx - dx
                cy = my - dy
                pyautogui.move(cx, cy)
            else:
                finished = True


class MHService:
    name = None
    call = None
    status = 0  # 0：停止 1：待执行 2： 执行中


class MHEvent:
    name = None
    EventThread = None
    instance = None

    def __init__(self, EventThread):
        self.EventThread = EventThread
        self.name = EventThread.name


if __name__ == '__main__':
    mhWindow = MHWindow()
    mhWindow.start()
    currentShot = pyautogui.screenshot(filePath + '\\..\\temp\\mh_window.png', mhWindow.region)
