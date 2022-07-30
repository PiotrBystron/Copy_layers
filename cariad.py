import keyboard
import time
import pyautogui
import win32api

win32api.MessageBox(0, 
'''Naciśnij X aby przenieść warstwy
Naciśnij Q aby wyłączyć program''', 'Clicker')

def clicker():
    while True:
        if keyboard.read_key() == 'x':
            # inherence Labeling
            pyautogui.rightClick()
            pyautogui.press('down')
            pyautogui.press('right')
            pyautogui.press('down')
            pyautogui.press('enter')

            # inherence Interpolation
            pyautogui.rightClick()
            pyautogui.press('down', presses=2)
            pyautogui.press('right')
            pyautogui.press('down', presses=3)
            pyautogui.press('enter')

            time.sleep(1)
            
        if keyboard.read_key() == 'q':
            win32api.MessageBox(0, 'Program został wyłączony', 'Clicker')
            break

clicker()