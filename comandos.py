import pyautogui
import time
from linksDeNavegacion import *
import pyperclip
import json
def clickIzquierdo():
    pyautogui.click()
def clickDerecho():
    pyautogui.click(button='right')
def resolucionpantalla():
    return pyautogui.size()
def abrirInicioYAbrirChrome():
    pyautogui.hotkey('win')
    esperarSegundos(2)
    escribirMensaje("google Chrome")
    esperarSegundos(1)
    teclaEnter()
    esperarSegundos(3)
    pyautogui.hotkey('win', 'up')


def buscarYAbrirChrome():
    pyautogui.press
def posicionMouse():
    esperarSegundos(5)
    # Obtener la posición actual del mouse
    x, y = pyautogui.position()
    # Imprimir la posición del mouse
    print(f"La posición actual del mouse es: ({x}, {y})")
def escribirMensaje(mensaje):
    time.sleep(2)
    pyautogui.typewrite(mensaje)
    time.sleep(1)
def teclaEnter():
    pyautogui.press('enter')
def teclaTab():
    pyautogui.press('tab')
def variasVecesTeclas(nombreTecla,veces,tiempo):
    for _ in range (veces):
        nombreTecla()
        time.sleep(tiempo)
def esperarSegundos(segundos):
    time.sleep(segundos)
def abrirUrl():
    pyautogui.press('f6')
def controlC():
    pyautogui.hotkey('ctrl', 'c')
def controlv():
    pyautogui.hotkey('ctrl', 'v')
def nuevapestaña():
    pyautogui.hotkey('ctrl', 't')
def cerrarpestaña():
    pyautogui.hotkey('ctrl', 'w')
def flechaAbajo():
    pyautogui.press('down')
def descargarPdfdesdeGoogleSheets():
    ancho, alto = resolucionpantalla()
    pyautogui.moveTo(ancho-30,alto-30)
    pyautogui.hotkey('alt', 'f')
    esperarSegundos(2)
    variasVecesTeclas(flechaAbajo,7,0.1)
    teclaEnter()
    esperarSegundos(1)
    variasVecesTeclas(flechaAbajo,2,0.1)
    teclaEnter()
    teclaTab()
    teclaEnter()
    esperarSegundos(4)
def abrirwhatsapp():
    nuevapestaña( )
    escribirMensaje(linkwhatsapp)
    teclaEnter()
    esperarSegundos(6)
def volverAtras():
    pyautogui.hotkey('shift', 'tab')
def teclaf4():
    pyautogui.press('f4')
def seleccionarAlInicio():
    pyautogui.hotkey('shift', 'home')
def borrar():
    pyautogui.press('backspace')
def teclaIzquierda():
    pyautogui.press('left')
def teclaDerecha():
    pyautogui.press('right')
def irAAbajo():
    pyautogui.hotkey('ctrl', 'down')
def irNumeroVentana(numero):
    numero=str(numero)
    pyautogui.hotkey('ctrl', numero)
def nuevoChat():
    pyautogui.hotkey('ctrl', 'alt', 'n')
def archivarchat():
    pyautogui.hotkey('ctrl', 'alt', 'shift', 'e')
def ponerGrandeVentana():
    pyautogui.hotkey('winleft','up')
def enviarMouse(x,y):
    pyautogui.moveTo(x,y)
enviarMouse(60,0)
def flechaArriba():
    pyautogui.press('up')
def cargar_posiciones():
    with open('posiciones_mouse.json', 'r') as file:
        posiciones = json.load(file)
    return posiciones
def teclaEsc():
    pyautogui.press('esc')
def abrirvinculo():
    pyautogui.hotkey( 'alt', 'enter')
def buscarEnSheets():
    pyautogui.hotkey( 'ctrl', 'h')
def pegarEnVariable():
    return pyperclip.paste()
def actualizarf5():
    pyautogui.press('f5')
def pasarDePestañaEnSheet():
    pyautogui.hotkey('alt' , 'up')
def teclaBorrar():
    pyautogui.press("backspace")
    