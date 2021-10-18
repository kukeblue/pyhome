import pyautogui, sys
import time
   
by = pyautogui.locateOnScreen('by.png', confidence=0.5)
if by != None:
    print(by)