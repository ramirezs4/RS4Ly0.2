from RS4LyExtra02 import CB,CR,CBL,FR,CG,CGL,CRL,FC,CM,CY,CRL,SB,SR
from RS4LyVerificacionDeDatos02 import Verificacion_Hostname
from datetime import datetime


#Analizar si la ip es valida
def Validar_IP(Data1):
    try:
        if(Data1['data']['isPublic']==True):
            ValidarIP="Publica"
            return ValidarIP
        else:
            ValidarIP="Privada"
            return ValidarIP
    except KeyError:
        ValidarIP="No valida"
        return ValidarIP
    
#Puntuacion de abuso
def Puntuacion_IPABUSEDB(Data1):
    A=Data1["data"]['abuseConfidenceScore']
    while(A>0):
        if(A<20):
            return Posibles_Puntuaciones(2)
        elif(A<30):
            return Posibles_Puntuaciones(3)
        elif(A<40):
            return Posibles_Puntuaciones(4)
        elif(A<50):
            return Posibles_Puntuaciones(5)
        elif(A<60):
            return Posibles_Puntuaciones(6)
        elif(A<70):
            return Posibles_Puntuaciones(7)
        elif(A<80):
            return Posibles_Puntuaciones(8)
        elif(A<90):
            return Posibles_Puntuaciones(9)
        elif(A>=90):
            return Posibles_Puntuaciones(10)
    else:
        return Posibles_Puntuaciones(1)
    
def Puntuacion_IPQUALITYSCORE(Data2):
    A=Data2["fraud_score"]
    while(A>0):
        if(A<20):
            return Posibles_Puntuaciones(2)
        elif(A<30):
            return Posibles_Puntuaciones(3)
        elif(A<40):
            return Posibles_Puntuaciones(4)
        elif(A<50):
            return Posibles_Puntuaciones(5)
        elif(A<60):
            return Posibles_Puntuaciones(6)
        elif(A<70):
            return Posibles_Puntuaciones(7)
        elif(A<80):
            return Posibles_Puntuaciones(8)
        elif(A<90):
            return Posibles_Puntuaciones(9)
        elif(A>=90):
            return Posibles_Puntuaciones(10)
    else:
        return Posibles_Puntuaciones(1)

def Puntuacion_IPVIRUSTOTAL(Data3):
    try:
        A=(len(Data3["detected_urls"]))
        while(A>0):
            if(A<20):
                return Posibles_Puntuaciones(2)
            elif(A<30):
                return Posibles_Puntuaciones(3)
            elif(A<40):
                return Posibles_Puntuaciones(4)
            elif(A<50):
                return Posibles_Puntuaciones(5)
            elif(A<60):
                return Posibles_Puntuaciones(6)
            elif(A<70):
                return Posibles_Puntuaciones(7)
            elif(A<80):
                return Posibles_Puntuaciones(8)
            elif(A<90):
                return Posibles_Puntuaciones(9)
            elif(A>=90):
                return Posibles_Puntuaciones(10)
        else:
            return Posibles_Puntuaciones(1)
        
    except KeyError:
        PuntuacionIPabusedb=CG+"0-Muy Bajo"+FR
        return PuntuacionIPabusedb
 
def Todo_Ok(Data1,Data2):
    A=Data1["data"]['abuseConfidenceScore']
    B=Data2["fraud_score"]

    while(A>0 or B>0):
        if(A<20 and B<20):
            return Posibles_Puntuaciones(2)
        elif(A<30 and B<30):
            return Posibles_Puntuaciones(3)
        elif(A<40 and B<40):
            return Posibles_Puntuaciones(4)
        elif(A<50 and B<50):
            return Posibles_Puntuaciones(5)
        elif(A<60 and B<60):
            return Posibles_Puntuaciones(6)
        elif(A<70 or B<70):
            return Posibles_Puntuaciones(7)
        elif(A<80 or B<80):
            return Posibles_Puntuaciones(8)
        elif(A<90 or B<90):
            return Posibles_Puntuaciones(9)
        elif(A>=90 or B>=90):
            return Posibles_Puntuaciones(10)
    else:
        return 0

