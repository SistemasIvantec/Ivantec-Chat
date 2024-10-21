import pyperclip
from comandos import *
from linksDeNavegacion import *
from resolucionPantalla import *





def abrirpestañaLTask(id_Tarea):
    nuevapestaña()
    escribirMensaje(baseLtalsk)
    teclaEnter()
    esperarSegundos(5)
    buscarEnSheets()
    escribirMensaje(id_Tarea)
    esperarSegundos(0.5)
    teclaEnter()
    esperarSegundos(2)
    teclaEsc()
    esperarSegundos(0.5)
    enviarnotificacionTarea(id_Tarea)
    
    
def enviarnotificacionTarea(id_Tarea):
    esperarSegundos(1)
    
    variasVecesTeclas(teclaIzquierda,1,0.3)
    controlC()
    esperarSegundos(2)
    numTelDestinatario=pyperclip.paste()
    esperarSegundos(2)
    
    variasVecesTeclas(teclaDerecha,2,0.3)
    esperarSegundos(2)
    controlC()
    enviarWhatsapp(numTelDestinatario, id_Tarea)

def enviarWhatsapp(numCel, id_tarea):
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
    esperarSegundos(3)
    teclaEnter()
    
    esperarSegundos(1)
    teclaBorrar()
    esperarSegundos(1)

    cerrarpestaña()

    marcarcomoEnviado(id_tarea)


def marcarcomoEnviado(id_tarea):
    irNumeroVentana(2)    
    cerrarpestaña()    
    esperarSegundos(0.5)
    nuevapestaña()
    escribirMensaje(baseLtalsk)
    teclaEnter()
    esperarSegundos(5)

    esperarSegundos(1)
    buscarEnSheets()
    escribirMensaje(id_tarea)
    teclaEnter()
    esperarSegundos(2)
    teclaEsc()
    esperarSegundos(0.5)
    variasVecesTeclas(teclaDerecha,2,0.3)
    escribirMensaje("ok")
    teclaEnter()
    esperarSegundos(1)
    cerrarpestaña()

    

    

    
esperarSegundos(5)

