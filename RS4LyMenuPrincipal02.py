from RS4LyConexiones02 import CambioDeKeys
from RS4LyExtra02 import LimpiarPantalla,BC,BF,CBL,FR,BF,CM,CG,CGL,CY,CR,Logo,Logo_Opcion1
from RS4LyOpcionesDelMenu02 import Opcion1_IP,Menu_Conexiones


Logo()

RevisarCambioDeKey=CambioDeKeys()

if RevisarCambioDeKey !="0":
    LimpiarPantalla()
    Logo()
    print(
        CM+"Menu Principal\n"+FR,
        CG+"1 Analisis de ip\n"+FR,
        "2-Analisis de red(/24 o mayor)(No disponible)\n",
        "3-Analisis de url(No disponible)\n",
        "4-Analisis de archivos(No disponible)\n",
        CG+"5-Verificar conexiones y keys personales\n"+FR,
        CG+"0-Salir\n"+FR
        )
    Eleccion=input("Seleccione una opcion ---> ")
    
    while Eleccion !="0":

        if Eleccion == "1":
            Opcion1_IP()
            
        
        if Eleccion == "5":
            Menu_Conexiones()
            
        if Eleccion == "0":
            break
            
        else:
            print("La opcion seleccionada en estos momentos no se encuentra disponible")
    
        LimpiarPantalla()
        Logo()
        print(
            CM+"Menu Principal\n"+FR,
            CG+"1 Analisis de ip\n"+FR,
            "2-Analisis de red(/24 o mayor)(No disponible)\n",
            "3-Analisis de url(No disponible)\n",
            "4-Analisis de archivos(No disponible)\n",
            CG+"5-Verificar conexiones y keys personales\n"+FR,
            CG+"0-Salir\n"+FR
            )
        Eleccion=input("Seleccione una opcion ---> ")
    else:
        print("Saliendo")
        exit
        
else:
    print("Saliendo")