def Puntuacion_GENERAL(Data1,Data2):
    A=Data1["data"]['abuseConfidenceScore']
    B=Data2["fraud_score"]

    while(A>1 or B>1):
        if(A<20 and B<20):
            return Posibles_Puntuaciones(2)
        elif(A<30 and B<30):
            return Posibles_Puntuaciones(3)
        elif(A<40 and B<40):
            return Posibles_Puntuaciones(4)
        elif(A<50 and B<50):
            return Posibles_Puntuaciones(5)
        elif(A<60 and B<60):
            return Posibles_Puntuaciones(6)
        elif(A<70 or B<70):
            return Posibles_Puntuaciones(7)
        elif(A<80 or B<80):
            return Posibles_Puntuaciones(8)
        elif(A<90 or B<90):
            return Posibles_Puntuaciones(9)
        elif(A>=90 or B>=90):
            return Posibles_Puntuaciones(10)
    else:
        return Posibles_Puntuaciones(1)
    
def Posibles_Puntuaciones(Valor):
    Puntuaciones={
        1: CG+"0-Muy Bajo"+FR,
        2: CGL+"1-Bajo"+FR,
        3: CGL+"2-Bajo Alto"+FR,
        4: CGL+"4-Medio Bajo"+FR,
        5: CRL+"5-Medio"+FR,
        6: CRL+"6-Medio Alto"+FR,
        7: CR+"7-Alto bajo"+FR,
        8: CR+"8-Alto"+FR,
        9: CR+"9-Muy Alto"+FR,
        10: CR+"10-Extremo"+FR
    }
    return Puntuaciones.get(Valor,"No fue posible calcular el riesgo")

def Evaluar_Cantidad(Cantidad):
    Valoracion={
        1: CG+", Nulo"+FR,
        2: CGL+", Bajo"+FR,
        3: CRL+", Medio"+FR,
        4: CR+", Alto"+FR,
        5: CR+", Masivo"+FR
    }
    return Valoracion.get(Cantidad,"No fue posible realizar el calculo")

def Num_De_Usuarios(Data1):
    NumeroDeUsuarios=int(Data1["data"]['numDistinctUsers'])
   
    while NumeroDeUsuarios>0:
        if(NumeroDeUsuarios<3):
            return FC+str(NumeroDeUsuarios)+FR+Evaluar_Cantidad(2)
        elif(NumeroDeUsuarios<6):
            return FC+str(NumeroDeUsuarios)+FR+Evaluar_Cantidad(3)
        elif(NumeroDeUsuarios<9):
            return FC+str(NumeroDeUsuarios)+FR+Evaluar_Cantidad(4)
        elif(NumeroDeUsuarios>9):
            return FC+str(NumeroDeUsuarios)+FR+Evaluar_Cantidad(5)
    else:
        NumeroDeUsuarios="0"
        return FC+NumeroDeUsuarios+FR+Evaluar_Cantidad(1)
    
def Num_De_Reportes(Data1):
    CantidadR=Data1["data"]['totalReports']
    while CantidadR>0:
        if(CantidadR<3):
            return FC+str(CantidadR)+FR+Evaluar_Cantidad(2)
        elif(CantidadR<6):
            return FC+str(CantidadR)+FR+Evaluar_Cantidad(3)
        elif(CantidadR<9):
            return FC+str(CantidadR)+FR+Evaluar_Cantidad(4)
        elif(CantidadR>9):
            return FC+str(CantidadR)+FR+Evaluar_Cantidad(5)
    else:
        CantidadR="0"
        return FC+CantidadR+FR+Evaluar_Cantidad(1)
                     
def Fecha_Ultimo_Report(Data1):
    try:
        FechaBruta=Data1["data"]["lastReportedAt"]
        Buscar=FechaBruta.index("T")
        AñoMesDia=FechaBruta[:Buscar]
        Hora=FechaBruta[Buscar+1:-6]
        
        ProcesarFecha=AñoMesDia+" "+Hora

        ProcesarFecha=datetime.strptime(ProcesarFecha[2:],"%y-%m-%d %H:%M:%S")
        FechaActual=datetime.now(tz=None)
        return str(FechaActual-ProcesarFecha)

    except AttributeError:
        return "nunca"
        
