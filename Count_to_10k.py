import time
import pyautogui

def sendMessage():
    time.sleep(5)
    thing = 30
    text = "Come play"
    while thing < 100:
        time.sleep(1.5)
        pyautogui.typewrite(str('@a'))
        pyautogui.press('enter')
        pyautogui.typewrite(str(text))
        pyautogui.press('enter')
        thing += 1
        
sendMessage()