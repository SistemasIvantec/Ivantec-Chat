import pyperclip
from comandos import *
from linksDeNavegacion import *
from resolucionPantalla import *

def abrirpestaña(numeroremision): 
    nuevapestaña()  
    escribirMensaje(linkwhatsapp)
    teclaEnter()
    nuevapestaña()
    escribirMensaje(remisiones)
    teclaEnter()
    esperarSegundos(5)
    escribirMensaje(numeroremision)
    esperarSegundos(4)
    teclaEnter()    
    variasVecesTeclas(flechaAbajo,9,0.5)
    esperarSegundos(3)
    controlC()  
    esperarSegundos(3)
    numeroCliente=pyperclip.paste()
    esperarSegundos(1)
    print("el numero es:" ,numeroCliente)
    descargarPdfdesdeGoogleSheets()
    enviarwhatsapp(numeroCliente)


def marcarComoHecho():
    nuevapestaña()
    escribirMensaje(listaMadraRemisionesColumnaL)
    teclaEnter()
    esperarSegundos(8)
    irAAbajo()
    esperarSegundos(1)
    flechaAbajo()
    escribirMensaje("SI")
    esperarSegundos(2)
    teclaEnter()
    teclaDerecha()
    teclaIzquierda()
    esperarSegundos(5)
    cerrarpestaña()
    esperarSegundos(2)
    irNumeroVentana(2)
    esperarSegundos(2)
    cerrarpestaña()
    esperarSegundos(2)
    irNumeroVentana(1)
    
    
    
    

def enviarwhatsapp(numero):
    
    nuevapestaña()
    escribirMensaje(textoAEnviarWhatsapp)
    teclaEnter()
    esperarSegundos(4)    
    controlC()
    cerrarpestaña()
    
    irNumeroVentana(2)
    esperarSegundos(3)
    nuevoChat()
    esperarSegundos(3)
    escribirMensaje(numero)
    esperarSegundos(4)
    posiciones = cargar_posiciones()

    
    #Nuevo Chat
    xmouse4, ymouse4 = posiciones["4"]["x"], posiciones["4"]["y"]
    #Escribir Cha
    xmouse5, ymouse5 = posiciones["5"]["x"], posiciones["5"]["y"]
    if xmouse4 and xmouse5 == "":
        central()        

    enviarMouse(xmouse4,ymouse4)
    clickIzquierdo()
    enviarMouse(xmouse5,ymouse5)
    clickIzquierdo()
    
    controlv()
    esperarSegundos(3)
    teclaEnter()





    esperarSegundos(3)
    enviarMouse(xmouse5,ymouse5)
    clickIzquierdo()
    esperarSegundos(0.3)
    volverAtras()
    esperarSegundos(1)
    teclaEnter()
    
    flechaAbajo()
    teclaEnter()
    esperarSegundos(3)
    variasVecesTeclas(teclaTab,9,1)
    esperarSegundos(2)
    teclaDerecha()
    teclaIzquierda()
    esperarSegundos(2)    
    teclaEnter()
    esperarSegundos(6)
    teclaEnter()
    esperarSegundos(3)
    archivarchat()
    esperarSegundos(10)
    cerrarpestaña()
    
    marcarComoHecho()
    

    



