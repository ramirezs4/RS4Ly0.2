from RS4LyAPIKEYS02 import ApiKey_IP_AbstractApi,ApiKey_IP_Abuse_DB,ApiKey_Virus_Total,ApiKey_IP_Quality_Score
from RS4LyManualDeUso02 import Guia_Añadir_Apis
from RS4LyExtra02 import LimpiarPantalla,CRL,CR,FR,CGL,CG,BR,BG,BF,BC,FC,CM,CY
import os
import requests
import json



            

#Verificar que las Keys personales esten de manera correcta:
def Verificacion_General_De_Keys():
    
    def Verificar_Key_VT():
        LinkDeLaApi="https://www.virustotal.com/vtapi/v2/ip-address/report"
        IP1="0.0.0.0"
        he={'apikey': ApiKey_Virus_Total, 'ip':IP1}
        DataDeVT2=requests.get(url=LinkDeLaApi, params=he)
        Correcta=00
        for Correcta in DataDeVT2:
            resultado="Si"
            break
        else:
            resultado="No"
            
        return(resultado)
    
    def Verificar_Key_IPADB():
        LinkDeLaApi="https://api.abuseipdb.com/api/v2/check"
        IP1="0.0.0.0"
        IP1={'ipAddress': IP1}
        he={"Accept":"application\json","key":ApiKey_IP_Abuse_DB}
        DataDeIpAbuseDb1=requests.get(url=LinkDeLaApi,headers=he,params=IP1)
        #Activar este print si quiere ver el codigo de estatus (200=correcta)
        #print(DataDeIpAbuseDb1)
        #Exception has occurred: JSONDecodeError
        #Expecting value
        try:
            DataDeIpAbuseDb1=json.loads(DataDeIpAbuseDb1.text)
            DataDeIpAbuseDb1="Si"
        except ValueError:
            DataDeIpAbuseDb1="No"
                    
        return(DataDeIpAbuseDb1)

    def Verificar_Key_IPQS():
        LinkDeLaApi="https://ipqualityscore.com/api/json/ip/"
        IP1="0.0.0.0"
        LinkFinal=LinkDeLaApi+ApiKey_IP_Quality_Score+"/"+IP1
        DataDeIpQualityScore1=requests.get(url=LinkFinal)
        DataDeIpQualityScore1=json.loads(DataDeIpQualityScore1.text)
        if DataDeIpQualityScore1["message"]=='Invalid or unauthorized key. Please check the API key and try again.':
            Resultado="No"
        else:
            Resultado="Si"
        
        return(Resultado)
           
    def Verificar_Key_AA():
        LinkDeLaApi="https://ipgeolocation.abstractapi.com/v1/"
        IP1="0.0.0.0"
        LinkFinal=LinkDeLaApi+"?api_key="+ApiKey_IP_AbstractApi+"&ip_address="+IP1
        DataDeIpAbstractApi1=requests.get(url=LinkFinal)
        DataDeIpAbstractApi1=json.loads(DataDeIpAbstractApi1.text)
        try:
            if DataDeIpAbstractApi1["error"]["message"]=="Invalid API key provided." or DataDeIpAbstractApi1["error"]["message"]=="You have exceeded the requests per second allowed by your current plan. Visit the Abstract dashboard to upgrade for a higher limit.":
                DataDeIpAbstractApi1="No"
            else:
                DataDeIpAbstractApi1="Si"
        except KeyError:
            None
            
        return(DataDeIpAbstractApi1)

    VerificarKeyAA=Verificar_Key_AA()
    VerificarKeyIPQS=Verificar_Key_IPQS()
    VerificarKeyIPADB=Verificar_Key_IPADB()
    VerificarKeyVirusTotal=Verificar_Key_VT()
    
    
    def Respuestas(Valor):
        PosiblesResultados={
            10: BR+"Incorrecto"+BF,
            11: BG+"Correcto"+BF,
            1: CR+"Key de AbstractA incorrecta"+FR,
            2: CG+"Key de AbstractA correcta"+FR,
            3: CR+"Key de IP Abuse DB incorrecta"+FR,
            4: CG+"Key de IP Abuse DB correcta"+FR,
            5: CR+"Key de IP Quality Score incorrecta"+FR,
            6: CG+"Key de IP Quality Score correcta"+FR,
            7: CR+"Key de Virus Total incorrecta"+FR,
            8: CG+"Key de Virus Total correcta"+FR
        
        }
        return PosiblesResultados.get(Valor,"Revise nuevamente")

    if VerificarKeyAA =="No" or VerificarKeyIPADB =="No" or VerificarKeyIPQS =="No" or VerificarKeyVirusTotal =="No":
        Estado=Respuestas(10)
        if VerificarKeyAA=="No":
            VerificarKeyAA=Respuestas(1)
        else:
            VerificarKeyAA=Respuestas(2)
        if VerificarKeyIPADB=="No":
            VerificarKeyIPADB=Respuestas(3)
        else:
            VerificarKeyIPADB=Respuestas(4)
        if VerificarKeyIPQS=="No":
            VerificarKeyIPQS=Respuestas(5)
        else:
            VerificarKeyIPQS=Respuestas(6)
        if VerificarKeyVirusTotal=="No":
            VerificarKeyVirusTotal=Respuestas(7)
        else:
            VerificarKeyVirusTotal=Respuestas(8) 
    else:
        Estado=Respuestas(11)
        VerificarKeyAA=Respuestas(2)
        VerificarKeyIPADB=Respuestas(4)
        VerificarKeyIPQS=Respuestas(6)
        VerificarKeyVirusTotal=Respuestas(8)
            
    print(CM+"El resultado de la verificacion es el siguiente: "+FR,Estado,"\nDe manera individual:\n",VerificarKeyAA,"\n",VerificarKeyIPADB,"\n",VerificarKeyIPQS,"\n",VerificarKeyVirusTotal)
    input("\nPresione enter para continuar")
    exit
     
