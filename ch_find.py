import pyautogui, sys
import time
import ch_move


# pyautogui.press('f1') 


def findYZ():
    pyautogui.press('f9')
    print('开始查找驿站老板')
    yz = None
    while yz == None:
        yz1 = findImage('images/yz1.png', confidence=0.8)
        if yz1 != None:
            yz = yz1
            break
        yz2 = findImage('images/yz1.png', confidence=0.8)
        if  yz2 != None:
            yz =  yz2
            break
        yz3 = findImage('images/yz1.png', confidence=0.8)
        if yz3 != None:
            yz =  yz3
            break
        yz4 = findImage('images/yz1.png', confidence=0.8)
        if yz4 != None:
            yz =  yz4
            break
        time.sleep(1)
    if yz != None:
        print('-找到驿站老板')
        ch_move.move(yz.left, yz.top)
        print('-点击驿站老板')
        pyautogui.click(clicks=2)
        time.sleep(1)
        yz_yes = findImage('images/yz_yes.png', check = True, confidence=0.6)
        ch_move.move(yz_yes.left, yz_yes.top)
        pyautogui.click()

def findImage(path, check = False, confidence = 0.6, region=(0,0, 1000, 800)):
    errerHandle = 0
    image = None
    if check == False:
        return pyautogui.locateOnScreen(path, confidence=confidence, region=region)

    else:
        while image == None:
            image = pyautogui.locateOnScreen(path, confidence=confidence, region=region)
            if image == None:
                print('图片查找失败， 进入异常倒计时！！！', errerHandle)
                time.sleep(0.5)
                errerHandle = errerHandle + 1
                if errerHandle == 10:
                    exit(1)
            else:
                ch_move.move(image.left, image.top)
                return image





    






