from RS4LyExtra02 import CB,CR,CBL,FR,CG,CGL,CRL,FC,CM,CY,CA


"""
#Ipabuse
Data1={'data': {'ipAddress': '12.12.12.12', 'isPublic': True, 'ipVersion': 4, 'isWhitelisted': False, 'abuseConfidenceScore': 0, 'countryCode': 'US', 'usageType': 'Fixed Line ISP', 'isp': 'Alascom Inc.', 'domain': 'att.com', 'hostnames': ['doh.att.net'], 'totalReports': 0, 'numDistinctUsers': 0, 'lastReportedAt': '2022-07-26T08:11:03+00:00'}}
#Ip quality score
Data2={'success': True, 'message': 'Success', 'fraud_score': 100, 'country_code': 'US', 'region': 'California', 'city': 'San Francisco', 'ISP': 'AT&T Services', 'ASN': 7018, 'organization': 'AT&T Services', 'is_crawler': False, 'timezone': 'America/Los_Angeles', 'mobile': False, 'host': 'doh.att.net', 'proxy': True, 'vpn': True, 'tor': False, 'active_vpn': False, 'active_tor': False, 'recent_abuse': True, 'bot_status': True, 'connection_type': 'Premium required.', 'abuse_velocity': 'Premium required.', 'zip_code': 'N/A', 'latitude': 37.77000046, 'longitude': -122.41999817, 'request_id': '9EiVOmsgqR'}
#Abstract Api
Data4={'ip_address': '12.12.12.12', 'city': None, 'city_geoname_id': None, 'region': None, 'region_iso_code': None, 'region_geoname_id': None, 'postal_code': None, 'country': 'United States', 'country_code': 'US', 'country_geoname_id': 6252001, 'country_is_eu': False, 'continent': 'North America', 'continent_code': 'NA', 'continent_geoname_id': 6255149, 'longitude': -97.822, 'latitude': 37.751, 'security': {'is_vpn': False}, 'timezone': {'name': 'America/Chicago', 'abbreviation': 'CST', 'gmt_offset': -6, 'current_time': '11:42:09', 'is_dst': False}, 'flag': {'emoji': '🇺🇸', 'unicode': 'U+1F1FA U+1F1F8', 'png': 'https://static.abstractapi.com/country-flags/US_flag.png', 'svg': 'https://static.abstractapi.com/country-flags/US_fla ag.svg'}, 'currency': {'currency_name': 'USD', 'currency_code': 'USD'}, 'connection': {'autonomous_system_number': 7018, 'autonomous_system_organization': 'ATT-INTERNET4', 'connection_type': 'Corporate', 'isp_name': 'Alascom, Inc.', 'organization_name': 'AT&T Services'}}
"""


def Verificacion_VPN(Data2,Data4):
        VPN2=Data2['vpn']
        VPN22=Data2["active_vpn"]
        VPN4=Data4['security']['is_vpn']
        
        VPNF=Data4['security']['is_vpn']
        
        if VPNF==True:
            VPNF=CG+"Si"+FR
        else:
            VPNF=CR+"No"+FR
        
        if VPN2 == VPN4 or VPN22 == VPN4:
            return VPNF+CG+", Confirmado"+FR
        else:
            return VPNF+CY+", No Confirmado"+FR

def Verificacion_Hostname(Data1,Data2):
        try:
            NH2=Data2['host']
            NH2="['"+NH2+"']"
            NH1=Data1['data']["hostnames"]
            NHF=Data2['host']
            
            if str(NH1) == NH2:
                NHF=FC+str(NHF)+CG+", Confirmado"+FR
                return NHF
            else:
                NHF=FC+str(NHF)+CY+", No Confirmado"+FR
                return NHF
        except KeyError:
            return Data1['data']["hostnames"]
        
def Verificacion_Pais(Data4,Data2,Data1):
        #Country Code
        CC1=Data1['data']["countryCode"]
        CC2=Data2['country_code']
        CC4=Data4['country_code']
        
        CCF=Data4['country_code']
        
        if CC1 == CC2 == CC4:
            CCF=FC+CCF+CG+", Confirmado"+FR
            return CCF
        else:
            CCF=FC+CCF+CY+", No Confirmado"+FR
            return CCF

def Verificacion_Org(Data2,Data4):
        #Nombre de la Org
        NO2=Data2['organization']
        NO4=Data4['connection']['organization_name']
        NOF=Data4['connection']['organization_name']
        if NO2 == NO4:
            NOF=FC+NOF+CG+", Confirmado"+FR
            return NOF
        else:
            NOF=FC+NOF+CY+", No Confirmado"+FR
            return NOF

def Verificacion_Isp(Data1,Data2,Data4):
        #ISP, la data del 4 y del 1 es igual pero la del 2 es diferente
        ISP1=Data1['data']["isp"]
        ISP2=Data2['ISP']
        ISP4=Data4['connection']['isp_name']
        ISPF=Data4['connection']['isp_name']
        if ISP1 == ISP2 == ISP4:
            ISPF=FC+ISPF+CG+", Confirmado"+FR
            return ISPF
        elif ISP2 == ISP4:
            ISPF=FC+ISPF+CGL+", Confirmado"+FR
            return ISPF
        else:
            ISPF=FC+ISPF+CY+", No Confirmado"+FR
            return ISPF

def Verificar_infoGeografica(Data1,Data2,Data4):

    Verificar=Verificacion_Pais(Data4,Data2,Data1)

    B=(FC+", Region "+FR)
    C=(FC+", City "+FR)
    E=str(Data2["region"])
    F=str(Data2["city"])
    
    if "No" in Verificar:
        GeograIP=B+E+C+F+CY+"No, confirmado"+FR
        return GeograIP
    else:
        GeograIP=B+E+C+F+CG+", Confirmado"+FR
        return GeograIP





