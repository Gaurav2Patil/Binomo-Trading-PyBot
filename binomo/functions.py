from pyautogui import *
import webbrowser as wb
import pyautogui
import keyboard
import random as random
import time as time
import win32api , win32con
import pyperclip

# dictionary of locations.
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

# open link on chrome or webbrowser
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
        l = [80,180,405,912,2052,4617,10388,23373,80000]
        for i in l:
                yield i
global values
values = gen()

class change_amount:
    def amount():
        global a
        a= values.__next__()
        pyautogui.write(str(a),interval=0.001)

    def print_amount():
        return a

def check():
    pyautogui.hotkey('ctrl','a','ctrl','c',interval=0.01)
    copied_value = pyperclip.paste()
    if copied_value == str(change_amount.print_amount()):
        click(1816,557)
        time.sleep(0.01)
    else:
        pyautogui.press('backspace', presses=8,interval=0.001)
        time.sleep(0.01)
        pyautogui.write(str(change_amount.print_amount()),interval=0.001)
        time.sleep(0.1)
        check()
        time.sleep(0.1)
