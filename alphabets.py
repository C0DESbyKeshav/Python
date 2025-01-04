import pyautogui
import time
str = 'PQRSTUVWXYZ'
time.sleep(1)
for i in str:
    pyautogui.press(i)
    pyautogui.press('Enter')