import pyperclip
from comandos import *
from linksDeNavegacion import *
from resolucionPantalla import *

<<<<<<< HEAD
=======




>>>>>>> 603de4d88da8eded7a5cecf36445a7454aa9f049
def enviosPrinc(numRemision):
    print(numRemision)
    
    nuevapestaña()
    escribirMensaje(baseGuias)
    esperarSegundos(1)
    teclaEnter()
<<<<<<< HEAD
    esperarSegundos(4)
    variasVecesTeclas(teclaDerecha,7,1)
=======
    esperarSegundos(5)
    buscarEnSheets()
    esperarSegundos(1)
    escribirMensaje(numRemision)
    teclaEnter()
    esperarSegundos(1)
    teclaEsc()
    esperarSegundos(2)
    variasVecesTeclas(teclaDerecha,2,1)
>>>>>>> 603de4d88da8eded7a5cecf36445a7454aa9f049
    controlC()
    numeroCel=pyperclip.paste()
    print(numeroCel)
    nuevapestaña()
    escribirMensaje(linkwhatsapp)
    teclaEnter()

    for i in range (7):
        print(i)
        esperarSegundos(1)
    nuevoChat()
    esperarSegundos(3)
    escribirMensaje(numeroCel)
    esperarSegundos(4)
    
    posiciones = cargar_posiciones()
    print(posiciones)
    #Nuevo Chat
    xmouse4, ymouse4 = posiciones["4"]["x"], posiciones["4"]["y"]
    #Escribir Cha
    xmouse5, ymouse5 = posiciones["5"]["x"], posiciones["5"]["y"]    
    
    enviarMouse(xmouse4,ymouse4)
    clickIzquierdo()
    enviarMouse(xmouse5,ymouse5)
    clickIzquierdo()
    irNumeroVentana(2)
    esperarSegundos(2)
    variasVecesTeclas(teclaDerecha,3,1)
    esperarSegundos(1)
    controlC()
    irNumeroVentana(3)
    enviarMouse(xmouse5,ymouse5)
    clickIzquierdo()
    controlv()    
    esperarSegundos(1)
    teclaEnter()
    irNumeroVentana(2)
    variasVecesTeclas(volverAtras,2,0.7)
    abrirvinculo()
    esperarSegundos(3)
    controlC()
    cerrarpestaña()
    esperarSegundos(2)
    irNumeroVentana(3)
    esperarSegundos(5)
    enviarMouse(xmouse5,ymouse5)
    clickIzquierdo()
    controlv()
    esperarSegundos(2)
    teclaEnter()
    esperarSegundos(5)
    archivarchat()
<<<<<<< HEAD
=======
    esperarSegundos(5)
    cerrarpestaña()
    esperarSegundos(5)
>>>>>>> 603de4d88da8eded7a5cecf36445a7454aa9f049
    marcarComoHecho(numRemision)
def marcarComoHecho(numRemision):
    irNumeroVentana(2)
    variasVecesTeclas(volverAtras,8,0.7)
    controlC()
    movmiento=pegarEnVariable()
    if movmiento == numRemision:
        print("Verificacion Hecha OK")
        variasVecesTeclas(teclaDerecha,4,0.7)
        controlC()
        marcarBase= pegarEnVariable()
        if marcarBase == "1-ALISTAMIENTO":
            abrirUrl()
            escribirMensaje(guias)
            teclaEnter()
            esperarSegundos(5)
            buscarEnSheets()
            escribirMensaje(numRemision)
            variasVecesTeclas(teclaTab,2,1)
            flechaAbajo()
            esperarSegundos(1)
            flechaAbajo()
            esperarSegundos(1)
            teclaEnter()
            variasVecesTeclas(teclaTab,7,1)
            teclaEnter()
            esperarSegundos(2)
            teclaEsc()
            esperarSegundos(1)
            variasVecesTeclas(teclaTab,7,1)
            escribirMensaje("Enviado alistado")
            esperarSegundos(1)
            teclaEnter()
            esperarSegundos(1)
            cerrarpestaña()
            irNumeroVentana(1)
            acutalizacionFinal(numRemision)
        elif marcarBase == "2-EMPACADO":
            abrirUrl()
            escribirMensaje(guias)
            teclaEnter()
            esperarSegundos(5)
            buscarEnSheets()
            escribirMensaje(numRemision)
            variasVecesTeclas(teclaTab,2,1)
            flechaAbajo()
            esperarSegundos(1)
            flechaAbajo()
            esperarSegundos(1)
            teclaEnter()
            variasVecesTeclas(teclaTab,7,1)
            teclaEnter()
            esperarSegundos(2)
            teclaEsc()
            esperarSegundos(1)
            variasVecesTeclas(teclaTab,10,1)
            escribirMensaje("Enviado empacado")
            esperarSegundos(1)
            teclaEnter()
            esperarSegundos(1)
            cerrarpestaña()
            irNumeroVentana(1)
            acutalizacionFinal(numRemision)
        elif marcarBase =="3-GUIAS":
            abrirUrl()
            escribirMensaje(guias)
            teclaEnter()
            esperarSegundos(5)
            buscarEnSheets()
            escribirMensaje(numRemision)
            variasVecesTeclas(teclaTab,2,1)
            flechaAbajo()
            esperarSegundos(1)
            flechaAbajo()
            esperarSegundos(1)
            teclaEnter()
            variasVecesTeclas(teclaTab,7,1)
            teclaEnter()
            esperarSegundos(2)
            teclaEsc()
            esperarSegundos(1)
            variasVecesTeclas(teclaTab,14,1)
            escribirMensaje("Enviado Guia")
            esperarSegundos(1)
            teclaEnter()
            esperarSegundos(1)
            esperarSegundos(2)
            cerrarpestaña()
            irNumeroVentana(1)
            acutalizacionFinal(numRemision)
def acutalizacionFinal (numRemision):
    print(numRemision," Ingreso al final")
    esperarSegundos(1)

    nuevapestaña()
    esperarSegundos(1)
    escribirMensaje(tablaDinamicaGuia)
    teclaEnter()
    for i in range (7):
        esperarSegundos(1)
        print("Segundo Actualizar ", i)
    cerrarpestaña()
    irNumeroVentana(1)
    

<<<<<<< HEAD

    
=======
>>>>>>> 603de4d88da8eded7a5cecf36445a7454aa9f049