def Evaluar_Ultimo_Reporte(Data1):
        try:
            Dias=Fecha_Ultimo_Report(Data1)
            Buscar=Dias.index("d")
            Dias1=int(Dias[:Buscar-1])
            DiasStr=Dias[:Buscar-1]
            
            if Dias1 == 0:
                DiasStr="0"
                return (CR+DiasStr+" dias, Menos de 24 horas"+FR)
            elif Dias1 < 3:
                DiasStr="1"
                return (CR+DiasStr+" dias, Menos de 2 dias"+FR)
            elif Dias1 < 7:
                return (CRL+DiasStr+" dias, Menos de 1 semana"+FR)
            elif Dias1 > 7 and Dias1 < 30:
                return (CRL+DiasStr+" dias, Mas de 1 semana"+FR)
            elif Dias1 > 30 and Dias1 < 60:
                return (CGL+DiasStr+" dias, Mas de 1 mes"+FR)
            elif Dias1 > 60 and Dias1 < 120:
                return (CG+DiasStr+" dias, Mas de 2 meses"+FR)
            elif Dias1 > 120:
                return (CG+DiasStr+" dias, Mas de 4 meses"+FR)
        
        except ValueError:
            try:
                Horas=Fecha_Ultimo_Report(Data1)
                Buscar=":"
                for Buscar in str(Horas):
                    DiasStr="0"
                    return (CR+DiasStr+" dias, Menos de 24 horas"+FR)
                else:
                    None
            except ValueError:    
                return (CG+"No tiene registros de reportes"+FR)

def Info_Geografica(Data2):
    A=(FC+"Codigo del pais "+FR)
    B=(FC+", Region "+FR)
    C=(FC+", City "+FR)
    D=str(Data2["country_code"])
    E=str(Data2["region"])
    F=str(Data2["city"])
    GeograIP=A+D+B+E+C+F
    return GeograIP

def Trafico_NoHumano(Data2):    
    if(Data2["bot_status"]==True): 
        return CR+"si"+FR
    else: 
        return CG+"No"+FR

def Conexion_Proxy(Data2):
    if(Data2["proxy"]==True): 
        return CR+"si"+FR
    else: 
        return CG+"No"+FR

def Nodo_Tor(Data2):
    if(Data2["active_tor"]==True and Data2["tor"]==True):
        return CR+"si"+FR
    else: 
        return CG+"No"+FR

def Limpiao_No1(Data1):
    if(Data1["data"]["abuseConfidenceScore"]>30): 
        return CR+"Maliciosa"+FR
    else: 
        return CG+"Limpia"+FR

def Limpia_No2(Data2):
    if(Data2["fraud_score"]>30): 
        return CR+"Maliciosa"+FR
    else: 
        return CG+"Limpia"+FR

def Limpia_No3(Data3):
    try:
        Detect=int(len(Data3["detected_urls"]))
        Resolu=int(len(Data3["resolutions"]))
        Muest=int(len(Data3["detected_referrer_samples"]))
        if(Detect>2 and Resolu>1 and Muest>2):
            return CR+"Maliciosa"+FR
        else: 
            return CG+"Limpia"+FR
        
    except KeyError:
        return CG+"Limpia"+FR

def Verificar_resoluciones(Data3):
    try:
        RegistroDeNombres=len(Data3['resolutions'])
        if RegistroDeNombres>0:
            return RegistroDeNombres
        else:
            return 0
    except KeyError:
        return 0

