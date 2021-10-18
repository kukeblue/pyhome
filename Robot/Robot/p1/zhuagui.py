import pyautogui
import time
import ch_move
import ch_find


def dozhuagui():
    isFighting = True
    while isFighting:
        time.sleep(1)
        button7location = pyautogui.locateOnScreen('./images/meng.png')
        if button7location == None:
            print('打架结束')
            isFighting = False

    pyautogui.moveTo(527, 456)
    pyautogui.click(button='right',  clicks=2) 


    print('-抓鬼脚本开始')

    print('-打开形囊')
    pyautogui.hotkey('alt', 'e')
    time.sleep(0.3)

    print('-使用导标旗')
    qi_ca = ch_find.findImage('../../../images/qi_ca.png', check=True, confidence=0.8)
    ch_move.move(qi_ca.left, qi_ca.top)
    pyautogui.click(button='right')
    time.sleep(0.3)

    qi_ca_yz = ch_find.findImage('../../../images/qi_ca_yz.png', check=True, confidence=0.8)
    ch_move.move(qi_ca_yz.left, qi_ca_yz.top)
    pyautogui.click()

    print('-关闭形囊')
    pyautogui.hotkey('alt', 'e')

    ch_find.findYZ()
    time.sleep(0.5)

    print('-前往地府')
    pyautogui.press('tab')
    time.sleep(0.5)
    ch_find.findImage('../../../images/gj_df.png', check=True, confidence=0.8)
    pyautogui.click(clicks=3)
    time.sleep(18)
    pyautogui.press('tab')


    print('-进入地府')
    ch_move.move(467, 118)
    pyautogui.click(clicks=2)
    time.sleep(1)
    pyautogui.press('tab')
    ch_find.findImage('../../../images/df_hwc.png', check=True, confidence=0.8)
    pyautogui.click()

    time.sleep(14)

    pyautogui.moveTo(633, 610)
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.press('f9')



    ch_find.findImage('../../../images/df_hwc_2.png', check=True)
    pyautogui.click(clicks=2)
    time.sleep(0.5)
    ch_find.findImage('../../../images/df_hwc_yes.png', check=True)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.click()

    pyautogui.moveTo(386, 705)
    pyautogui.click(clicks=2)
    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(0.3)
    ch_find.findImage('../../../images/df_zd.png', check=True)
    pyautogui.click()

    pyautogui.press('tab')
    time.sleep(15)
    pyautogui.press('f9')
    ch_find.findImage('../../../images/df_zd_2.png', check=True)
    pyautogui.click()
    ch_find.findImage('../../../images/df_zd_yes.png', check=True)
    pyautogui.click()





















