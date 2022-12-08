from RS4LyAnálisisDeCondiciones02 import Puntuacion_GENERAL,Puntuacion_IPABUSEDB,Puntuacion_IPQUALITYSCORE,Puntuacion_IPVIRUSTOTAL,Num_De_Reportes,Num_De_Usuarios,Info_Geografica,Evaluar_Ultimo_Reporte,Todo_Ok,Trafico_NoHumano,Conexion_Proxy,Nodo_Tor,Limpiao_No1,Limpia_No2,Limpia_No3,Informacion_Resolucion,Urls_Detectadas
from RS4LyVerificacionDeDatos02 import Verificacion_Isp,Verificacion_Org,Verificacion_Pais,Verificacion_VPN,Verificar_infoGeografica
from RS4LyExtra02 import LimpiarPantalla,CM,FR,CG,CA,init,SB,SR,FC
init()



def Conjunto_Analisis_De_IP(IP1,Data1,Data2,Data3,Data4):
    #Traer los datos de las puntuaciones de riesgo tanto individual como general.
    PuntuacionIPabusedb=Puntuacion_IPABUSEDB(Data1)
    PuntuacionIPqualityscore=Puntuacion_IPQUALITYSCORE(Data2)
    PuntuacionIPvirustotal=Puntuacion_IPVIRUSTOTAL(Data3)
    Puntuaciongeneral=Puntuacion_GENERAL(Data1,Data2)
    
    
    LimpiarPantalla()
    #Resumen del analisis de IP
    print(
        CA+"El analisis de la direccion "+IP1+" arrojo los siguientes resultados:"+FR
        ,"\n a) La direccion pertenece a una red:",FC+"Publica"+FR
        ,"\n b) El nivel de riesgo general es:",Puntuaciongeneral
        ,CM+"\n\nFuentes:"+FR
        ,"\n 1) IP Abuse DB:",PuntuacionIPabusedb
        ,"\n 2) IP Quality Score:",PuntuacionIPqualityscore
        ,"\n 3) Virus Total:",PuntuacionIPvirustotal
    )
    
    print(CM+"\nOpciones Disponible:"+FR," \n 1)Ver informacion completa \n 2)Guardar la data en un documento(No disponible) \n 0)Volver Atras")
    AS=input("---> ")
    if AS=="1":
        LimpiarPantalla()
        TodoOk=Todo_Ok(Data1,Data2)
        if TodoOk=="0":
            print(
                CA+"El analisis de la direccion "+IP1+" arrojo los siguientes resultados:"+FR
                ,"\n a) La direccion pertenece a una red:",CG+"Publica"+FR
                ,CG+"\n b) La direccion esta limpia"+FR                
            )
        else:
            Analisis_De_IP_Completo(IP1,Data1,Data2,Data3,Data4,Puntuaciongeneral,PuntuacionIPabusedb,PuntuacionIPqualityscore,PuntuacionIPvirustotal)
            
    elif AS=="2":
        print("Opcion no disponible")
    else:
        exit
    

def Analisis_De_IP_Completo(IP1,Data1,Data2,Data3,Data4,Puntuaciongeneral,PuntuacionIPabusedb,PuntuacionIPqualityscore,PuntuacionIPvirustotal):
    LimpiarPantalla()
    NumeroUsuarios=Num_De_Usuarios(Data1)
    NumeroReportes=Num_De_Reportes(Data1)
    InfoGeografica=Info_Geografica(Data2)
    FeUltimoReporte=Evaluar_Ultimo_Reporte(Data1)
    
    #Informacion de geolocalizacion
    VerifiVPN=Verificacion_VPN(Data2,Data4)
    VerifiPais=Verificacion_Pais(Data4,Data2,Data1)
    VerifiOrg=Verificacion_Org(Data2,Data4)
    VerifiIsp=Verificacion_Isp(Data1,Data2,Data4)
    VerificarGeo=Verificar_infoGeografica(Data1,Data2,Data4)
    
    #bot,proxy,tor
    UnBot=Trafico_NoHumano(Data2)
    ConProxy=Conexion_Proxy(Data2)
    NodTor=Nodo_Tor(Data2)
    
    #Maliciosa o no
    LimpiaoNo1=Limpiao_No1(Data1)
    LimpiaNo2=Limpia_No2(Data2)
    LimpiaNo3=Limpia_No3(Data3)
        
    #Analisis de IP Completa
    print(
        CA+"El analisis de la direccion "+IP1+" arrojo los siguientes resultados:"+FR
        ,SB+"\n a)"+SR+" La direccion pertenece a una red:",CG+"Publica"+FR
        ,SB+"\n b)"+SR+" Usuarios que han reportado esta Ip:",NumeroUsuarios
        ,SB+"\n c)"+SR+" Numero de veces que se ha reportado esta ip:",NumeroReportes
        ,SB+"\n d)"+SR+" Desde la ultima vez que se reporto han pasado:",FeUltimoReporte
        ,SB+"\n e)"+SR+" El nivel de riesgo general es:",Puntuaciongeneral
        ,SB+"\n h)"+SR+" Tipo de uso: "+FC+Data1["data"]["usageType"]+FR
        ,SB+"\n f)"+SR+" Puede ser una conexion tipo:"+FC+" proxy "+FR+ConProxy,FC+"Nodo Tor "+FR+NodTor
        ,SB+"\n g)"+SR+" Es una conexion de tipo"+FC+" VPN:"+FR,VerifiVPN
        ,SB+"\n i)"+SR+" Presenta trafico no humano"+FC+" (bot)"+FR+": "+UnBot
        ,CM+"\n\nFuentes:"+FR
        ,SB+"\n 1)"+SR+" IP Abuse DB:",LimpiaoNo1+", Puntuacion de riesgo individual:",PuntuacionIPabusedb
        ,SB+"\n 2)"+SR+" IP Quality Score:",LimpiaNo2+", Puntuacion de riesgo individual:",PuntuacionIPqualityscore
        ,SB+"\n 3)"+SR+" Virus Total:",LimpiaNo3+", Puntuacion de riesgo individual:",PuntuacionIPvirustotal
        ,CM+"\n\nInformacion de Geolocalizacion:"+FR
        ,"\n 1) El ISP actual es:",VerifiIsp
        ,"\n 2) Nombre de la organizacion:",VerifiOrg
        ,"\n 3) El pais de origen es:",VerifiPais
        ,"\n 4) Informacion Geografica:",VerificarGeo
        ,"\n 5) Tipo de uso:",FC+Data1["data"]["usageType"]+FR
        ,"\n 6) El nombre del dominio es: "+FC+Data1["data"]["domain"]+FR   
    )
    
    Informacion_Resolucion(Data1,Data2,Data3)
    Urls_Detectadas(Data3)