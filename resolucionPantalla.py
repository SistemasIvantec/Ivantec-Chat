"""

import pyautogui
import time
from comandos import *

pyautogui.alert(text='Gracias por utilizar App-Ats nos sentimos muy alegres de poder contar contigo.\n Para empezar es necesario hacer un ajuste de resoluciones de las ventanas principales', title='Bienvenida-Ats',button='Super :D')
pyautogui.alert(text='Vamos a necesitar que abras chrome y ve a whatsapp \n Ten presente no mover las pestañas y seguir las siguientes instrucciones', title='Datos BasicosAts',button='Si señor XD')
pyautogui.alert(text='Pon la pantalla en grande y sigue las siguientes instrucciones', title='Datos BasicosAts',button='Claro que si!!! :O')

# Paso 1 Deteccion del Cierre Ventana, con este se sabe en donde esta la barra de pestañas

while  True :
    pyautogui.alert(text='1- Coloca el mouse en la X de cerrar ventana, por favor no des click para que cierres la ventana \n no  cambies la ubicacion hasta que pasen 5 segundos \n luego veras que el mouse se va a dirigir automaticamente al lugar donde quedo guardado', title='ATS 1 Paso',button='Claro que si!!! :O')
    time.sleep(3)
    xmouse1,ymouse1 = pyautogui.position()
    pyautogui.alert(text='Ubicacion Guarda, ahora el mouse se va dirigir donde se guardo la ubicación', title='ATS 1 Paso',button='YES!!!')
    
    pyautogui.moveTo(xmouse1,ymouse1,3)

    validacionfinal=pyautogui.confirm(text='¿El mouse se dirigio hacia el boton de cerrar', title='ATS 1 Paso', buttons=['SI :D', 'Volver a Intentar :C'])
    if validacionfinal == 'SI :D':
      break

# Paso 2 Deteccion de escribir Chat en Whatsapp
while  True :
    pyautogui.alert(text='2-En la app de Whatsapp por favor coloca el mouse en Buscar', title='ATS 2 Paso',button='Claro que si!!! :O')
    time.sleep(6)
    xmouse2,ymouse2 = pyautogui.position()
    pyautogui.alert(text='Ubicacion Guarda, ahora el mouse se va dirigir donde se guardo la ubicación', title='ATS 2 Paso',button='YES!!!')
    
    pyautogui.moveTo(xmouse2,ymouse2,3)

    validacionfinal=pyautogui.confirm(text='¿El mouse se dirigio hacia donde indica la instruccion', title='ATS 2 Paso', buttons=['SI :D', 'Volver a Intentar :C'])
    if validacionfinal == 'SI :D':
      break
      
# Paso 3 Deteccion de  Chat en Whatsapp
while  True :
    pyautogui.alert(text='3- Ahora colocate en el primer chat que este abierto ', title='ATS 3 Paso',button='Claro que si!!! :O')
    time.sleep(3)
    xmouse3,ymouse3 = pyautogui.position()
    pyautogui.alert(text='Ubicacion Guarda, ahora el mouse se va dirigir donde se guardo la ubicación', title='ATS 3 Paso',button='YES!!!')
    
    pyautogui.moveTo(xmouse3,ymouse3,3)

    validacionfinal=pyautogui.confirm(text='¿El mouse se dirigio hacia donde indica la instruccion', title='ATS 3 Paso', buttons=['SI :D', 'Volver a Intentar :C'])
    if validacionfinal == 'SI :D':
      break

# Paso 4 Nuevo de  Chat en Whatsapp
while  True :
    
    
    pyautogui.click()
    nuevoChat()    
    escribirMensaje("3004092105")

    
    pyautogui.alert(text='4- Ahora el nuevo Chat esta abierto, dirigite a donde este la primera conversación. ', title='ATS 4 Paso',button='Claro que si!!! :O')
    time.sleep(3)
    xmouse4,ymouse4 = pyautogui.position()
    pyautogui.alert(text='Ubicacion Guarda, ahora el mouse se va dirigir donde se guardo la ubicación', title='ATS 4 Paso',button='YES!!!')
    
    pyautogui.moveTo(xmouse4,ymouse4,3)

    validacionfinal=pyautogui.confirm(text='¿El mouse se dirigio hacia donde indica la instruccion', title='ATS 4 Paso', buttons=['SI :D', 'Volver a Intentar :C'])
    if validacionfinal == 'SI :D':
      break

  # Paso 5 Deteccion de  Chat en Whatsapp
while  True :
    pyautogui.click(xmouse4,ymouse4)
    pyautogui.alert(text='5- Ahora colocate en el donde envías mensajes. ', title='ATS 3 Paso',button='Si mi Cap!!! :O')
    time.sleep(3)
    xmouse5,ymouse5 = pyautogui.position()
    pyautogui.alert(text='Ubicacion Guarda, ahora el mouse se va dirigir donde se guardo la ubicación', title='ATS 5 Paso',button='YES!!!')
    
    pyautogui.moveTo(xmouse5,ymouse5,3)

    validacionfinal=pyautogui.confirm(text='¿El mouse se dirigio hacia donde indica la instruccion', title='ATS 5 Paso', buttons=['SI :D', 'Volver a Intentar :C'])
    if validacionfinal == 'SI :D':
      break


pyautogui.alert(text='Acabamos fue más rapido de lo esperado. ', title='ATS Guardado de Datos',button='¡¡¡Ya era hora!!! :D :D :D')





"""
import pyautogui
import time
import os
import json
from comandos import *

