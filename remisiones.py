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
    esperarSegundos(3)
    escribirMensaje(numeroremision)
    teclaEnter()
    variasVecesTeclas(flechaAbajo,9,0.5)
    esperarSegundos(2)
    controlC()  
    esperarSegundos(1)
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
    variasVecesTeclas(flechaAbajo,2,1)
    irNumeroVentana(3)
    cerrarpestaña()
    irNumeroVentana(3)
    cerrarpestaña()
    irNumeroVentana(1)
    esperarSegundos(1)
    irNumeroVentana(2)
    cerrarpestaña()
    
    
    
    

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

    enviarMouse(xmouse4,ymouse4)
    clickIzquierdo()
    enviarMouse(xmouse5,ymouse5)
    clickIzquierdo()
    
    controlv()
    esperarSegundos(1)
    teclaEnter()





    esperarSegundos(1)
    enviarMouse(xmouse5,ymouse5)
    clickIzquierdo()
    
    volverAtras()
    teclaEnter()
    
    flechaAbajo()
    teclaEnter()
    esperarSegundos(2)
    variasVecesTeclas(teclaTab,9,1)
    esperarSegundos(1)
    teclaDerecha()
    teclaIzquierda()
    esperarSegundos(1)    
    teclaEnter()
    esperarSegundos(6)
    teclaEnter()
    esperarSegundos(3)
    archivarchat()
    esperarSegundos(5)
    cerrarpestaña()
    esperarSegundos(5)
    
    marcarComoHecho()
    

    