#Verificar que se cambiara el valor por defectos en las keys
def CambioDeKeys():
    if(ApiKey_IP_AbstractApi == "Key-Personal" or ApiKey_IP_Abuse_DB == "Key-Personal" or ApiKey_IP_Quality_Score == "Key-Personal" or ApiKey_Virus_Total == "Key-Personal"):
        print(CR+"Una de las Keys personales no ha sido insertada"+FR,"\n")
        print("Quiere obtener ayuda para insertar sus keys personales?\n"," 1","Si\n"," 2","No")
        ESO=input("--->  ")
        LimpiarPantalla()
        if ESO=="1":
            Guia_Añadir_Apis()
            print("Luego de completar sus keys personales puede volver a iniciar la herramienta, gracias")
            ESO=input("Para salir presione enter")
            if ESO=="0":
                return 0
            else:
                return 0
                
        else:
            LimpiarPantalla()
            print("Luego de completar sus keys personales puede volver a iniciar la herramienta, gracias")
            return 0
    else:
        return "V"
           
def PruebaDeConexion():
    #Paginas a la que se realiza ping 
    Ping1="www.abuseipdb.com"
    Ping2="www.ipqualityscore.com"
    Ping3="www.abstractapi.com"
    Ping4="www.virustotal.com"

        
    #Ping en el cual debe llegar el 100% de los paquetes
    RPing1=os.system("ping "+Ping1+" > nul")
    RPing2=os.system("ping "+Ping2+" > nul")
    RPing3=os.system("ping "+Ping3+" > nul")
    RPing4=os.system("ping "+Ping4+" > nul") 

    ValorBuscado="0"
    
    def Respuestas(Valor):
        PosiblesResultados={
            10: CR+"Almenos una conexion erronea"+FR,
            11: CG+"Conexiones exitosas"+FR,
            1: CR+"Conexion con AbstractA  incorrecta"+FR,
            2: CG+"Conexion con AbstractA  correcta"+FR,
            3: CR+"Conexion con IP Abuse DB incorrecta"+FR,
            4: CG+"Conexion con IP Abuse DB correcta"+FR,
            5: CR+"Conexion con IP Quality Score incorrecta"+FR,
            6: CG+"Conexion con IP Quality Score correcta"+FR,
            7: CR+"Conexion con Virus Total incorrecta"+FR,
            8: CG+"Conexion con Virus Total correcta"+FR
        
        }
        return PosiblesResultados.get(Valor,"Revise nuevamente")
    
    if RPing1 == "1" or RPing2 == "1" or RPing3 == "1" or RPing4 == "1":
        Estatus=Respuestas(10)
        if RPing1=="1":
            Ping1=Respuestas(3)
        else:
            Ping1=Respuestas(4)
        if RPing2=="1":
            Ping2=Respuestas(5)
        else:
            Ping2=Respuestas(6)
        if RPing3=="1":
            Ping3=Respuestas(1)
        else:
            Ping3=Respuestas(2)
        if RPing4=="1":
            Ping4=Respuestas(7)
        else:
            Ping4=Respuestas(8)
    else:
        Estatus=Respuestas(11)
        Ping1=Respuestas(4)
        Ping2=Respuestas(6)
        Ping3=Respuestas(8)
        Ping4=Respuestas(2)
    
    print(FC+"El resultado de la verificacion de conexiones es el siguiente: "+FR,Estatus,
          "\nDe manera individual:\n",Ping1,"\n",Ping2,"\n",Ping3,"\n",Ping4)

    input("\nPresione enter para continuar")
    exit

