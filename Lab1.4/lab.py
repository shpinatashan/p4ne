
"""
class Subnet:
    def __init__(self, n = "0.0.0.0", p = "0"):
        self.network = n
        self.prefix = p
    def __str__(self):
        return self.network+self.prefix
    def getnet(self):
        return self.network
    def getprefix(self):
        return self.prefix


n1 = Subnet("192.168.1.0", "/24")
print(n1)
print(n1.__str__())
print(n1.getnet())
print(n1.getprefix())
print(type(n1))


class Addr_plan_entry(Subnet):
    def __init__(self, n = "0.0.0.0", p = "0", gw="0.0.0.0"):
        Subnet.__init__(self, n, p)
        self.gateway = gw
    def getway(self):
        return self.gateway
    def __str__(self):
        return "Network: %s, prefix: %s, gateway: %s" %(self.network, self.prefix, self.gateway)

n2 = Addr_plan_entry("192.168.1.0", "/24", "192.168.1.1")
print(n2)
print(n2.__str__())
print(n2.getnet())
print(n2.getprefix())
print(dir(n2))
"""
import ipaddress
from ipaddress import IPv4Network
import random

class IPv4RandomNetwork(ipaddress.IPv4Network):
    def __init__(self, mask_min=8, mask_max=24):
        IPv4Network.__init__(self,(random.randint(0x0b000000, 0xdf000000),random.randint(mask_min, mask_max)), strict=False)

    def regular(self):
        return not(self.is_private)
    def key_value(self):
        return int(self.netmask) * 2^32 + int(self.network_address)        #маску помещаем в разряды, тким образом сначала сортировка по маске и затем по ip


list_of_address = [];
for i in range(20):
    list_of_address.append(IPv4RandomNetwork(8,24))


def sortfunc(x):
    return x.key_value()

for adr in sorted(list_of_address, key=sortfunc):
        print(adr)


# net1 = ipaddress.IPv4Network((random.randint(0xb000000,0xf000000),random.randint(8,24)),strict = False)

