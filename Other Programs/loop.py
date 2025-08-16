import pyautogui
import time
pyautogui.hotkey('winleft', 'q')
time.sleep(0.5)
pyautogui.typewrite("Whats")
pyautogui.press("Enter")
time.sleep(2.5)
pyautogui.hotkey('ctrl', 'f')
pyautogui.typewrite("Neech")
pyautogui.press("tab")
pyautogui.press("Enter")
time.sleep(2)
count = 1
# a='pppp'
while count <= 50:
    if (count % 2 == 0):
        pyautogui.typewrite("%d. Kutte" % (count))
    else:
        pyautogui.typewrite("%d. Neech" % (count))
    # pyautogui.typewrite(a)
    time.sleep(0.5)
    pyautogui.press("Enter")
    count += 1
    # a++

# while count <= 50:
#     pyautogui.typewrite("Neech")
#     time.sleep(0.5)
#     pyautogui.press("Enter")
#     count += 1
