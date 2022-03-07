# 聚精惠神战斗服务
import pyautogui
import time
from main.gwindow import mhWindow

MHService = mhWindow.MHService


def tjJJHS(mhWindow):
    button7location = mhWindow.findImgInWindow('meng.png')
    if button7location is None:
        tjButton = mhWindow.findImgInWindow('zd_tj.png')
        if tjButton is not None:
            print('聚精会神战斗自动服务：发现特技按钮')
            mhWindow.resetMove2()
            # 查看愤怒
            fn = mhWindow.findImgInWindow('fn.png', confidence=0.98)
            if fn is not None:
                mhWindow.findImgInWindowMultiple('zd_tj.png')
                time.sleep(0.3)
                pyautogui.click()
                time.sleep(0.3)
                mhWindow.findImgInWindowMultiple('tj_jjhs.png')
                time.sleep(0.3)
                warn = mhWindow.findImgInWindow('tj_jjhs_warn.png')
                if warn is None:
                    pyautogui.click()
                    time.sleep(0.3)
                    pyautogui.click()
                    time.sleep(0.3)
                    pyautogui.hotkey('alt', 'q')
                else:
                    pyautogui.hotkey('alt', 'q')
                    pyautogui.hotkey('alt', 'q')
            else:
                print('聚精会神战斗自动服务：愤怒不足')
                pyautogui.hotkey('alt', 'q')
                pyautogui.hotkey('alt', 'q')


serviceTjJJHS = MHService()
serviceTjJJHS.name = '聚精会神战斗自动服务'
serviceTjJJHS.call = tjJJHS
serviceTjJJHS.status = 0
