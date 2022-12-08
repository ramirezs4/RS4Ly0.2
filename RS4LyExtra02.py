from colorama import Back, Fore, Style, init
import os
init()

#Limpiar pantalla
def LimpiarPantalla():
    if os.name == "posix": os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos": os.system ("cls")


#Para cambiar estilo de letras

SB=Style.BRIGHT

SR=Style.RESET_ALL

#SB=Fore.MAGENTA

#SR=Fore.RESET

#Para cambiar colores de letra
CY=Fore.YELLOW

CA=Fore.BLUE

CG=Fore.GREEN

CGL=Fore.LIGHTGREEN_EX

CR=Fore.RED

CRL=Fore.LIGHTRED_EX

CM=Fore.MAGENTA

CB=Fore.BLACK

CBL=Fore.WHITE

FC=Fore.CYAN

FR=Fore.RESET

#Para cambiar colores de fondo
BR=Back.RED

BC=Back.CYAN

BG=Back.GREEN

BF=Back.RESET
def Logo():
    print(BC+"""
            ____  ____  _  _   _          
            |  _ \/ ___|| || | | |   _   _ 
            | |_) \___ \| || |_| |  | | | |
            |  _ < ___) |__   _| |__| |_| |
            |_| \_\____/   |_| |_____\__, |
                                    |___/  Bienvenid@s
                                    """+BF)

def Logo_Opcion1():
    print(BC+"""
    ____  ____  _  _   _          
    |  _ \/ ___|| || | | |   _   _ 
    | |_) \___ \| || |_| |  | | | |
    |  _ < ___) |__   _| |__| |_| |
    |_| \_\____/   |_| |_____\__, |
                            |___/  Analizar IP
                            """+BF)