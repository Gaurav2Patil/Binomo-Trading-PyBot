import functions as f
import pyautogui
import time
import pytesseract as tess
from PIL import Image
import keyboard
import os
import pyperclip

while keyboard.is_pressed("q")==False :
    time.sleep(0.01)
    if pyautogui.locateOnScreen('time_remainning_30.png',region=[358,183,98,37]) != None:
        time.sleep(0.1)
        print('entered in winning time')
        if pyautogui.pixelMatchesColor(1410,995,(225,221,60),tolerance=50)==True:
            time.sleep(0.1)
            print('win')
        else:
            print('not entered in winning')
    else:
        if pyautogui.locateOnScreen('time_remainning_30.png',region=[358,183,98,37]) != None:
            time.sleep(0.1)
            print('entered in loosing time')
            if pyautogui.pixelMatchesColor(1410,995,(225,221,60),tolerance=50)!=True:
                time.sleep(0.1)
                print('ok')
            else:
                print('not entered in ')
        else:
            continue
        continue
