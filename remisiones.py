import pyperclip
from comandos import *
from linksDeNavegacion import *
from resolucionPantalla import *

<<<<<<< HEAD
def remisionesPrinc(numeroremision): 
=======
def abrirpestaña(numeroremision): 
>>>>>>> 603de4d88da8eded7a5cecf36445a7454aa9f049
    nuevapestaña()  
    escribirMensaje(linkwhatsapp)
    teclaEnter()
    nuevapestaña()
    escribirMensaje(remisiones)
    teclaEnter()
<<<<<<< HEAD
    esperarSegundos(3)
    escribirMensaje(numeroremision)
    teclaEnter()
    variasVecesTeclas(flechaAbajo,9,0.5)
    controlC()  
    esperarSegundos(1)
=======
    esperarSegundos(5)
    escribirMensaje(numeroremision)
    esperarSegundos(4)
    teclaEnter()    
    variasVecesTeclas(flechaAbajo,9,0.5)
    esperarSegundos(3)
    controlC()  
    esperarSegundos(3)
>>>>>>> 603de4d88da8eded7a5cecf36445a7454aa9f049
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
<<<<<<< HEAD
    variasVecesTeclas(flechaAbajo,2,1)
    irNumeroVentana(3)
    cerrarpestaña()
    irNumeroVentana(3)
    cerrarpestaña()
    irNumeroVentana(1)
    esperarSegundos(1)
    irNumeroVentana(2)
    cerrarpestaña()
=======
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
>>>>>>> 603de4d88da8eded7a5cecf36445a7454aa9f049
    
    
    
    

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
<<<<<<< HEAD

=======
    if xmouse4 and xmouse5 == "":
        central()        
>>>>>>> 603de4d88da8eded7a5cecf36445a7454aa9f049

    enviarMouse(xmouse4,ymouse4)
    clickIzquierdo()
    enviarMouse(xmouse5,ymouse5)
    clickIzquierdo()
    
    controlv()
<<<<<<< HEAD
    esperarSegundos(1)
=======
    esperarSegundos(3)
>>>>>>> 603de4d88da8eded7a5cecf36445a7454aa9f049
    teclaEnter()





<<<<<<< HEAD
    esperarSegundos(1)
    enviarMouse(xmouse5,ymouse5)
    clickIzquierdo()
    
    volverAtras()
=======
    esperarSegundos(3)
    enviarMouse(xmouse5,ymouse5)
    clickIzquierdo()
    esperarSegundos(0.3)
    volverAtras()
    esperarSegundos(1)
>>>>>>> 603de4d88da8eded7a5cecf36445a7454aa9f049
    teclaEnter()
    
    flechaAbajo()
    teclaEnter()
<<<<<<< HEAD
    esperarSegundos(2)
    variasVecesTeclas(teclaTab,9,1)
    esperarSegundos(1)
    teclaDerecha()
    teclaIzquierda()
    esperarSegundos(1)    
=======
    esperarSegundos(3)
    variasVecesTeclas(teclaTab,9,1)
    esperarSegundos(2)
    teclaDerecha()
    teclaIzquierda()
    esperarSegundos(2)    
>>>>>>> 603de4d88da8eded7a5cecf36445a7454aa9f049
    teclaEnter()
    esperarSegundos(6)
    teclaEnter()
    esperarSegundos(3)
    archivarchat()
<<<<<<< HEAD
=======
    esperarSegundos(10)
    cerrarpestaña()
>>>>>>> 603de4d88da8eded7a5cecf36445a7454aa9f049
    
    marcarComoHecho()
    

    



