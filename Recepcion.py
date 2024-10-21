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
    print(id_Tarea+" "+id_task)
    if id_task==id_Tarea:
        enviarnotificacionTarea(id_task)

    
    
def enviarnotificacionTarea(id_task):
    print("holi")
    variasVecesTeclas(teclaIzquierda,1,0.3)
    controlC()
    esperarSegundos(2)
    numTelDestinatario=pyperclip.paste()
    esperarSegundos(2)
    #Copia fecha para buscar
    variasVecesTeclas(teclaIzquierda,4,0.3)
    esperarSegundos(2)
    controlC()
    idPorFechaDestinatario=pyperclip.paste()  
    esperarSegundos(1)
    variasVecesTeclas(teclaDerecha,6,0.3)
    esperarSegundos(2)
    controlC()
    enviarWhatsapp(numTelDestinatario,idPorFechaDestinatario)

def enviarWhatsapp(numCel,fecha):
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

    marcarcomoEnviado(fecha)


def marcarcomoEnviado(fecha):
    irNumeroVentana(2)    
    cerrarpestaña()    
    esperarSegundos(0.5)
    nuevapestaña()
    escribirMensaje(baseTareasMensaje)
    teclaEnter()
    esperarSegundos(5)

    esperarSegundos(1)
    buscarEnSheets()
    escribirMensaje(fecha)
    teclaEnter()
    esperarSegundos(2)
    teclaEsc()
    esperarSegundos(0.5)
    variasVecesTeclas(teclaDerecha,8,0.3)
    escribirMensaje("ok")
    teclaEnter()
    esperarSegundos(1)
    cerrarpestaña()

    

    

    
esperarSegundos(5)

abrirpestañaTask("TASK IVTJUAN ORJUELA3057960502")