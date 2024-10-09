import pyperclip
import time
import pyautogui


pyautogui.moveTo(150,150,3)
pyautogui.moveTo(950,950,3)
screenshot = pyautogui.screenshot(region=(150, 150, 800, 800))
screenshot.save(f'r1pantallazo_region.png')