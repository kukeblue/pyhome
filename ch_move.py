import pyautogui, sys
import time


def getJtPosition():
    errorHandle = 0
    while True:
        jiantou = pyautogui.locateOnScreen('./images/jiantou.png', region=(0,0, 1000, 800) ,confidence=0.8)
        if jiantou != None:
            return jiantou
        else:
            errorHandle = errorHandle + 1
            print('未找到箭头', errorHandle)
            if errorHandle == 10:
                print('异常：未找到光标')
                exit(1)

def move(mx, my):
    finished = False
    while finished == False:
        jiantou = getJtPosition()
        dx = jiantou.left - 30
        dy = jiantou.top - 30
        if mx - dx > 2 or mx - dx < -2 or my-dy > 2 or my - dy < -2 :
            cx = mx - dx
            cy =  my - dy
            pyautogui.move(cx, cy)
        else:
            finished = True