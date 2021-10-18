import pyautogui
import time
import zhuagui

# pyautogui.press('f1')

order = 1
# zhuagui.dozhuagui()

def doFighting():
    pyautogui.moveTo(527, 456)
    pyautogui.click() 
    pyautogui.click() 
    pyautogui.click() 

    
    # by = pyautogui.locateOnScreen('./images/by.png', confidence=0.5)
    by = None
    if by != None:
        print('找到by')
        pyautogui.moveTo(by.left + 2, by.top - 5)
        pyautogui.press('f2') 
        pyautogui.click() 
    else:
        pyautogui.moveTo(338, 285)
        pyautogui.press('f2') 
        pyautogui.click() 

    time.sleep(1)
    pyautogui.hotkey('alt', 'q')

    isFighting = True
    while isFighting:
        time.sleep(1)
        button7location = pyautogui.locateOnScreen('./images/meng.png')
        if button7location == None:
            print('打架结束')
            if order % 2 == 0:
                zhuagui.dozhuagui()
            isFighting = False
        button7location2 = pyautogui.locateOnScreen('./images/zidong.png')
        if button7location2 != None:
            pyautogui.hotkey('alt', 'a')

            # 第二回合点自动
            pyautogui.hotkey('alt', 'q')
            # pyautogui.moveTo(button7location2.left, button7location2.top)
            # pyautogui.click()
            # doOption = True
        else: 
            print('等待自动...')
        # 结束

# # 打开客户端完毕
print('Press Ctrl-C to quit.')
round = 1
try:
    while True:
        time.sleep(1)
        youxi = pyautogui.locateOnScreen('./images/youxi.png')
        if youxi == None:
            print('未找到游戏')
            continue

        button7location = pyautogui.locateOnScreen('./images/meng.png')
        if button7location != None:
            print('进入打架')
            order = order + 1
            time.sleep(0.5)
            doFighting()
        else:
            print('等待打架')
        # x, y = pyautogui.position()
        # positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        # print(positionStr, end='')
        # print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')

