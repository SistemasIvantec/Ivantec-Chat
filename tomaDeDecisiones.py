from comandos import *
from linksDeNavegacion import *
import pyperclip
from remisiones import *
from enviosPrincipal import *

abrirInicioYAbrirChrome()
esperarSegundos(3)
escribirMensaje(tomaDeDecisiones)
teclaEnter()


while True:
    print("nuevavuelta")
    

    esperarSegundos(4)
    controlC()  
    filaDeEspera=pyperclip.paste()  

    print(filaDeEspera[:5])
    
    if filaDeEspera[:5] == "Filas":
        print("HOLI :D :D :D")
        for i in range (60):
            esperarSegundos(1)
            print(i)
    elif filaDeEspera[:4] == "NTF-":
        filaDeEspera=filaDeEspera
        enviosPrinc(filaDeEspera)
        

   

    elif filaDeEspera[:6] == "XO IVT":
        filaDeEspera=filaDeEspera
        remisionesPrinc(filaDeEspera)

    