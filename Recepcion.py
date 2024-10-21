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
    enviarWhatsapp(numTelDestinatario)

def enviarWhatsapp(numCel):
    abrirwhatsapp()
    esperarSegundos(1)
    nuevoChat()
    esperarSegundos(3)
    escribirMensaje(numCel)
    esperarSegundos(4)
    posiciones = cargar_posiciones()

    
    #Nuevo Chat
    xmouse4, ymouse4 = posiciones["4"]["x"], posiciones["4"]["y"]
    #Escribir Cha
    xmouse5, ymouse5 = posiciones["5"]["x"], posiciones["5"]["y"]

    enviarMouse(xmouse4,ymouse4)
    clickIzquierdo()
    enviarMouse(xmouse5,ymouse5)
    clickIzquierdo()
    
    controlv()
    esperarSegundos(1)
    teclaEnter()

    cerrarpestaña()

    marcarcomoEnviado()


def marcarcomoEnviado():
    irNumeroVentana(2)    
    
    

    
esperarSegundos(5)

abrirpestañaTask("TASK IVTJUAN ORJUELA3057960502")