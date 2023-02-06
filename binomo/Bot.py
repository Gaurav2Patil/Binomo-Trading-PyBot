from pyautogui import *
import pyautogui
import keyboard
import time as time
import functions as f
import pyperclip

f.open_webbrowser()
time.sleep(10)
f.chart_scanner()
time.sleep(2)
f.click(f.data['Amount.png'][0],f.data['Amount.png'][1])
pyautogui.press('backspace', presses=8,interval=0.001)
f.change_amount()
f.click(1816,557)

while keyboard.is_pressed("q")==False :
    time.sleep(0.1)
    if pyautogui.locateOnScreen('time_remainning_30.png',region=[358,183,98,37]) != None:
        time.sleep(0.7)
        if pyautogui.pixelMatchesColor(1440,1005,(225,221,60),tolerance=50)==True:
            time.sleep(0.1)
            f.values.close()
            f.values = f.gen()
            f.click(f.data['Amount.png'][0],f.data['Amount.png'][1])
            time.sleep(0.01)
            pyautogui.press('backspace', presses=8,interval=0.001)
            time.sleep(0.01)
            f.change_amount.amount()
            time.sleep(0.01)
            f.check()
        elif pyautogui.pixelMatchesColor(1440,1005,(225,221,60),tolerance=50)!=True:
            time.sleep(0.1)
            f.click(f.data['Amount.png'][0],f.data['Amount.png'][1])
            pyautogui.press('backspace', presses=8,interval=0.001)
            time.sleep(0.01)
            f.change_amount.amount()
            time.sleep(0.01)
            f.check()
        else:
            continue
    elif pyautogui.locateOnScreen('5_30_notify.png',confidence=0.75) != None:
            f.notify_5_30()
            time.sleep(0.1)
            f.click(1816,650)
            time.sleep(0.1)
            pyautogui.moveTo(1816,557)
    else:
        continue
