import pyperclip
from comandos import *
from linksDeNavegacion import *
from resolucionPantalla import *

def enviosPrinc(numRemision):
    nuevapestaña()
    esperarSegundos
    escribirMensaje(guias)
    teclaEnter()
    esperarSegundos(5)
    buscarEnSheets()
    escribirMensaje(numRemision)
    esperarSegundos(1)
    teclaEnter()
    esperarSegundos(1)
    teclaEsc()
    esperarSegundos(1)
    controlC()
    esperarSegundos(2)
    numeroCliente=pyperclip.paste()
    esperarSegundos(2)
    teclaDerecha()
    teclaDerecha()
    esperarSegundos(2)
    controlC()
    tipoMovimiento=pyperclip.paste()

    teclaDerecha()
    controlC()
    whatsappEnviar(numeroCliente, numRemision,tipoMovimiento)
    
def whatsappEnviar(numeroCliente, numRemision, tipoMovimiento):
    abrirwhatsapp()
    esperarSegundos(2)
    nuevoChat()
    esperarSegundos(3)
    escribirMensaje(numeroCliente)
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

    irNumeroVentana(2)
    esperarSegundos(1)
    teclaIzquierda()
    teclaIzquierda()
    abrirvinculo()
    esperarSegundos(2)
    irNumeroVentana(3)
    esperarSegundos(3)
    enviarMouse(52,179)
    clickDerecho()
    esperarSegundos(3)
    flechaAbajo()
    flechaAbajo()
    flechaAbajo()
    teclaEnter()
    esperarSegundos(1)
    irNumeroVentana(4)

    enviarMouse(xmouse5,ymouse5)
    clickIzquierdo()
    controlv()
    esperarSegundos(1)
    teclaEnter()
    esperarSegundos(15)

    archivarchat()

    cerrarpestaña()
    esperarSegundos(1)
    cerrarpestaña()
    esperarSegundos(1)
    cerrarpestaña()
    esperarSegundos(1)
    marcarEnviado(numRemision, tipoMovimiento)


def marcarEnviado(numRemision, tipoMovimiento):
    if tipoMovimiento== "1-ALISTAMIENTO":
        abrirUrl()
        escribirMensaje(guiasMarcarHecho)
        teclaEnter()
        esperarSegundos(5)
        buscarEnSheets()
        esperarSegundos(1)
        escribirMensaje(numRemision)
        teclaEnter()
        esperarSegundos(2)
        teclaEsc()
        esperarSegundos(1)
        variasVecesTeclas(teclaDerecha,8,1)
        esperarSegundos(1)
        escribirMensaje("Envio Alistado")
        teclaDerecha()
    elif tipoMovimiento== "2-EMPACADO":
        abrirUrl()
        escribirMensaje(guiasMarcarHecho)
        teclaEnter()
        esperarSegundos(5)
        buscarEnSheets()
        esperarSegundos(1)
        escribirMensaje(numRemision)
        teclaEnter()
        esperarSegundos(2)
        teclaEsc()
        esperarSegundos(1)
        variasVecesTeclas(teclaDerecha,11,1)
        esperarSegundos(1)
        escribirMensaje("Envio Empacado")
        teclaDerecha()
    
    elif tipoMovimiento== "3-GUIAS":
        abrirUrl()
        escribirMensaje(guiasMarcarHecho)
        teclaEnter()
        esperarSegundos(5)
        buscarEnSheets()
        esperarSegundos(1)
        escribirMensaje(numRemision)
        teclaEnter()
        esperarSegundos(2)
        teclaEsc()
        esperarSegundos(1)
        variasVecesTeclas(teclaDerecha,15,1)
        esperarSegundos(1)
        escribirMensaje("Enviado Guia")
        teclaDerecha()


    esperarSegundos(8)
    abrirUrl()
    esperarSegundos(1)
    escribirMensaje(tomaDeDecisiones)
    teclaEnter()
    esperarSegundos(8)
    




