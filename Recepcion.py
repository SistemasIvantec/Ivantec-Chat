import pyperclip
from comandos import *
from linksDeNavegacion import *
from resolucionPantalla import *

def abrirpestañaTask(id_Tarea):
    nuevapestaña()
    escribirMensaje(baseTareasMensaje)
    teclaEnter()
    esperarSegundos(5)
    variasVecesTeclas(teclaDerecha,5,0.3)
    controlC()
    esperarSegundos(2)
    id_task=pyperclip.paste()
    if id_task== id_Tarea:
        enviarnotificacionTarea(id_task)

    
    
def enviarnotificacionTarea():
    print("holi")
    variasVecesTeclas(teclaIzquierda,1,0.3)
    controlC()
    esperarSegundos(2)
    numTelDestinatario=pyperclip.paste()
    esperarSegundos(2)
    variasVecesTeclas(teclaDerecha,2,0.3)
    esperarSegundos(2)
    controlC()
    abrirwhatsapp()

