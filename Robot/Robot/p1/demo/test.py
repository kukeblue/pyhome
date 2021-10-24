import pyautogui, sys
import time
   
by = pyautogui.locateOnScreen('by.png', confidence=0.3)
if by != None:
    print(by)