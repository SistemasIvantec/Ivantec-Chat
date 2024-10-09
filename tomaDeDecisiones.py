<<<<<<< HEAD
=======

>>>>>>> 603de4d88da8eded7a5cecf36445a7454aa9f049
from comandos import *
from linksDeNavegacion import *
import pyperclip
from remisiones import *
from enviosPrincipal import *

<<<<<<< HEAD
abrirInicioYAbrirChrome()
esperarSegundos(3)
escribirMensaje(tomaDeDecisiones)
teclaEnter()


while True:
    print("nuevavuelta")
    

    esperarSegundos(4)
=======

abrirInicioYAbrirChrome()                                   


esperarSegundos(4)      
escribirMensaje(tomaDeDecisiones)                                   


teclaEnter()                                    





while True:
    esperarSegundos(8)                                  

    
    teclaEsc()
    print("nuevavuelta")
    

    esperarSegundos(5)
>>>>>>> 603de4d88da8eded7a5cecf36445a7454aa9f049
    controlC()  
    filaDeEspera=pyperclip.paste()  

    print(filaDeEspera[:5])
<<<<<<< HEAD
    
    if filaDeEspera[:5] == "Filas":
=======
    if filaDeEspera[:5] == "Filas" :
>>>>>>> 603de4d88da8eded7a5cecf36445a7454aa9f049
        print("HOLI :D :D :D")
        for i in range (60):
            esperarSegundos(1)
            print(i)
<<<<<<< HEAD
    elif filaDeEspera[:4] == "NTF-":
        filaDeEspera=filaDeEspera
        enviosPrinc(filaDeEspera)
        

   

    elif filaDeEspera[:6] == "XO IVT":
        filaDeEspera=filaDeEspera
        remisionesPrinc(filaDeEspera)

=======

    elif filaDeEspera[:4] == "NTF-":
        filaDeEspera=filaDeEspera
        enviosPrinc(filaDeEspera)

    elif filaDeEspera[:6] == "XO IVT":
        filaDeEspera=filaDeEspera
        abrirpestaña(filaDeEspera)
>>>>>>> 603de4d88da8eded7a5cecf36445a7454aa9f049
    