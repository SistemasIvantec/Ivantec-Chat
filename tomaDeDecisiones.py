from comandos import *
from linksDeNavegacion import *
import pyperclip
from remisiones import *
from enviosPrincipal import *
from Recepcion import *
from SegundoNivelRecp import *

abrirInicioYAbrirChrome()                                   


esperarSegundos(4)      
escribirMensaje(tomaDeDecisiones)                                   


teclaEnter()                                    





while True:

    esperarSegundos(2)
    actualizarf5()
    esperarSegundos(8)

    
    teclaEsc()
    print("nuevavuelta")
    

    esperarSegundos(5)
    controlC()  
    filaDeEspera=pyperclip.paste()  

    print(filaDeEspera[:5])
    if filaDeEspera[:5] == "Filas" :
        print("HOLI :D :D :D")
        for i in range (60):
            esperarSegundos(1)
            print(i)
#Guias
    elif filaDeEspera[:4] == "NTF-":
        filaDeEspera=filaDeEspera
        enviosPrinc(filaDeEspera)
#Remisiones
    elif filaDeEspera[:6] == "XO IVT":
        filaDeEspera=filaDeEspera
        abrirpestaña(filaDeEspera)
#Tareas Recepcion    
    elif filaDeEspera[:6] == "TASK I":
        filaDeEspera=filaDeEspera
        abrirpestañaTask(filaDeEspera)
#Tareas Segundo Nivel
    elif filaDeEspera[:6] == "LTASK ":
        filaDeEspera=filaDeEspera
        abrirpestañaLTask(filaDeEspera)
    