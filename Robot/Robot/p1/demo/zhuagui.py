import pyautogui, sys
import time
import ch_move


# pyautogui.press('f1') 


def findYZ():
    print('开始查找yz ...')

    yz1 = pyautogui.locateOnScreen('./images/yz1.png', confidence=0.6)
    if yz1 != None:
        print('找到yz1')
        return yz1
    yz2 = pyautogui.locateOnScreen('./images/yz1.png', confidence=0.3)
    if yz2 != None:
        print('找到yz2')
        return yz2
    yz3 = pyautogui.locateOnScreen('./images/yz1.png', confidence=0.3)
    if yz3 != None:
        print('找到yz3')
        return yz3
    yz4 = pyautogui.locateOnScreen('./images/yz1.png', confidence=0.3)
    if yz4 != None:
        print('找到yz14')
        return yz4

# # 打开客户端完毕
print('Press Ctrl-C to quit.')
finished = False

try:
    while finished == False:
        time.sleep(1)
        yz = findYZ()
        if yz != None:
            ch_move.move(yz.left, yz.top)
            finished = True
            








  

    
except KeyboardInterrupt:
    print('\n')

