import pyperclip
import time
import pyautogui

time.sleep(2)


screenshot = pyautogui.screenshot(region=(150, 150, 500, 500))

            # Guardar el pantallazo en un archivo
screenshot.save(f'r1empezandopantallazo_region_empezando.png')
        

x_start, y_start = 550, 550  # Coordenadas iniciales del mouse

for i in range(1,25):
    
    # Izquierda
    for ilos in range(1, 25):
        print("Izquierda")
        pyautogui.moveTo(x_start, y_start)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(x_start - 500, y_start, duration=1)
        pyautogui.mouseUp(button='left')
        time.sleep(0.5)
       
        screenshot = pyautogui.screenshot(region=(150, 150, 500, 500))

            # Guardar el pantallazo en un archivo
        screenshot.save(f'1-1Izquierda{i}pantallazo_region_{ilos}.png')
        

    # Abajo
    pyautogui.moveTo(x_start, y_start)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(x_start, y_start -500, duration=1)
    pyautogui.mouseUp(button='left')
    time.sleep(0.5)
    screenshot = pyautogui.screenshot(region=(150, 150, 500, 500))

            # Guardar el pantallazo en un archivo
    screenshot.save(f'1-2Abajo{i}pantallazo_region_{ilos}.png')
        

    # Derecha
    for ilo in range(1, 25):
        print("Derecha")
        pyautogui.moveTo(x_start, y_start)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(x_start + 500, y_start, duration=1)
        pyautogui.mouseUp(button='left')
        time.sleep(0.5)
       
        
        screenshot = pyautogui.screenshot(region=(150, 150, 500, 500))

            # Guardar el pantallazo en un archivo
        screenshot.save(f'1-3Derecha{i}pantallazo_region_{ilo}.png')
        

    # Abajo
    pyautogui.moveTo(x_start, y_start)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(x_start, y_start - 500, duration=1)
    pyautogui.mouseUp(button='left')
    time.sleep(0.5)
    screenshot = pyautogui.screenshot(region=(150, 150, 500, 500))

            # Guardar el pantallazo en un archivo
    screenshot.save(f'1-4Abajo{i}pantallazo_region_{ilos}.png')

from comandos import *
time.sleep(5)
for _ in range(150):
    time.sleep(3)
    flechaArriba()
    time.sleep(1)
    controlC()
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    controlv()
    time.sleep(5)
    pyautogui.hotkey('alt', 'tab')

  