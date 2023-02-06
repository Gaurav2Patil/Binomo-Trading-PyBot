from pyautogui import *
import pyautogui
import time as time
import keyboard
import schedule
from schedule import repeat,every
import random as random
import win32api , win32con
import functions as f
import webbrowser as wb

data ={
    'Amount.png' : [1815,215],
    'up.png' : [1820,500],
    'down.png' : [1820,560],
    'chart_scanner.png' : [1672,205],
    '5_30_notify.png' : [1685,810],
    'reload_site.png' : [87,48],
    'chart_list.png' : [296,130],
    'CL_1.png' : [345,350],
    'CL_2.png' : [345,395],
    'CL_3.png' : [345,440]
}

def open_webbrowser():
    url = "https://binomo.com/trading"
    chrom_path = r"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
    wb.register("chrome",None,wb.BackgroundBrowser(chrom_path))
    wb.get('chrome').open_new_tab(url)

# click function for clicking on location within 0.01 sec
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.0001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def chart_scanner():
    if pyautogui.locateOnScreen('chart_scanner.png',confidence=0.7)!=None:
        click(data['chart_scanner.png'][0],data['chart_scanner.png'][1])
    else :
        pass

def notify_5_30():
        click(data['5_30_notify.png'][0],data['5_30_notify.png'][1])

def reload_website():
        click(data['reload_site.png'][0],data['reload_site.png'][1])

def gen():
        l = [80,260,665,1577,3627,8240,18620,41974,80000]
        for i in l:
                yield i
global values
values = gen()

class change_amount:
    global a
    a = values.__next__()

    def print_amount():
        print(a)

while keyboard.is_pressed("q")==False :
    # if pyautogui.locateOnScreen('lose.png',confidence=0.7,region=[1365,933,355,100]) != None:
    #     print('no')
    # elif pyautogui.locateOnScreen('win.png',confidence=0.5,region=[1365,933,355,100]) != None:
    #     print("yes")
    # else :
    #     print('Noting')


    # if pyautogui.locateOnScreen('time_remainning.png',region=[358,183,98,37]) != None and pyautogui.locateOnScreen('expected_loose.png')!=None:
    #     print('no')
    # else :
    #     if pyautogui.locateOnScreen('time_remainning.png',region=[358,183,98,37]) != None and pyautogui.locateOnScreen('expected_win.png',confidence=0.8)!=None :
    #         print('yes')
    #     else:
    #         print('Nothing')

    if pyautogui.locateOnScreen('expected_win.png',confidence=0.7)!=None: #and pyautogui.locateOnScreen('time_remainning.png',region=[358,183,98,37]) != None:
        time.sleep(0.1)
        values.close()
        values = f.gen()
        click(data['Amount.png'][0],data['Amount.png'][1])
        time.sleep(0.01)
        for i in range(8):
            pyautogui.keyDown('backspace')
            pyautogui.keyUp('backspace')
        pyautogui.write(str(a),interval=0.001)
        # if pyautogui.locateOnScreen('expected_win.png',confidence=0.7)!=None:
        #     change_amount.print_amount()
        # else:
        #     print('amount is not equal')
    else:
        if pyautogui.locateOnScreen('expected_loose.png')!=None: # and pyautogui.locateOnScreen('time_remainning.png',region=[358,183,98,37]) != None:
            change_amount()
        else:
            print('nothing')
    # pyautogui.displayMousePosition()