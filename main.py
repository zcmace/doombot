from win32api import SetCursorPos, GetSystemMetrics
import win32gui
import win32con
from time import sleep
from pyautogui import screenshot

x, y, width, height = 0, 0, 1280, 720


window = win32gui.FindWindow(None, 'DOOM')

win32gui.SetForegroundWindow(window)

win32gui.SetWindowPos(window, win32con.HWND_TOP, x, y, width, height, win32con.SWP_SHOWWINDOW)


count = 0

while count < 10000:
    screenshot('./dump/screenshot_' + str(count) + '.png', region=(x, y, width, height))
    sleep(1)
    count += 1
