# 战斗服务
from main.gwindow import mhWindow
import os
MHService = mhWindow.MHService


def battleTip(mhWindow):
    isBattle = mhWindow.findImgInWindow('battleSign.png')
    if isBattle is None:
        if mhWindow.userServices['battleTip'].status == 3:
            print('battleTip: 战斗结束')
            mhWindow.battleCount = 0
            os.system('D:/project/pyhome/images/8378.wav')
            mhWindow.userServices['battleTip'].status = 2
    else:
        mhWindow.userServices['battleTip'].status = 3


serviceBattleTip = MHService()
serviceBattleTip.name = '战斗结束提示'
serviceBattleTip.call = battleTip
serviceBattleTip.status = 0