def centralResolucion():
    def guardar_posicion(paso, x, y):
        posiciones = cargar_posiciones()
        posiciones[paso] = {'x': x, 'y': y}
        with open('posiciones_mouse.json', 'w') as file:
            json.dump(posiciones, file)

    def cargar_posiciones():
        if os.path.exists('posiciones_mouse.json'):
            with open('posiciones_mouse.json', 'r') as file:
                return json.load(file)
        return {}

    def ejecutar_paso(paso, mensaje, confirmacion):
        posiciones = cargar_posiciones()
        if str(paso) in posiciones:
            x, y = posiciones[str(paso)]['x'], posiciones[str(paso)]['y']
            pyautogui.moveTo(x, y, 3)
            if pyautogui.confirm(text=confirmacion, title=f'ATS {paso} Paso', buttons=['SI :D', 'Volver a Intentar :C']) == 'SI :D':
                return x, y
        while True:
            pyautogui.alert(text=mensaje, title=f'ATS {paso} Paso', button='Claro que si!!! :O')
            time.sleep(3)
            x, y = pyautogui.position()
            pyautogui.alert(text='Ubicación guardada', title=f'ATS {paso} Paso', button='YES!!!')
            pyautogui.moveTo(x, y, 3)
            if pyautogui.confirm(text=confirmacion, title=f'ATS {paso} Paso', buttons=['SI :D', 'Volver a Intentar :C']) == 'SI :D':
                guardar_posicion(paso, x, y)
                return x, y

    def bienvenida():
        pyautogui.alert(text='Gracias por utilizar App-Ats nos sentimos muy alegres de poder contar contigo.\nPara empezar es necesario hacer un ajuste de resoluciones de las ventanas principales', title='Bienvenida-Ats', button='Super :D')
        pyautogui.alert(text='Vamos a necesitar que abras chrome y vayas a whatsapp \n Ten presente no mover las pestañas y seguir las siguientes instrucciones', title='Datos BasicosAts', button='Si señor XD')
        pyautogui.alert(text='Pon la pantalla en grande y sigue las siguientes instrucciones', title='Datos BasicosAts', button='Claro que si!!! :O')

    def configurar_ubicaciones():
        # Paso 1: Detección del Cierre Ventana
        ejecutar_paso(
            1,
            '1- Coloca el mouse en la X de cerrar ventana, por favor no des click para que cierres la ventana \n no cambies la ubicación hasta que pasen 5 segundos \n luego veras que el mouse se va a dirigir automáticamente al lugar donde quedó guardado',
            '¿El mouse se dirigió hacia el botón de cerrar?'
        )

        # Paso 2: Detección de escribir Chat en Whatsapp
        ejecutar_paso(
            2,
            '2- En la app de Whatsapp por favor coloca el mouse en Buscar',
            '¿El mouse se dirigió hacia donde indica la instrucción?'
        )

        # Paso 3: Detección de Chat en Whatsapp
        ejecutar_paso(
            3,
            '3- Ahora colócate en el primer chat que esté abierto',
            '¿El mouse se dirigió hacia donde indica la instrucción?'
        )

        # Paso 4: Nuevo Chat en Whatsapp
        while True:
            pyautogui.click()
            nuevoChat()    
            escribirMensaje("3004092105")
            xmouse4, ymouse4 = ejecutar_paso(
                4,
                '4- Ahora el nuevo Chat está abierto, dirígete a donde esté la primera conversación.',
                '¿El mouse se dirigió hacia donde indica la instrucción?'
            )
            if xmouse4 and ymouse4:
                break

        # Paso 5: Detección de Chat en Whatsapp
        pyautogui.click(xmouse4, ymouse4)
        ejecutar_paso(
            5,
            '5- Ahora colócate en el donde envías mensajes.',
            '¿El mouse se dirigió hacia donde indica la instrucción?'
        )

    def main():
        bienvenida()
        configurar_ubicaciones()
        pyautogui.alert(text='Acabamos fue más rápido de lo esperado.', title='ATS Guardado de Datos', button='¡¡¡Ya era hora!!! :D :D :D')

    if __name__ == '__main__':
        main()
