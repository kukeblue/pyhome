from gwindow.mhWindow import MHWindow, MHEvent
from main.gwindow.event.eventGetZgTask import EventZgTask
from main.gwindow.service.serviceTjJJHS import serviceTjJJHS
from main.gwindow.service.serviceBattleTip import serviceBattleTip
from main.gwindow.service.serviceTjMSZZ import serviceTjMSZY



class Robot:
    mhWindow = None

    def __init__(self):
        print("- RoboticArm: 初始化机器臂🙌 ...")

    def initMhWindow(self):
        self.mhWindow = MHWindow()
        # 注册抓鬼事件
        zgTaskEvent = MHEvent(EventZgTask)
        self.mhWindow.addEvent('zgTask', zgTaskEvent)
        # self.mhWindow.addService('zdJJHS', serviceTjJJHS)
        # self.mhWindow.addService('battleTip', serviceBattleTip)
        # self.mhWindow.addService('zdMSZY', serviceTjMSZY)
        # serviceBattleTip.status = 1
        # serviceTjMSZY.status = 1
        print('- RoboticArm: 初始化梦幻窗口💕 ...')

    def start(self):
        self.initMhWindow()
        self.mhWindow.start()