def Numero_DeRegistrosHN(Data3):
    NumeroDeRegistros=Verificar_resoluciones(Data3)
    
    while NumeroDeRegistros>0:
    #Nombre de host a los que ha resolvido esta ip
        if NumeroDeRegistros==1:
            return FC+"1, "+FR+Posibles_Puntuaciones(1)
        elif NumeroDeRegistros==2:
            return FC+"2, "+FR+Posibles_Puntuaciones(2)
        elif NumeroDeRegistros==3:
            return FC+"3, "+FR+Posibles_Puntuaciones(3)
        elif NumeroDeRegistros==4:
            return FC+"4, "+FR+Posibles_Puntuaciones(4)
        elif NumeroDeRegistros==5:
            return FC+"5, "+FR+Posibles_Puntuaciones(5)
        elif NumeroDeRegistros==6:
            return FC+"6, "+FR+Posibles_Puntuaciones(6)
        elif NumeroDeRegistros==7:
            return FC+"7, "+FR+Posibles_Puntuaciones(7)
        elif NumeroDeRegistros==8:
            return FC+"8, "+FR+Posibles_Puntuaciones(8)
        elif NumeroDeRegistros==9:
            return FC+"9, "+FR+Posibles_Puntuaciones(9)
        elif NumeroDeRegistros>=10:
            return FC+str(int(NumeroDeRegistros))+", "+FR+Posibles_Puntuaciones(10)
    else:
        return CG+"No se encontraron registros de la misma"+FR

def Informacion_Resolucion(Data1,Data2,Data3):    
    Resolu1=Verificar_resoluciones(Data3)
    Resoluciones=Numero_DeRegistrosHN(Data3)
    
    def Nombre_actual(Data1):
        try:
            Verificacion=Verificacion_Hostname(Data1,Data2)
            return Verificacion
        except KeyError:
            #try:
                Verifi=Data1['data']['hostnames']
                return Verifi
            #except KeyError: return " No tiene un nombre en la actualidad"
            
    NombreActual=str(Nombre_actual(Data1))
    
    if Resolu1==0:
        print(
            CM+"\nRegistro de resoluciones"+FR
            ,SB+"\n 1)"+SR+" Posee registros de cambio de nombre: "+CG+"No"+FR
            ,SB+"\n 2)"+SR+" Cuantos cambios presenta: "+Resoluciones
            ,SB+"\n "+SR+CM+"3) Historial:"+FR
            ,SB+"\n   a)"+SR+" Nombre actual:"+FC+NombreActual+FR)
        
    elif Resolu1>=3:
        print(
            CM+"\nRegistro de resoluciones"+FR
            ,SB+"\n 1)"+SR+" Posee registros de cambio de nombre: "+CY+"Si"+FR
            ,SB+"\n 2)"+SR+" Cuantos cambios presenta: "+Resoluciones
            ,SB+"\n "+SR+CM+"3) Historial:"+FR
            ,SB+"\n   a)"+SR+" Nombre actual:"+FC+str(Data1["data"]["hostnames"])+FR
            ,SB+"\n   b)"+SR+" Nombres anteriores y fecha del resultado:"
            ,SB+"\n    b.1) Nombre "+SR+CY+Data3["resolutions"][0]["hostname"]+FR+", Fecha del resultado "+FC+Data3["resolutions"][0]["last_resolved"]+FR
            ,SB+"\n    b.2) Nombre "+SR+CY+Data3["resolutions"][1]["hostname"]+FR+", Fecha del resultado "+FC+Data3["resolutions"][1]["last_resolved"]+FR
            ,SB+"\n    b.3) Nombre "+SR+CY+Data3["resolutions"][2]["hostname"]+FR+", Fecha del resultado "+FC+Data3["resolutions"][2]["last_resolved"]+FR
        )

