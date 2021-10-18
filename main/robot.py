from gwindow.mhWindow import MHWindow
from gwindow.eventGetZgTask import eventGetZgTask
from gwindow.serviceTjJJHS import serviceTjJJHS


class Robot:
    mhWindow = None

    def __init__(self):
        print("- RoboticArm: 初始化机器臂🙌 ...")

    def initMhWindow(self):
        self.mhWindow = MHWindow()
        # 注册抓鬼事件
        self.mhWindow.addEvent('zgTask', eventGetZgTask)
        self.mhWindow.addService('zdJJHS', serviceTjJJHS)
        print('- RoboticArm: 初始化梦幻窗口💕 ...')

    def start(self):
        self.initMhWindow()
        self.mhWindow.start()