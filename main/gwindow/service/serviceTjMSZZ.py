# 聚精惠神战斗服务
import pyautogui
import time
from main.gwindow import mhWindow

MHService = mhWindow.MHService


def zdHS(mhWindow):
    button7location = mhWindow.findImgInWindow('meng.png')
    if button7location is None:
        tjButton = mhWindow.findImgInWindow('zd_tj.png')
        if tjButton is not None:
            mhWindow.battleCount = mhWindow.battleCount + 1
            if mhWindow.battleCount == 1:
                mhWindow.resetMove4()
                time.sleep(0.3)
                pyautogui.press('f3')
                time.sleep(0.3)
                pyautogui.click()
                time.sleep(0.3)
                pyautogui.hotkey('alt', 'q')
            elif mhWindow.battleCount == 3:
                print('魔兽之鹰战斗自动服务：发现特技按钮')

                mhWindow.findImgInWindowMultiple('zd_tj.png')
                time.sleep(0.3)
                pyautogui.click()
                time.sleep(0.3)
                mhWindow.findImgInWindowMultiple('tj_mszy.png')
                time.sleep(0.3)
                pyautogui.click()
                mhWindow.resetMove4()
                time.sleep(0.3)
                pyautogui.click()
                pyautogui.hotkey('alt', 'q')
            else:
                pyautogui.hotkey('alt', 'q')
                pyautogui.hotkey('alt', 'q')



serviceTjMSZY = MHService()
serviceTjMSZY.name = '魔兽之鹰战斗自动服务'
serviceTjMSZY.call = zdHS
serviceTjMSZY.status = 0
