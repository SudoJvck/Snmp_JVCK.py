from pysnmp.hlapi import *
import pyfiglet

ascii_banner = pyfiglet.figlet_format("SNMPJVCK")
print(ascii_banner)


def snmp_walk(ip, community, oids):
    for oid in oids:
        errorIndication, errorStatus, errorIndex, varBinds = next(
            getCmd(SnmpEngine(),
                   CommunityData(community),
                   UdpTransportTarget((ip, 161)),
                   ContextData(),
                   ObjectType(ObjectIdentity(oid)))
        )

        if errorIndication:
            print(errorIndication)
        elif errorStatus:
            print('%s at %s' % (errorStatus.prettyPrint(),
                                errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        else:
            for varBind in varBinds:
                print(f'{varBind[0]} = {varBind[1]}')

if __name__ == '__main__':
    # Get SNMP community string from user
    community_string = input("Enter the SNMP community string: ")
    # Get IP address from user
    ip_address = input("Enter the IP address of the device: ")
    # Get OIDs to poll from user
    oids = input("Enter the OIDs to poll (separated by commas): ").split(',')
    # Perform SNMP poll
    snmp_walk(ip_address, community_string, oids)

'''
#  Sample OIDs to poll
oids = ['1.3.6.1.2.1.1.1.0',   # sysDescr
        '1.3.6.1.2.1.1.2.0',   # sysObjectID
        '1.3.6.1.2.1.1.3.0',   # sysUpTime
        '1.3.6.1.2.1.1.4.0',   # sysContact
        '1.3.6.1.2.1.1.5.0'    # sysName
       ]
'''
