from pysnmp.hlapi import * #high-level API

ipaddr_string = '10.31.70.107'
port_int = 161

print("Result from getCmd")
snmp_object = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
result = getCmd(SnmpEngine(),
	CommunityData('public', mpModel=0),
	UdpTransportTarget((ipaddr_string, port_int)),
	ContextData(),
	ObjectType(snmp_object))

for r in result:
	for s in r[3]:
		print(s)



print("\n \n Result from nextCmd ")
snmp_object = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')
result2 = nextCmd (SnmpEngine(),
	CommunityData('public', mpModel=0),
	UdpTransportTarget((ipaddr_string, port_int)),
	ContextData(),
	ObjectType(snmp_object), lexicographicMode=False)

for r in result2:
	for s in r[3]:
		print(s)