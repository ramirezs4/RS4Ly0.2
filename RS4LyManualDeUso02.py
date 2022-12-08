from RS4LyExtra02 import LimpiarPantalla,CR,FR


def Guia_Cambio_Color():
    LimpiarPantalla    
    print("""Cambiar Colores
    \nEn este apartado se le muestra cómo puede cambiar los colores del menú de toda la herramienta.\nNota: No puede modificar los colores rojos y verde al analizar una ip, url u otro.
    \nEn primer lugar, debe ir al módulo RS4LyExtra02
    
    \nEjemplos y casos de uso:
    \n 1) Si el color verde no es de su agrado o simplemente quiere que todo lo que este en verde sea de otro color, debe:
    \n  a) Buscar la variable que tiene el color verde. En este caso "CG".\n  b) Modifica la parte que esta después del punto, dejando siempre la primera parte igual "Fore."\n  c) Listo con esto ya debería tener el color del texto cambiado.
    \n 2) Si de igual manera quiere que los fondos de ciertos textos cambien es posible hacerlo.
    \n  a) Busca la variable que tiene el fondo que quiere cambiar, en este caso el Cian. "BC"\n  b) Modifica la parte que esta después del punto, dejando siempre la primera parte igual "Back."\n  c) Listo con esto ya debería tener el color del fondo cambiado.
    \n Extra:\n  También es posible que con estas mismas opciones pueda, por ejemplo, añadir negritas o aclarar el texto agregando la opción “style.” o modificar un color por negritas.""")
    
def Guia_Añadir_Apis():
    LimpiarPantalla
    print("""Añadir Apis Key
    \nEn este apartado se le muestra cómo añadir sus Apis key personales para el uso de la herramienta.
    
    \n a) En primer lugar, debe ir al módulo RS4LyAPIKEYS02
    \n b) Una vez se encuentre dentro del modulo vera que hasta el momento de escribir esto necesita 4 Apis diferente para trabajar con la herramienta, las mismas son de uso gratuito solo debera registrarse con una direccion de correo valida siguiendo los enlaces dejados.
    \n c) Mientras se registra en las diferentes plataformas puede verificar sobre los diferentes planes que tiene la misma, los limites de uso, entre otras informaciones importantes.
    \n d) Una vez registrado y con sus codigos apis personales solo debe copiar y reemplazar        
    
    """,
    CR+"Cuidado con crearse múltiples cuentas para pasar del uso diario gratuito, estas plataformas cuentan con sistemas de seguridad para detectar esto y la sanción que puede tener es el baneo permanente"+FR)
    
    print("""
        1.1 ApiKey_Virus_Total
            1)Link para registrarse https://www.virustotal.com/gui/join-us
            2)Link para ver su clave api y registros de uso https://www.virustotal.com/gui/user/"Su-usuario"/apikey

        1.2 ApiKey_IP_Abuse_DB
            1) #Para ver su key y las estadisticas de uso https://www.abuseipdb.com/account/api
            2) Una vez este en la pagina debe ir al apartado "API"
            3) Busque la opcion "Create Key" e ingresele el nombre que guste para identificarla
            4) Copie solamente el "Key"
        
        1.3 ApiKey_IP_Quality_Score
            1) Despues de creada su cuenta debe ir al link https://www.ipqualityscore.com/documentation/proxy-detection/overview
            2) Luego que la pagina cargue debe presional "Ctrl + F" esto abrira la herramienta de busqueda
            3) Ya abierta la herramienta de busqueda ingrese "Private Key"
            4) Esto le mostrara el apartado donde se encuentra su Key para la api
                   
        1.4 ApiKey_IP_AbstractApi
            1) Para encontrar su Key debe ir al link https://app.abstractapi.com/api/ip-geolocation/documentation
            2) Ir al apartado de "Documentation"
            3) Una vez en documentation en la parte superior vera un mensaje que dice "This is your private API key, specific to this API."
            4) Seguido de este mensaje esta su Key.
          """)
