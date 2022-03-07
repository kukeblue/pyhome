import pyautogui
import time
import threading
import ctypes
import os


from pydub import AudioSegment
from pydub.playback import play

class EventZgTask(threading.Thread):
    name = '领取抓鬼任务'
    status = 0
    mhWindow = None

    def __init__(self, mhWindow):
        self.mhWindow = mhWindow
        threading.Thread.__init__(self)

    def run(self):
        try:
            self.call()
        finally:
            self.status = -1
            print('ended')

    def call(self):
        mhWindow = self.mhWindow
        isFighting = True
        while isFighting:
            time.sleep(1)
            button7location = mhWindow.findImgInWindow('meng.png', confidence=0.85)
            if button7location is not None:
                print('打架结束')
                isFighting = False
                print('-抓鬼脚本开始')

                print('-打开形囊')
                pyautogui.hotkey('alt', 'e')
                time.sleep(0.3)

                print('-使用导标旗')
                mhWindow.findImgInWindowMultiple('qi_ca.png')
                time.sleep(0.3)
                pyautogui.click(button='right')
                time.sleep(0.3)
                mhWindow.findImgInWindowMultiple('qi_ca_yz.png')
                time.sleep(0.3)
                pyautogui.click()

                print('-关闭形囊')
                pyautogui.hotkey('alt', 'e')

                pyautogui.press('f9')
                print('开始查找驿站老板')
                yz = None
                while yz is None:
                    yz1 = mhWindow.findImgInWindow('yz1.png')
                    if yz1 is not None:
                        yz = yz1
                        break
                    yz2 = mhWindow.findImgInWindow('yz2.png')
                    if yz2 is not None:
                        yz = yz2
                        break
                    yz3 = mhWindow.findImgInWindow('yz3.png')
                    if yz3 is not None:
                        yz = yz3
                        break
                    yz4 = mhWindow.findImgInWindow('yz4.png')
                    if yz4 is not None:
                        yz = yz4
                        break
                    time.sleep(0.5)
                if yz is not None:
                    print('-找到驿站老板')
                    mhWindow.pointMove(yz.left, yz.top)
                    print('-点击驿站老板')
                    pyautogui.click(clicks=2)
                    time.sleep(1)
                    mhWindow.findImgInWindowMultiple('yz_yes.png')
                    pyautogui.click()

                time.sleep(1)

                print('-前往地府')
                pyautogui.press('tab')
                time.sleep(0.5)

                mhWindow.findImgInWindowMultiple('gj_df.png')
                pyautogui.click(clicks=3)
                time.sleep(18)
                pyautogui.press('tab')

                print('-进入地府')
                pyautogui.press('f9')
                time.sleep(0.3)
                mhWindow.findImgInWindowMultiple('df_mk.png')
                pyautogui.click(clicks=2)
                time.sleep(1.5)
                if self.status == 1:
                    pyautogui.press('tab')
                    mhWindow.findImgInWindowMultiple('df_hwc.png')
                    pyautogui.click()

                    time.sleep(14)

                    mhWindow.moveInWindow(533, 510)
                    pyautogui.click()
                    time.sleep(1.5)
                    pyautogui.press('f9')

                    mhWindow.findImgInWindowMultiple('df_hwc_2.png')
                    pyautogui.click(clicks=2)
                    time.sleep(0.4)
                    mhWindow.findImgInWindowMultiple('df_hwc_yes.png')
                    pyautogui.click()
                    time.sleep(0.4)
                    pyautogui.click()
                    pyautogui.click()

                    mhWindow.moveInWindow(386, 560)
                    pyautogui.click(clicks=2)
                    time.sleep(2)
                pyautogui.press('tab')
                time.sleep(0.3)
                df_zd = mhWindow.findImgInWindow('df_zd.png')
                if df_zd is not None:
                    mhWindow.findImgInWindowMultiple('df_zd.png')
                else:
                    mhWindow.findImgInWindowMultiple('df_zd2.png')
                pyautogui.click()
                time.sleep(13)
                self.status = -1
                print('ended')
                os.system('D:/project/pyhome/images/14430.wav')
                # time.sleep(3)
                # pyautogui.press('f9')

                # os.system(‘mpg123’+ file)
                # song = AudioSegment.from_wav(')
                # mhWindow.findImgInWindowMultiple('df_zd_2.png')
                # pyautogui.click()
                # mhWindow.findImgInWindowMultiple('df_zd_yes.png')
                # pyautogui.click()

    def get_id(self):
        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')

if __name__ == '__main__':
    os.system('D:/project/pyhome/images/14430.wav')