def Urls_Detectadas(Data3):
    
    def Urls_NDetectadas(Data3):
        try:
            return (len(Data3['detected_urls']))
        except KeyError:
            return 0

    UrlsDetectadas=Urls_NDetectadas(Data3)

    if UrlsDetectadas>3:
        print(
            CM+"\nUrls en esta direccion"+FR
            ,SB+"\n 1)"+SR+" Se encontraron direcciones en esta direccion: "+CY+"Si"+FR
            ,SB+"\n 2)"+SR+" Cuantas fueron detectadas como maliciosas: "+str(UrlsDetectadas)
            ,SB+"\n "+SR+CM+"3) Historial:"+FR
            ,SB+"\n   b)"+SR+" Urls detectadas como maliciosas:"
            ,SB+"\n    b.1) "+SR+CY+str(Data3['detected_urls'][0]["url"])+FR+", fecha del escaneo "+FC+str(Data3['detected_urls'][0]["scan_date"])+FR+", Se escaneo con: "+FC+str(Data3['detected_urls'][0]["total"])+FR+" AV,  esta positivo en: "+CR+str(Data3['detected_urls'][0]["positives"])+FR
            ,SB+"\n    b.2) "+SR+CY+str(Data3['detected_urls'][1]["url"])+FR+", fecha del escaneo "+FC+str(Data3['detected_urls'][0]["scan_date"])+FR+", Se escaneo con: "+FC+str(Data3['detected_urls'][1]["total"])+FR+" AV,  esta positivo en: "+CR+str(Data3['detected_urls'][1]["positives"])+FR
            ,SB+"\n    b.3) "+SR+CY+str(Data3['detected_urls'][2]["url"])+FR+", fecha del escaneo "+FC+str(Data3['detected_urls'][0]["scan_date"])+FR+", Se escaneo con: "+FC+str(Data3['detected_urls'][2]["total"])+FR+" AV,  esta positivo en: "+CR+str(Data3['detected_urls'][2]["positives"])+FR
            ,SB+"\n    b.4) "+SR+CY+str(Data3['detected_urls'][3]["url"])+FR+", fecha del escaneo "+FC+str(Data3['detected_urls'][0]["scan_date"])+FR+", Se escaneo con: "+FC+str(Data3['detected_urls'][3]["total"])+FR+" AV,  esta positivo en: "+CR+str(Data3['detected_urls'][3]["positives"])+FR
        )
        
    else:
        print(
        CM+"\nUrls en esta direccion"+FR
        ,SB+"\n 1)"+SR+" Se encontraron direcciones en esta direccion: "+CG+"No"+FR
        ,SB+"\n 2)"+SR+" Cuantas fueron detectadas como maliciosas: "+CG+"0"+FR
    )



"""
Data5={'search': '103.118.253.228/24', 'result': {'count': 5, 'limit': 100, 'from': '', 'next': None, 'inetnums': [{'inetnum': '103.118.252.0 - 103.118.255.255', 'inetnumFirst': 281472417594368, 'inetnumLast': 281472417595391, 'inetnumFirstString': '281472417594368', 'inetnumLastString': '281472417595391', 'as': {'asn': 55933, 'name': 'CLOUDIE-AS-AP', 'type': 'Cable/DSL/ISP', 'route': '103.118.252.0/22', 'domain': 'http://worria.com/'}, 'netname': 'Snowcomic', 'nethandle': '', 'description': ['MIXTELECOM LLC'], 'modified': '2022-11-11T07:52:35Z', 'country': 'CN', 'city': '', 'address': [], 'abuseContact': [{'id': 'AC1601-AP', 'role': 'ABUSE CNNICCN', 'email': 'ipas@cnnic.cn', 'phone': '+000000000', 'country': 'ZZ', 'city': '', 'address': ['Beijing, China']}], 'adminContact': [{'id': 'LY4158-AP', 'person': 'luo yupang', 'email': 'abuse@cloudie.hk', 'phone': '+852-61725306', 'country': 'CN', 'city': '', 'address': ['a-5 floor taisang building xilidaxuecheng nanshan district Shenzhen']}], 'techContact': [{'id': 'LY4158-AP', 'person': 'luo yupang', 'email': 'abuse@cloudie.hk', 'phone': '+852-61725306', 'country': 'CN', 'city': '', 'address': ['a-5 floor taisang building xilidaxuecheng nanshan district Shenzhen']}], 'org': None, 'mntBy': [{'mntner': 'MAINT-CNNIC-AP', 'email': 'ipas@cnnic.cn'}], 'mntDomains': [], 'mntLower': [{'mntner': 'MAINT-CNNIC-AP', 'email': 'ipas@cnnic.cn'}], 'mntRoutes': [{'mntner': 'MAINT-CNNIC-AP', 'email': 'ipas@cnnic.cn'}], 'remarks': [], 'source': 'APNIC'}, {'inetnum': '103.85.36.0 - 103.192.159.255', 'inetnumFirst': 281472415376384, 'inetnumLast': 281472422420479, 'inetnumFirstString': '281472415376384', 'inetnumLastString': '281472422420479', 'as': None, 'netname': 'NON-RIPE-NCC-MANAGED-ADDRESS-BLOCK', 'nethandle': '', 'description': ['IPv4 address block not managed by the RIPE NCC'], 'modified': '2022-05-05T14:17:14Z', 'country': 'EU', 'city': '', 'address': [], 'abuseContact': [], 'adminContact': [], 'techContact': [], 'org': None, 'mntBy': [{'mntner': 'RIPE-NCC-HM-MNT', 'email': ''}], 'mntDomains': [], 'mntLower': [], 'mntRoutes': [], 'remarks': ['------------------------------------------------------', '', 'For registration information,', 'you can consult the following sources:', '', 'IANA', 'http://www.iana.org/assignments/ipv4-address-space', 'http://www.iana.org/assignments/iana-ipv4-special-registry', 'http://www.iana.org/assignments/ipv4-recovered-address-space', '', 'AFRINIC (Africa)', 'http://www.afrinic.net/ whois.afrinic.net', '', 'APNIC (Asia Pacific)', 'http://www.apnic.net/ whois.apnic.net', '', 'ARIN (Northern America)', 'http://www.arin.net/ whois.arin.net', '', 'LACNIC (Latin America and the Carribean)', 'http://www.lacnic.net/ whois.lacnic.net', '', '------------------------------------------------------', '****************************', '* THIS OBJECT IS MODIFIED', '* Please note that all data that is generally regarded as personal', '* data has been removed from this object.', '* To view the original object, please query the RIPE Database at:', '* http://www.ripe.net/whois', '****************************'], 'source': 'RIPE'}, {'inetnum': '103.0.0.0 - 103.255.255.255', 'inetnumFirst': 281472409796608, 'inetnumLast': 281472426573823, 'inetnumFirstString': '281472409796608', 'inetnumLastString': '281472426573823', 'as': None, 'netname': 'APNIC-AP', 'nethandle': '', 'description': ['Asia Pacific Network Information Centre', 'Regional Internet Registry for the Asia-Pacific Region', '6 Cordelia Street', 'PO Box 3646', 'South Brisbane, QLD 4101', 'Australia'], 'modified': '2020-05-20T04:31:46Z', 'country': 'AU', 'city': '', 'address': [], 'abuseContact': [{'id': 'AA1452-AP', 'role': 'ABUSE APNICAP', 'email': 'helpdesk@apnic.net', 'phone': '+000000000', 'country': 'ZZ', 'city': '', 'address': ['Brisbane, Australia']}], 'adminContact': [{'id': 'HM20-AP', 'role': 'APNIC Hostmaster', 'email': 'helpdesk@apnic.net', 'phone': '+61 7 3858 3100', 'country': 'AU', 'city': '', 'address': ['6 Cordelia Street', 'South Brisbane', 'QLD 4101']}], 'techContact': [{'id': 'NO4-AP', 'person': 'APNIC Network Operations', 'email': 'netops@apnic.net', 'phone': '+61 7 3858 3100', 'country': 'AU', 'city': '', 'address': ['6 Cordelia Street', 'South Brisbane', 'QLD 4101']}], 'org': None, 'mntBy': [{'mntner': 'APNIC-HM', 'email': 'helpdesk@apnic.net\nnetops@apnic.net'}], 'mntDomains': [], 'mntLower': [{'mntner': 'APNIC-HM', 'email': 'helpdesk@apnic.net\nnetops@apnic.net'}], 'mntRoutes': [], 'remarks': [], 'source': 'APNIC'}, {'inetnum': '0.0.0.0 - 255.255.255.255', 'inetnumFirst': 281470681743360, 'inetnumLast': 281474976710655, 'inetnumFirstString': '281470681743360', 'inetnumLastString': '281474976710655', 'as': None, 'netname': 'IANA-IPV4-MAPPED-ADDRESS', 'nethandle': 'NET6-0-0-0-0-0-FFFF-1', 'description': [], 'modified': '2022-02-26T00:00:00Z', 'country': 'US', 'city': 'Los Angeles', 'address': ['12025 Waterfront Drive', 'Suite 300'], 'abuseContact': [], 'adminContact': [], 'techContact': [], 'org': {'org': 'IANA', 'name': 'Internet Assigned Numbers Authority', 'email': 'abuse@iana.org', 'phone': '+1-310-301-5820', 'country': 'US', 'city': 'Los Angeles', 'postalCode': '90292', 'address': ['12025 Waterfront Drive', 'Suite 300']}, 'mntBy': [], 'mntDomains': [], 'mntLower': [], 'mntRoutes': [], 'remarks': ['IPv4-mapped Address [RFC4291]'], 'source': 'ARIN'}, {'inetnum': ':: - ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', 'inetnumFirst': 0, 'inetnumLast': 3.402823669209385e+38, 'inetnumFirstString': '0', 'inetnumLastString': '340282366920938463463374607431768211455', 'as': None, 'netname': 'IANA-BLK', 'nethandle': '', 'description': ['The whole IPv6 address space'], 'modified': '2022-05-23T14:49:16Z', 'country': 'EU', 'city': '', 'address': [], 'abuseContact': [], 'adminContact': [], 'techContact': [], 'org': {'org': 'ORG-IANA1-RIPE', 'name': 'Internet Assigned Numbers Authority', 'email': 'bitbucket@ripe.net', 'phone': '', 'country': '', 'city': '', 'postalCode': '', 'address': ['see http://www.iana.org']}, 'mntBy': [{'mntner': 'RIPE-NCC-HM-MNT', 'email': ''}], 'mntDomains': [], 'mntLower': [{'mntner': 'RIPE-NCC-HM-MNT', 'email': ''}], 'mntRoutes': [], 'remarks': ['This network is not allocated.', 'This object is here for Database', 'consistency and to allow hierarchical', 'authorisation checks.', '****************************', '* THIS OBJECT IS MODIFIED', '* Please note that all data that is generally regarded as personal', '* data has been removed from this object.', '* To view the original object, please query the RIPE Database at:', '* http://www.ripe.net/whois', '****************************'], 'source': 'RIPE'}]}}

#Informacion de la general

#ASN
#Informacion de la red

ASN=Data5['result']["inetnums"][0]["as"]["asn"]
Nombre=Data5['result']["inetnums"][0]["as"]["name"]
RedGrande=Data5['result']["inetnums"][0]["as"]["route"]

#Informacion del isp, nombre de la red y fecha de la ultima actualizacion de los datos
ISP=Data5['result']["inetnums"][0]["description"]
NombreDeLaRed=Data5['result']["inetnums"][0]["netname"]
FechaDeActualizacion=Data5['result']["inetnums"][0]["modified"]

#contactos
#1-Contacto de abuso
AbuseContact=Data5['result']["inetnums"][0]["abuseContact"][0]["role"]+", email: "+Data5['result']["inetnums"][0]["abuseContact"][0]["email"]
AdminContact=str(Data5['result']["inetnums"][0]["adminContact"][0]["person"])+", email: "+str(Data5['result']["inetnums"][0]["adminContact"][0]["email"])+", address: "+str(Data5['result']["inetnums"][0]["adminContact"][0]["address"])
#+","+Data5['result']["inetnums"][0]["abuseContact"]["role"]["email"]+","+Data5['result']["inetnums"][0]["abuseContact"]["role"]["address"]

print(
    ASN,
    Nombre,
    RedGrande,
    ISP,
    NombreDeLaRed,
    FechaDeActualizacion,
    "\n\n",
    AbuseContact,
    "\n\n",
    AdminContact,
    
    
    
)
"""



